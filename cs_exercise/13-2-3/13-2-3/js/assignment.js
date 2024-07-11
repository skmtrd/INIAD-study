let count = 0;
let waittime = 0;

function timer() {
  count++;
  let result = document.getElementById("message");
  result.textContent = waittime - count;
}

function startNoodle() {
  let waittimeElement = document.getElementById("time");
  waittime = Number(waittimeElement.value) * 60;

  count = 0;

  let interval = setInterval(timer, 1000);
}

function stopNoodle() {}
