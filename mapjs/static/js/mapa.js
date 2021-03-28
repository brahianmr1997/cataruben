

const tilesProvider = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"

const mapa = L.map('mapa').setView([4.38, -74.09], 5)
L.tileLayer(tilesProvider,{maZoom:18,}).addTo(mapa)