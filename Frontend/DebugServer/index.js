const express = require("express");
const path = require('path');
const app = express();

app.use(express.static(path.join(__dirname, '../')));

app.get('/', function(req, res){
    //res.send('ay');
    res.sendFile(path.join(__dirname, '../WeatherMap3.html'));
});

app.get('/map', function (req, response) {
    
    console.log("ein get für " + req.query.year);

    var returnJson = {'temp' : [], 'rain' : []};
    for (var i = 0; i < 500; i++){
        returnJson.temp.push(Math.random() * 30);
    }

    for (var i = 0; i < 500; i++){
        returnJson.rain.push(Math.random() * 1200);
    }

    
    //sleep
    for (var i = -10000; i < 1000000; i++){
        
    }
    response.json(returnJson);

})



//console.log(database);
app.listen(8080, "0.0.0.0", () => console.log('Server is listening!'))