let text1 = document.getElementsByClassName('text1')[0].offsetHeight;
let text2 = document.getElementsByClassName('text2')[0].offsetHeight;
let text3 = document.getElementsByClassName('text3')[0].offsetHeight;
let text4 = document.getElementsByClassName('text4')[0].offsetHeight;
let text5 = document.getElementsByClassName('text5')[0].offsetHeight;

if (text1 > 265) {
  document.getElementsByClassName('text1')[0].style.maxHeight = '265px'
  document.getElementById('button1').style.display = 'block'
}
if (text2 > 265) {
  document.getElementsByClassName('text2')[0].style.maxHeight = '265px'
  document.getElementById('button2').style.display = 'block'
}
if (text3 > 48) {
  document.getElementsByClassName('text3')[0].style.maxHeight = '48px'
  document.getElementById('button3').style.display = 'block'
}
if (text4 > 48) {
  document.getElementsByClassName('text4')[0].style.maxHeight = '48px'
  document.getElementById('button4').style.display = 'block'
}
if (text5 > 48) {
  document.getElementsByClassName('text5')[0].style.maxHeight = '48px'
  document.getElementById('button5').style.display = 'block'
}

function Expand(e, button) {
  if (button.dataset.value == 0) {
    document.getElementsByClassName(e)[0].style.maxHeight = 'none'
    button.dataset.value = "1"
    button.innerHTML = 'Свернуть'
  }else{
    document.getElementsByClassName(e)[0].style.maxHeight = '265px'
    button.dataset.value = "0"
    button.innerHTML = 'Развернуть'
  }
}

function Expand2(e, button) {
  if (button.dataset.value == 0) {
    document.getElementsByClassName(e)[0].style.maxHeight = 'none'
    button.dataset.value = "1"
    button.innerHTML = 'Свернуть'
  }else{
    document.getElementsByClassName(e)[0].style.maxHeight = '48px'
    button.dataset.value = "0"
    button.innerHTML = 'Развернуть'
  }
}
