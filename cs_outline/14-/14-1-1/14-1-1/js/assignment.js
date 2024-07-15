let API_KEY_GOOGLE = "AIzaSyAYSeZRkkIEUkvEc1Ut7UYs7q0lLRZds94";
let API_KEY_WEATHER = "581bf30f05a38e311380d9fa83776630";

function apiError(error) {
  console.log("ERROR: " + error);
}

let map;
function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 35.7804643, lng: 139.7151025 },
    zoom: 15,
  });
}

function findWeather() {
  let inputAddress = document.getElementById("input-address").value;
  fetch(
    "https://maps.googleapis.com/maps/api/geocode/json?address=" +
      encodeURI(inputAddress) +
      "&key=" +
      API_KEY_GOOGLE
  )
    .then((response) => response.json())
    .then((result) => displayCoordinate(result))
    .catch(apiError);
}

function displayCoordinate(result) {
  console.log(result);
  let lat = result.results[0].geometry.location.lat;
  let lon = result.results[0].geometry.location.lng;
  let address = result.results[0].address_components[0].long_name;

  document.getElementById("city").textContent = address;
  document.getElementById("latitude").textContent = lat;
  document.getElementById("longitude").textContent = lon;

  map.setCenter({ lat: Number(lat), lng: Number(lon) });

  displayWeather(lat, lon);
}

function displayWeather(lat, lon) {
  fetch(
    "http://api.openweathermap.org/data/2.5/weather?lat=" +
      lat +
      "&lon=" +
      lon +
      "&appid=" +
      API_KEY_WEATHER
  )
    .then((response) => response.json())
    .then(function (json) {
      let city = document.getElementById("city");
      let weather = document.getElementById("td-weather");
      let temperature = document.getElementById("td-temperature");
      let humidity = document.getElementById("td-humidity");
      let pressure = document.getElementById("td-pressure");

      city.textContent = json.name;
      weather.textContent = json.weather[0].main;
      temperature.textContent = json.main.temp - 273.15;
      humidity.textContent = json.main.humidity;
      pressure.textContent = json.main.pressure;
    })
    .catch(function (error) {
      console.log("ERROR: " + error);
    });
}
