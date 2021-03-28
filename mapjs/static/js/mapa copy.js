const tilesProvider = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"

const myMap = L.map('myMap').setView([4.38, -74.09], 5)
L.tileLayer(tilesProvider,{
    maZoom:18,
}).addTo(myMap)


var circle = L.circle([4.38, -74.09], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 5000
}).addTo(myMap);

/*  */
var map = L.map('map').setView([4.38, -74.09], 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

L.marker([4.38, -74.09]).addTo(map)
    .bindPopup('A pretty CSS3 popup.<br> Easily customizable.')
    .openPopup();

/*  */

const tilesProvider1 = "https://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png"

const myMap1 = L.map('myMap1').setView([4.38, -74.09], 5)
L.tileLayer(tilesProvider1,{
    maZoom:18,
}).addTo(myMap1)

