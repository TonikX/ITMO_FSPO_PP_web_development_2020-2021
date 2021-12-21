function Button1(e) {
  let button = document.querySelectorAll('.rating_button')
  for (var i = 0; i < button.length; i++) {
    button[i].classList.remove('active')
  }
  e.classList.add('active')
}
