let map;

function initMap() {
    const mapElement = document.getElementById('map-container');

    if (!mapElement) {
        console.error("Map container element not found!");
        return;
    }

    try {
        const mapOptions = {
            center: {lat: 40.0, lng: -74.0},
            zoom: 12,
        };
        map = new google.maps.Map(mapElement, mapOptions)
    } catch (error) {
        console.error('Error initializing map: ', error);
        mapElement.innerHTML = '<div style="color: red;">Failed to load map. Please check your connection.</div>';
    }
}


function initMenu() {
    const menu = document.getElementById('menu-container');
    if (!menu) {
        console.warn('Menu container element not found!');
        return;
    }
}

function initApp() {
    if (typeof google === 'object' && typeof google.maps === 'object') {
        initMap();
    } else {
        console.error('Google Maps API not loaded.');
        const mapElement = document.getElementById('map-container');
        if (mapElement) {
            mapElement.innerHTML = '<a href="https://www.google.com/maps" target="_blank">View on Google Maps</a>';
        }
    }
    initMenu();
}


function loadGoogleMaps() {
    const script = document.createElement('script');
    script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyCJjc11DCIklUwAvTujuc7u6GFaU_MRBus&callback=initApp';
    script.async = true;
    script.defer = true;
    document.head.appendChild(script);
}

window.onload = loadGoogleMaps;
