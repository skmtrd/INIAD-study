let count = 0;
let waittime = 0;
let interval = null;
let isActive = false;

function timer() {
  if (count === waittime) {
    clearInterval(interval);
    complite();
    return;
  }
  count++;
  let result = document.getElementById("message");
  result.textContent = waittime - count;
}

function complite() {
  alert(`${waittime / 60}分経過しました`);
  isActive = false;
}

function startNoodle() {
  if (isActive) return;

  isActive = true;
  let waittimeElement = document.getElementById("time");
  waittime = Number(waittimeElement.value) * 60;

  count = 0;
  interval = setInterval(timer, 1000);
}

function stopNoodle() {
  clearInterval(interval);
  isActive = false;
  alert("中断しました");
}
