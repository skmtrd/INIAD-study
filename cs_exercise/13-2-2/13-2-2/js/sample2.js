// Sample 2-1
// IDがsample-2-1である要素内のHTMLを表示する
function sample2_1_1() {
  let element = document.getElementById('sample-2-1');
  let content = element.innerHTML;
  console.log(content);
}

// IDがsample-2-1である要素内のテキストを表示する
function sample2_1_2() {
  let element = document.getElementById('sample-2-1');
  let text = element.textContent;
  console.log(text);
}

// Sample 2-2
// IDがsample-2-linkである要素のhref属性を表示する
function sample2_2_1() {
  let element = document.getElementById('sample-2-link');
  let attribute = element.getAttribute('href');
  console.log(attribute);
}

// IDがsample2-2である要素がsample-contentクラスを持つかを確認する
function sample2_2_2() {
  let element = document.getElementById('sample-2-2');
  let containsSampleContent = element.classList.contains('sample-content');
  console.log(containsSampleContent);
}

// Sample 2-3
// テキストボックスの値を取得する
function sample2_3_1() {
  let element = document.getElementById('textbox');
  let value = element.value;
  console.log(value);
}

// チェックボックスの状態を取得する
function sample2_3_2() {
  let element = document.getElementById('checkbox');
  let checked = element.checked;
  console.log(checked);
}

// チェックボックスが操作可能かを取得する
function sample2_3_3() {
  let element = document.getElementById('checkbox');
  let disabled = element.disabled;
  console.log(disabled);
}

// Sample 2-4
// IDがcontentである要素に、テキストエリアの内容をHTMLとして設定する
function sample2_4_1() {
  let textarea = document.getElementById('textarea');
  let content = document.getElementById('content');
  let value = textarea.value;
  content.innerHTML = value;
}

// IDがcontentである要素に、テキストエリアの内容をテキストとして設定する
function sample2_4_2() {
  let textarea = document.getElementById('textarea');
  let content = document.getElementById('content');
  let value = textarea.value;
  content.textContent = value;
}

// Sample 2-5
// IDがsample-2-imgである要素のsrc属性を設定する
function sample2_5_1() {
  let element = document.getElementById('sample-2-img');
  element.setAttribute('src', 'img/hub1.jpg');
}

// IDがsample-2-5である要素からsample-contentクラスを削除する
function sample2_5_2() {
  let element = document.getElementById('sample-2-5');
  element.classList.remove('sample-content');
}

// IDがsample-2-5である要素にsample-contentクラスを追加する
function sample2_5_3() {
  let element = document.getElementById('sample-2-5');
  element.classList.add('sample-content');
}

// Sample 2-6
// テキストボックスの値を設定する
function sample2_6_1() {
  let element = document.getElementById('textbox2');
  element.value = 'hello';
}

// チェックボックスの状態を設定する
function sample2_6_2() {
  let element = document.getElementById('checkbox2');
  element.checked = true;
}

// チェックボックスの操作の可否を設定する
function sample2_6_3() {
  let element = document.getElementById('checkbox2');
  element.disabled = true;
}