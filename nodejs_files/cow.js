var exec = require('child_process').exec;
function puts(error, stdout, stderr) { console.log(stdout) }


var awsIot = require('aws-iot-device-sdk');

var device = awsIot.device({
  keyPath: '/home/chip/private.pem.key',
  certPath: '/home/chip/certificate.pem.crt',
  caPath: '/home/chip/iotbutton/root-CA.pem',
  clientId: 'chip',
  region: 'ap-northeast-1',
  reconnectPeriod: 5000
});

device.on('connect', function() {
	console.log('connect');
	device.subscribe('chip/led');
});

//Prepare GPIO
exec("echo 408 > /sys/class/gpio/export", puts);
exec("echo out > /sys/class/gpio/gpio408/direction", puts);
console.log("Determine GPIO 408 direction:");
exec("cat /sys/class/gpio/gpio408/direction", puts);

 
device.on('message', function(topic, payload) {
	// console.log('message', topic, payload.toString());
	if (payload.toString().toUpperCase() == 'ON') {
		console.log('LED: ON');
                exec("echo 0 > /sys/class/gpio/gpio408/value", puts);
	} // end if 
	else if (payload.toString().toUpperCase() == 'OFF') {
		console.log('LED: OFF');
                exec("echo 1 > /sys/class/gpio/gpio408/value", puts);
	} // end else if
	else {
		console.log('UNKNOWN COMMAND');
	} // end else
});
