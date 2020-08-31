$(document).ready(function(){

  anime.set('#winners', {display: 'none'})

  var fadeout = anime.timeline({
    autoplay: false,
    delay: 100,
  })
  .add({
    targets: '#icons',
    opacity: [1, 0],
    delay: 700,
    easing: 'easeInOutCubic',
  })

  fadeout.finished.then(() => {
    var next_url = icons.getAttribute('data-nexturl')
    console.log(next_url)
    window.location.href = next_url
  })

  trigger.onclick = () => {
    var heart = document.querySelector('#trigger .heart.icon')
    heart.classList.add('pink')
    heart.classList.remove('outline')
    fadeout.play()
  }

})

// vim: set ts=2 sw=2 et:
