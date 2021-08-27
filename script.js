const mapboxApiToken = pk.eyJ1IjoiYW9zeHh4IiwiYSI6ImNrc3VmZjdrdTAydDAycHMzcWw0ZWQ4Z3cifQ.lt_PAlq_hnf4ToB70mX5VQ

const map = new mapboxgl.Map({
    container: 'map', // container ID
    center: [-122.420679, 37.772537], // starting position [lng, lat]
    zoom: 13, // starting zoom
    style: 'mapbox://styles/mapbox/streets-v11', // style URL or style object
    hash: true, // sync `center`, `zoom`, `pitch`, and `bearing` with URL
    // Use `transformRequest` to modify requests that begin with `http://myHost`.
    transformRequest: (url, resourceType) => {
        if (resourceType === 'Source' && url.startsWith('http://myHost')) {
            return {
                url: url.replace('http', 'https'),
                headers: {'my-custom-header': true},
                credentials: 'include'  // Include cookies for cross-origin requests
            };
        }
    }
});
