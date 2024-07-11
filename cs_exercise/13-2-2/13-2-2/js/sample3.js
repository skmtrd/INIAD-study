// IDがtypeである要素に、イベントと座標を表示する
function printEvent(event) {
  let type = document.getElementById('type');
  let html = event.type + ' (' + event.offsetX + ',' + event.offsetY + ')<br>';
  type.innerHTML += html;
}

// IDがxおよびyである要素に、イベントの座標を表示する
function printCoordinate(event) {
  let offsetX = event.offsetX;
  let offsetY = event.offsetY;
  let x = document.getElementById('x');
  let y = document.getElementById('y');
  x.textContent = offsetX;
  y.textContent = offsetY;
}

// IDがfieldである要素に、イベントハンドラを登録する
let element = document.getElementById('field');
element.addEventListener('click', printEvent);
element.addEventListener('dblclick', printEvent);
element.addEventListener('mousedown', printEvent);
element.addEventListener('mouseup', printEvent);
element.addEventListener('mouseover', printEvent);
element.addEventListener('mouseenter', printEvent);
element.addEventListener('mouseleave', printEvent);
element.addEventListener('mousemove', printCoordinate);
