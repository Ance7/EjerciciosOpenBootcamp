let map, markers

function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 8,
    })

    markers.push(
        new google.map.Marker({
            position: {
                lat: 48.858550319440546,
                lng: 2.294535050175646,
            },
            map,
            title: "Torre Eiffel",
        })
    )
    markers.push(
        new google.map.Marker({
            position: {
                lat: 29.979639128529616,
                lng: 31.13395420150334,
            },
            map,
            title: "Piramides de Giza",
        })
    )
    markers.push(
        new google.map.Marker({
            position: {
                lat: -22.94493064792068,
                lng: -43.21131124170299,
            },
            map,
            title: "Cristo Redentor",
        })
    )
}

window.initMap = initMap