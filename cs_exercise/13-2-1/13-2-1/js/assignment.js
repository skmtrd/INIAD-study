// Assignment
let cnt = 0;
function plus() {
  cnt++;
  let element = document.getElementById("count");
  element.textContent = String(cnt);
}

function minus() {
  cnt--;
  let element = document.getElementById("count");
  element.textContent = String(cnt);
}
