let API_KEY_GOOGLE = 'AIzaSyAYSeZRkkIEUkvEc1Ut7UYs7q0lLRZds94';
let API_KEY_WEATHER = '581bf30f05a38e311380d9fa83776630';

// Sample 1
function displayCoordinate(result) {
  if (result == null) {
    return;
  }
  let location = result.results[0].geometry.location;
  let lat = document.getElementById('lat');
  let lon = document.getElementById('lon');
  lat.textContent = location.lat;
  lon.textContent = location.lng;
}

function apiError(error) {
  console.log('ERROR: ' + error);
}

function getCoordinate() {
  let inputAddress = document.getElementById('input-address');
  let address = inputAddress.value;

  fetch('https://maps.googleapis.com/maps/api/geocode/json?address=' + encodeURI(address) + '&key=' + API_KEY_GOOGLE)
  .then(response => response.json())
  .then(displayCoordinate)
  .catch(apiError);
}

// Sample 2
function getWeather() {
  let inputLatitude = document.getElementById('input-lat');
  let inputLongitude = document.getElementById('input-lon');
  let lat = inputLatitude.value;
  let lon = inputLongitude.value;

  fetch('http://api.openweathermap.org/data/2.5/weather?lat=' + lat + '&lon=' + lon + '&appid=' + API_KEY_WEATHER)
  .then(response => response.json())
  .then(function(json) {
    let city = document.getElementById('city');
    let weather = document.getElementById('weather');
    let temperature = document.getElementById('temperature');
    let humidity = document.getElementById('humidity');
    let pressure = document.getElementById('pressure');
  
    city.textContent = json.name;
    weather.textContent = json.weather[0].main;
    temperature.textContent = json.main.temp;
    humidity.textContent = json.main.humidity;
    pressure.textContent = json.main.pressure;
  })
  .catch(function(error) {
    console.log('ERROR: ' + error);
  });
}

// Sample 3
let map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 35.7804643, lng: 139.7151025 },
    zoom: 15
  });
}

function setMapCenter() {
  let inputLatitude2 = document.getElementById('input-lat2');
  let inputLongitude2 = document.getElementById('input-lon2');
  map.setCenter({ lat: Number(inputLatitude2.value), lng: Number(inputLongitude2.value) });
}
