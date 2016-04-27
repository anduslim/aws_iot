var awsIot = require('aws-iot-device-sdk');
var EstimoteSticker = require('./estimote-sticker');

var device = awsIot.device({
  keyPath: '/home/chip/private.pem.key',
  certPath: '/home/chip/certificate.pem.crt',
  caPath: '/home/chip/iotbutton/root-CA.pem',
  clientId: 'chip',
  region: 'ap-northeast-1',
  reconnectPeriod: 5000
});

// EstimoteSticker.on('discover', function(estimoteSticker) {
//   console.log(estimoteSticker);
// });

//returns a sticker oject on discover in json
EstimoteSticker.on('discover', function(estimoteSticker) {
	var estimoteData;
	relevantdata(estimoteSticker,function(data) {	
	estimoteData = data;
});
	publish(estimoteData);
});

EstimoteSticker.startScanning();

// Parse data and returns in callback
function relevantdata(estimoteSticker, callback) {
	// only receive from 2 stickers:
	// TOP - 	d0d3fa86ca7645ec9bd96af443105c979fb993a5
	// BOTTOM - d0d3fa86ca7645ec9bd96af46b59d8d1ae708533
	// console.log(estimoteSticker);
	uuid = estimoteSticker.uuid;
	if (uuid == 'd0d3fa86ca7645ec9bd96af443105c979fb993a5') { 
		// console.log('TOP');
		var relevantJson ={'uuid':estimoteSticker.uuid, 'battery_level':estimoteSticker.batteryLevel, 'power':estimoteSticker.power, 'acc_x':estimoteSticker.acceleration['x'], 'acc_y':estimoteSticker.acceleration['y'], 'acc_z':estimoteSticker.acceleration['z'], 'pos':'top'};
	} // end if 
	else if (uuid == 'd0d3fa86ca7645ec9bd96af46b59d8d1ae708533') {
		// console.log('BOTTOM');
		var relevantJson ={'uuid':estimoteSticker.uuid, 'battery_level':estimoteSticker.batteryLevel, 'power':estimoteSticker.power, 'acc_x':estimoteSticker.acceleration['x'], 'acc_y':estimoteSticker.acceleration['y'], 'acc_z':estimoteSticker.acceleration['z'], 'pos':'bottom'};
	} // end else if 
	else {
		console.log('UNKNOWN STICKER');
	} // end else

	// do some processing for fun:
	console.log(estimoteSticker.acceleration['z'])
	if (estimoteSticker.acceleration['z'] <= -500.0) 
		console.log('state: close')
	else
		console.log('state: open')

	callback(relevantJson);
} // end relevantdata

function publish(sticker) {
	console.log("publishing sticker reading!");
	device.publish('chip/sticker', JSON.stringify(sticker));
} // end publish

function exit() {
	process.exit();
} // exit 

process.on('SIGINT', exit);
