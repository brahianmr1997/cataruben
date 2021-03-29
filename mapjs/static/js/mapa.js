
var tilesProvider = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"

var mapa = L.map('mapa').setView([4.38, -74.09], 5)
L.tileLayer(tilesProvider,{maZoom:18,}).addTo(mapa)




var cali = L.marker([3.45, -76.533])
            .addTo(mapa)
            .bindPopup("<h1>Cali</h1><p>Capital valle del cauca</p> <img src='http://www.institutocanzion.com.co/wp-content/uploads/2019/02/CALI.jpg' width='180' height='75'> ")
            .openPopup()


L.geoJSON(colombia, {
    color: 'purple',
}).addTo(mapa);


var circle = L.circle([4.38, -74.09], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 50000
}).addTo(mapa).bindPopup("I am a circle.");

var marker = L.marker([4, -69.09]).addTo(mapa).bindPopup("<b>Hola colombia</b><br>Comentario de brahian munar")

var polygon = L.polygon([
    [4 , -72],
    [4.3, -71],
    [4.5, -73]
]).addTo(mapa).bindPopup("I am a polygon.");


var popup = L.popup();

function onMapClick(e) {
    popup
        .setLatLng(e.latlng)
        .setContent("You clicked the map at " + e.latlng.toString())
        .openOn(mapa);
}

mapa.on('click', onMapClick);


