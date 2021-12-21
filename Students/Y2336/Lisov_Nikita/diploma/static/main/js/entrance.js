let registr_count = 0
let enter_count = 0
function Registration() {
  if (registr_count === 0) {
    document.getElementById('entrance').style.display = 'block'
    document.getElementById('enter').style.display = 'none'
    document.getElementById('registration').style.display = 'block'
    enter_count = 0
    registr_count ++
  }else{
    document.getElementById('entrance').style.display = 'none'
    document.getElementById('registration').style.display = 'none'
    registr_count = 0
  }

}
function Enter() {
  if (enter_count === 0) {
    document.getElementById('entrance').style.display = 'block'
    document.getElementById('registration').style.display = 'none'
    document.getElementById('enter').style.display = 'block'
    enter_count ++
    registr_count = 0
  }else{
    document.getElementById('entrance').style.display = 'none'
    document.getElementById('enter').style.display = 'none'
    enter_count = 0
  }

}
