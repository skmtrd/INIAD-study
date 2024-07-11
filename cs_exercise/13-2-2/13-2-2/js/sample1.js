// Sample 1-1
// IDがsample-1である要素を検索する
function sample1_1() {
  let element = document.getElementById('sample-1');
  let text = element.textContent;
  console.log(text);
}

// Sample 1-2
// h2要素を検索する
function sample1_2_1() {
  let elements = document.getElementsByTagName('h2');
  for(let i = 0; i < elements.length; i++) {
    let element = elements[i];
    let text = element.textContent;
    console.log(text);
  }
}

// IDがsample-1-2の要素に含まれる、h2要素を検索する
function sample1_2_2() {
  let element = document.getElementById('sample-1-2');
  let elements = element.getElementsByTagName('h2');
  for(let i = 0; i < elements.length; i++) {
    let element = elements[i];
    let text = element.textContent;
    console.log(text);
  }
}

// Sample 1-3
// クラスがsample-descriptionの要素を検索する
function sample1_3_1() {
  let elements = document.getElementsByClassName('sample-description');
  for(let i = 0; i < elements.length; i++) {
    let element = elements[i];
    let text = element.textContent;
    console.log(text);
  }
}

// IDがsample-1-3の要素に含まれる、クラスがsample-descriptionの要素を検索する
function sample1_3_2() {
  let element = document.getElementById('sample-1-3');
  let elements = element.getElementsByClassName('sample-description');
  for(let i = 0; i < elements.length; i++) {
    let element = elements[i];
    let text = element.textContent;
    console.log(text);
  }
}

// Sample 1-4
// "#sample-1-4 h2"にマッチする要素を検索する
function sample1_4_1() {
  let elements = document.querySelectorAll('#sample-1-4 h2');
  for(let i = 0; i < elements.length; i++) {
    let element = elements[i];
    let text = element.textContent;
    console.log(text);
  }
}

// IDがsample-1-4の要素に含まれる、".sample-description"にマッチする要素を検索する
function sample1_4_2() {
  let element = document.getElementById('sample-1-4');
  let elements = element.querySelectorAll('.sample-description');
  for(let i = 0; i < elements.length; i++) {
    let element = elements[i];
    let text = element.textContent;
    console.log(text);
  }
}