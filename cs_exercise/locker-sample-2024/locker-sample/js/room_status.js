let BASE_URL = "https://edu-iot.iniad.org/api/v1";

function displayRoomStatus(result) {
  let monitoringResult = document.getElementById("monitoring-result");
  let temperature = document.getElementById("room-temperature");
  let humidity = document.getElementById("room-humidity");
  let illuminance = document.getElementById("room-illuminance");
  let airpressure = document.getElementById("room-airpressure");
  if (result.status === "success") {
    temperature.innerHTML = result.temperature;
    humidity.innerHTML = result.humidity;
    illuminance.innerHTML = result.illuminance;
    airpressure.innerHTML = result.airpressure;
  } else {
    temperature.innerHTML = "none";
    humidity.innerHTML = "none";
    illuminance.innerHTML = "none";
    airpressure.innerHTML = "none";
  }
}

function getRoomStatus() {
  let userid = document.getElementById("iniad-id").value;
  let userpw = document.getElementById("iniad-pw").value;
  let roomNum = document.getElementById("room-number").value;
  let url = BASE_URL + "/sensors/" + roomNum;
  callRoomStatusAPI(url, "GET", userid, userpw, displayRoomStatus);
}
