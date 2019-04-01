mapboxgl.accessToken = 'pk.eyJ1IjoidWJlcmRhdGEiLCJhIjoiY2pudzRtaWloMDAzcTN2bzN1aXdxZHB5bSJ9.2bkj3IiRC8wj3jLThvDGdA';
const map = new mapboxgl.Map({
  style: 'mapbox://styles/mapbox/dark-v9',
  center: [18.0585, 59.3344],
  zoom: 15,
  pitch: 55,
  bearing: 100,
  container: 'map'
});

// The 'building' layer in the mapbox-streets vector source contains building-height
// data from OpenStreetMap.
map.on('load', () => {
  map.addLayer({
    id: '3d-buildings',
    source: 'composite',
    'source-layer': 'building',
    filter: ['==', 'extrude', 'true'],
    type: 'fill-extrusion',
    minzoom: 10,
    paint: {
      'fill-extrusion-color': '#aaa',
      'fill-extrusion-height': ['get', 'height'],
      // 'fill-extrusion-base': ['get', 'min_height'],
      'fill-extrusion-opacity': 0.2
    }
  });

  // Start to retrieve data
  features = map.queryRenderedFeatures({
    layers: ["building"],
    filter: ['==', 'extrude', 'true']
  });
  const data_buildings = []; // objective data container
  features.forEach(function (feature) {
    // console.log(feature.geometry.coordinates);  // returns coordinates of building shape points
    // console.log(feature.properties.height); // returns building height
    // console.log(feature.properties.min_height); // returns building part elevation from groung, e.g. a bridge, not applicable in Kungsgatan
    const new_data = {
      height: feature.properties.height,
      polygon: feature.geometry.coordinates,
    };
    data_buildings.push(new_data);
  });
  console.log(data_buildings);

  // Save data_buildings as json and download
  const pom = document.createElement('a');
  pom.setAttribute('href', 'data:text/json;charset=utf-8,' + encodeURIComponent(JSON.stringify(data_buildings)));
  pom.setAttribute('download', 'buildings.json');
  if (document.createEvent) {
    const event = document.createEvent('MouseEvents');
    event.initEvent('click', true, true);
    pom.dispatchEvent(event);
  } else {
    pom.click();
  }
});
