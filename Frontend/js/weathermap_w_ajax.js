/*
 * Map displaying average Temperature and Rainfall througout the years!
 * Using Leaflet.js
 * authors: Alexander Franz
 *  	   Daniel Hartung
 */


//global variable to indicate what is being shown
modus = "Temperatur";

//in anther js file an varibale called data holds all the geojson data necessary to display the states and their corresponding borders
var listOfStates = data.features;


//initializingmap
//var mymap = L.map("mapid1",{dragging : false}).setView([51.1130576,10.4233481], 6.5);
var mymap = L.map("mapid1").setView([51.1130576,10.4233481], 6);
L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
maxZoom: 18,
attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
	'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
	'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
id: 'mapbox.light'
}).addTo(mymap);


/*
does ajax call to server which connects to a database and does some caculations
*/
function getDataforYear(year){

	//remoe old layer
	geojson.clearLayers();	

	console.log("update " + modus + " für alle states für das jahr" + year);

	if (modus == 'Temperatur'){
		var query = '?year=' + year;
		$.get('http://127.0.0.1:8000/avgtemp' + query, function(jsondata){
			for (var i = 0; i < listOfStates.length; i++){
				listOfStates[i].properties.temperature = jsondata[i];
			}
			//add new data to map
			geojson.addData(data)
		},'json');

	} 
	else if (modus == 'Niederschlag'){
		var query = '?year=' + year;
		$.get('http://127.0.0.1:8000/avgrain' + query, function(jsondata){
		
			for (var i = 0; i < listOfStates.length; i++){
			  listOfStates[i].properties.rainfall = jsondata[i];
			}
			//add new data to map
			geojson.addData(data)
		},'json');
	}
	else{
		console.log('fehler globale variable temp');
	}
	
	//geojson.setStyle(styleForState);
	
}

//add states to map
//
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








//coloring for states in map
function getColor(d) {

  if (modus == "Temperatur"){
    return d > 30 ? '#800026' :
           d > 25  ? '#BD0026' :
           d > 20  ? '#E31A1C' :
           d > 15  ? '#FC4E2A' :
           d > 10   ? '#FD8D3C' :
           d > 5   ? '#FEB24C' :
           d > 0   ? '#FED976' :
                      '#FFEDA0';
  }
  else if (modus == "Niederschlag"){
    return  d < 200 ? '#f1eef6' :
            d < 400 ? '#ece7f2' : 
            d < 600 ? '#d0d1e6' :
            d < 800 ? '#a6bddb' :
            d <1000 ? '#3690c0' :
            d <1200 ? '#0570b0' :
                      '#034e7b' ; 
  }
}

//styles postal code based on temperature using getColor()
function styleForState(feature) {
	return {
        fillColor: modus == "Temperatur" ? getColor(feature.properties.temperature) : getColor(feature.properties.rainfall),
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
    this._div.style.background= (modus == 'Temperatur') ? 'linear-gradient( rgba(255, 237, 160, 0.2) , rgba(128, 0, 38, 0.2))' : 'linear-gradient( rgba(241, 238, 246, 0.2), rgba(3, 78, 123, 0.2))';
    

    return this._div;
};

// method that we will use to update the control based on feature properties passed
info.update = function (properties) {
  if (modus == "Temperatur"){
    this._div.innerHTML = (
    	properties ? '<b>' + properties.locality + '<br> Temperatur : '+ Math.round(properties.temperature * 100) / 100  + ' °C</b>' : 'Hover over a state');
  }
  else if (modus == "Niederschlag"){
    this._div.innerHTML = (
      properties ? '<b>' + properties.locality + '<br> Niederschlag : '+ Math.round(properties.rainfall * 100) / 100  + ' mm</b>' : 'Hover over a state');
  
  }
  else{
    console.log("fehler bei globaler variable modus");
  }

};
info.addTo(mymap);

//Legende
var legend = L.control({position: 'bottomright'});
legend.onAdd = function (map) {

//TODO noch niederschlag dazu
  var div = L.DomUtil.create('div', 'info legend'),
      grades = [0, 5, 10, 15, 20, 25, 30];
  div.style.background= (modus == 'Temperatur') ? 'linear-gradient( rgba(255, 237, 160, 0.2) , rgba(128, 0, 38, 0.2))' : 'linear-gradient( rgba(241, 238, 246, 0.2), rgba(3, 78, 123, 0.2))';

  $(div).attr('id', 'legendenSkala');
  div.innerHTML += '<h4> Temperatur Skala</h4>'    
  // loop through our density intervals and generate a label with a colored square for each interval
  for (var i = 0; i < grades.length; i++) {
      div.innerHTML +=
          '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
          grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '°C<br>' : '°C+<br>');
  }
  
  addModusButton(div);

  
  return div;
};
legend.addTo(mymap);

