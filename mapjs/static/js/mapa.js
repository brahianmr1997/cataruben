
var tilesProvider = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"

var mapa = L.map('mapa').setView([4.38, -74.09], 5)
L.tileLayer(tilesProvider,{maZoom:18,}).addTo(mapa)

var circle = L.circle([4.38, -74.09], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 5000
}).addTo(mapa).bindPopup("I am a circle.");

var marker = L.marker([4, -72.09]).addTo(mapa).bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup()

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


