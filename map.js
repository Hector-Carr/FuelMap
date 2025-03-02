const map = new maplibregl.Map({
        style: 'https://tiles.openfreemap.org/styles/liberty',
        center: [153, -27.4],
        zoom: 9,
        container: 'map',
    });

    const locs = [{'latlong': [153, -27.5]}, {'latlong': [153, -27.4]}]
    
locs.forEach(loc => {
        var marker = new maplibregl.Marker().setLngLat(loc['latlong']).addTo(map);
    });