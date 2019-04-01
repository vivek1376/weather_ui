document.addEventListener("DOMContentLoaded", function () {
    google.charts.load('current', {'packages':['annotationchart']});
    //google.charts.load('current', {packages: ['corechart', 'line']});
    google.charts.setOnLoadCallback(drawLineColors);

    var chart = undefined;
    var data = undefined;
    var options = undefined;

    function drawLineColors(response) {
        data = new google.visualization.DataTable();
        // data.addColumn('string', 'X');
        // data.addColumn('string', 'Min Temp');
        // data.addColumn('string', 'Max Temp');
	
	data.addColumn('date', 'X');
	data.addColumn('number', 'Tmin');
	data.addColumn('number', 'Tmax');
	
	if (response != undefined) {
	    for (var i = 0; i < response.length; i++) {
		data.addRows([[
		    new Date(parseInt(response[i]["DATE"].substring(0, 4)),
			     parseInt(response[i]["DATE"].substring(4, 6)),
			     parseInt(response[i]["DATE"].substring(6, 8))),
		    parseInt(response[i]["TMIN"]),
		    parseInt(response[i]["TMAX"])]]);
	    }
	}
	
        options = {
            hAxis: {
                title: 'Date',
                titleTextStyle: {
                    fontSize: 22,
                },
            },
	    height: 600,
	    //dateFormat: 'MMMM dd, yyyy',
	    trendlines: null,
            vAxis: {
                title: 'Temperature',
                titleTextStyle: {
                    fontSize: 22,
                }
            },
//            colors: ['#a52714', '#87b1c6', '#d18181'],
            legend: {
                textStyle: {
                    fontSize: 18,
                }
            },
            fontName: 'Share Tech Mono',
        };
	
        chart = new google.visualization.LineChart(document.getElementById('chart_div'));
        chart.draw(data, options);
    }

    document.querySelector("input#submit").addEventListener("click", function () {
	var opt_selected = document.querySelector(
	    "input[name='weather_data_srcapi']:checked").value;

	var api_url = '/weather/api/forecast/';

	console.log(opt_selected)
	if (opt_selected == "local") {
	    api_url += document.querySelector("input#indate").value;
	}

	aja()
	    .method('GET')
	    .url(api_url)
	    .timeout(2500)
	    .on('200', function(response) {
		console.log(data);
		console.log(response);
		drawLineColors(response);
	    })
	    .go();
    });
});