//slíder
var sliderControl = L.control({position: 'bottomleft'});

sliderControl.onAdd = function (map) {
	 var div = L.DomUtil.create('div', 'info legend');
	 $(div).attr('id', 'divuntenlinks');
	 div.style.background= (modus == 'Temperatur') ? 'linear-gradient( rgba(255, 237, 160, 0.2) , rgba(128, 0, 38, 0.2))' : 'linear-gradient( rgba(241, 238, 246, 0.2), rgba(3, 78, 123, 0.2))';
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
	
  if (typeof time === "undefined" ){
    console.log("update all states with undefined");
    return 0;
  }
  //update text next to slider
  $(jahrrangesliderText).text(time);

  getDataforYear(time);

	
}


function updateLegende(){

  //reset old inner html 
  $('#legendenSkala').innerHTML ="";
  var div = document.getElementById('legendenSkala');
  div.innerHTML = "";

  //and replace with new 
  if (modus == "Temperatur"){

    grades = [0, 5, 10, 15, 20, 25, 30];
    div.innerHTML += '<h4> Temperatur Skala</h4>'    
    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '°C<br>' : '°C+<br>');
    }
  
  }
  else if (modus == "Niederschlag"){
    grades = [0, 200, 400, 600, 800, 1000, 1200];
    div.innerHTML += '<h4> Niederschlag Skala</h4>'    
    // loop through our density intervals and generate a label with a colored square for each interval
    for (var i = 0; i < grades.length; i++) {
        div.innerHTML +=
            '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
            grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + ' mm<br>' : 'mm+<br>');
    }
  
  }
  else{
     console.log("fehler globale variable");
  }


  //add button again
  addModusButton(div);
}




function addModusButton(div){
  //button to switch between temperatur and niederschlag
  var changeButton = L.DomUtil.create('button');
  $(changeButton).attr('type','button');
  //changeButton.innerHTML = "modus";

  changeButton.innerText = (modus == 'Temperatur') ? 'Temperatur' : 'Niederschlag';
  changeButton.style.background= (modus == 'Temperatur') ? 'rgba(128, 0, 38, 0.5)' : 'rgba(3, 78, 123, 0.5)';
  changeButton.style.color= 'white';

  $(changeButton).click(function(){
    if (modus == "Temperatur"){
      //$('#divuntenlinks').css('background-color','#99ccff');
      //$('.legend, .info').css('background-color','#99ccff');
      $('.legend, .info').css('background','linear-gradient( rgba(241, 238, 246, 0.2), rgba(3, 78, 123, 0.2))');
      modus = "Niederschlag";
      
      //$(this).css('color','#99ccff');
    }
    else  if(modus = "Niederschlag"){
      modus = "Temperatur";
      //$('.legend, .info').css('background-color','#ffd1b3');
      $('.legend, .info').css('background','linear-gradient( rgba(255, 237, 160, 0.2) , rgba(128, 0, 38, 0.2))');
      //$(this).css('color','#ffd1b3');
      //$('#divuntenlinks').css('background-color',' #ffd1b3');
    }
    else{
      console.log("error globale variable");
    }
   
    updateAllStates($('#jahrrangeslider').attr('value'));
    updateLegende();
  })

  //disable dragging or zooming the map while over GUI
   $(div).mouseover(function() {
    mymap.dragging.disable();
    mymap.doubleClickZoom.disable();  
   });
   $(div).mouseout(function() {
    mymap.dragging.enable();
    mymap.doubleClickZoom.enable();
   });

  $(div).append(changeButton);

}

//map hover interaction
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





getDataforYear(2018);