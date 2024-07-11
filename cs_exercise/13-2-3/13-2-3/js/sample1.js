// Sample 1-1
function showDialogTimeout() {
  alert('Hello');
}

let timeoutId;
function startTimeout() {
  timeoutId = setTimeout(showDialogTimeout, 5000);
}

function stopTimeout() {
  clearTimeout(timeoutId);
}

// Sample 1-2
let cnt;
function updateContentInterval() {
  cnt++;
  let element = document.getElementById('count');
  element.textContent = String(cnt);
}

let intervalId;
function startInterval() {
  cnt = 0;
  intervalId = setInterval(updateContentInterval, 1000);
}

function stopInterval() {
  clearInterval(intervalId);
}
