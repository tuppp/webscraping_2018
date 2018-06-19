


//initializing
//var mymap = L.map("mapid1",{dragging : false}).setView([51.1130576,10.4233481], 6.5);
var mymap = L.map("mapid1").setView([51.1130576,10.4233481], 6);
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
maxZoom: 18,
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
	'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
	'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
id: 'mapbox.light'
}).addTo(mymap);

var listOfStates = data.features;

//set temperature for debug purposes
for (var i = 0; i < listOfStates.length; i++){
	listOfStates[i].properties.temperature = Math.random() * 30;
}





//hover interaction
function highlightFeature(e) {
    var layer = e.target;
    layer.setStyle({
        weight: 3,
        color: '#000000',
        dashArray: '',
        fillOpacity: 0.7
    });

    if (!L.Browser.ie && !L.Browser.opera && !L.Browser.edge) {
        layer.bringToFront();
    }
    info.update(layer.feature.properties);
}
function resetHighlight(e) {
    geojson.resetStyle(e.target);
    info.update();
}


//add states
function SetupEvents(feature, layer) {
    layer.on({
        mouseover: highlightFeature,
        mouseout: resetHighlight,
    });
}
var geojson = L.geoJson(data, {
	style: styleForState,
	onEachFeature : SetupEvents
}).addTo(mymap);








//coloring
function getColor(d) {
    return d > 30 ? '#800026' :
           d > 25  ? '#BD0026' :
           d > 20  ? '#E31A1C' :
           d > 15  ? '#FC4E2A' :
           d > 10   ? '#FD8D3C' :
           d > 5   ? '#FEB24C' :
           d > 0   ? '#FED976' :
                      '#FFEDA0';
}

//styles postal code based on temperature using getColor()
function styleForState(feature) {
	return {
        fillColor: getColor(feature.properties.temperature),
        weight: 1,
        opacity: 1,
        color: 'white',
        dashArray: '3',
        fillOpacity: 0.7
	};
}





/*
 *
 * Graphical User Interface
 *
 */
//hover info
var info = L.control();

info.onAdd = function (map) {
    this._div = L.DomUtil.create('div', 'info'); // create a div with a class "info"
    this.update();
    return this._div;
};

// method that we will use to update the control based on feature properties passed
info.update = function (properties) {
    this._div.innerHTML = (
    	properties ? '<b>' + properties.locality + '<br> Temperatur : '+ Math.round(properties.temperature * 100) / 100  + ' °C</b>' : 'Hover over a state');
};
info.addTo(mymap);

//Legende
var legend = L.control({position: 'bottomright'});
legend.onAdd = function (map) {


  var div = L.DomUtil.create('div', 'info legend'),
      grades = [0, 5, 10, 15, 20, 25, 30],
      labels = [];
  div.innerHTML += '<h4> Temperatur Skala</h4>'    
  // loop through our density intervals and generate a label with a colored square for each interval
  for (var i = 0; i < grades.length; i++) {
      div.innerHTML +=
          '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
          grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '°C<br>' : '°C+');
  }

  var changeButton = L.DomUtil.create('button');
  $(changeButton).attr('type','button');
  changeButton.innerHTML = 'Temperatur';
  $(changeButton).click(function(){
    if (this.innerHTML == 'Temperatur'){
      this.innerHTML = 'Niederschlag';
    }
    else{
      this.innerHTML = 'Temperatur';
    }
  })

  $(div).append(changeButton);
  return div;
};
legend.addTo(mymap);

//slíder
var sliderControl = L.control({position: 'bottomleft'});

sliderControl.onAdd = function (map) {
	 var div = L.DomUtil.create('div', 'info legend');
	 $(div).attr('id', 'divuntenlinks');
	 

	 var jahresslider = $('<input/>', {
	 	type:"range",
	 	id:"jahrrangeslider",
	 	min:1940,
	 	max:2018,
	 	value:2018,
	    class: 'slider',
	    onmouseup:'updateAllStates(this.value)'
	  });

     var jahressliderText = $('<h4>', {
        class: "legend",
        id:"jahrrangesliderText",
        html:"2018",
      });
     
     
	 $(div).append(jahresslider);
     $(div).append(jahressliderText);
     

	 //disable dragging the map when sliding the slider
	 $(div).mouseover(function() {
	 	mymap.dragging.disable();
	 	mymap.doubleClickZoom.disable(); 	
	 });
	 $(div).mouseout(function() {
	 	mymap.dragging.enable();
	 	mymap.doubleClickZoom.enable();
	 });

	 return div;
}
sliderControl.addTo(mymap);



//slider functionality
function updateAllStates(time){
	
    $(jahrrangesliderText).text(time);

    //remoe old layer
	geojson.clearLayers();
	console.log("update alle states" + time);

	//set temperature for debug purposes
	for (var i = 0; i < listOfStates.length; i++){
		listOfStates[i].properties.temperature = Math.random() * 30;
	}
	//add to map
	geojson.addData(data)
	//geojson.setStyle(styleForState);

	
}

