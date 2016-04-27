/*
Name: 			UI Elements / Charts - Examples
Written by: 	Okler Themes - (http://www.okler.net)
Theme Version: 	1.4.1
*/

(function( $ ) {

	'use strict';


	/*
	Chartist: Line Chart - Scatter Diagram With Responsive Settings
	*/
	(function() {
		var times = function(n) {
			return Array.apply(null, new Array(n));
		};

		var data = times(52).map(Math.random).reduce(function(data, rnd, index) {
			data.labels.push(index + 1);
			data.series.forEach(function(series) {
				series.push(Math.random() * 100)
			});

			return data;
		}, {
			labels: [],
			series: times(4).map(function() {
				return new Array()
			})
		});

		var data = {
		  labels: ['1', '2', '3', '4', '5', '6'],
		  series: [
		    {
		      data: [1, 0, 1, 0, 1, 10]
		    }
		  ]
		};

		var options = {
			showLine: false,
			axisX: {
				labelInterpolationFnc: function(value, index) {
					return index % 13 === 0 ? 'W' + value : null;
				}
			}
		};

		var responsiveOptions = [
			['screen and (min-width: 640px)', {
				axisX: {
					labelInterpolationFnc: function(value, index) {
						return index % 4 === 0 ? 'W' + value : null;
					}
				}
			}]
		];

		new Chartist.Line('#ChartistLineScatterDiagramWithResponsiveSettings', data, options, responsiveOptions);
	})();

	/*
	Chartist: CSS Animation
	*/
	(function() {
		var data = {
			labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
			series: [
				[1, 2, 2.7, 0, 3, 5, 3, 4, 8, 10, 12, 7],
				[0, 1.2, 2, 7, 2.5, 9, 5, 8, 9, 11, 14, 4],
				[10, 9, 8, 6.5, 6.8, 6, 5.4, 5.3, 4.5, 4.4, 3, 2.8]
			]
		};

		var responsiveOptions = [
			[
				'only screen', {
					axisX: {
						labelInterpolationFnc: function(value, index) {
							// Interpolation function causes only every 2nd label to be displayed
							if (index % 2 !== 0) {
								return false;
							} else {
								return value;
							}
						}
					}
				}
			]
		];

		new Chartist.Line('#ChartistCSSAnimation', data, null, responsiveOptions);
	})();

}).apply( this, [ jQuery ]);