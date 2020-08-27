$(document).ready(function(){

  var heart = document.querySelector('#trigger .heart.icon')

  trigger.onclick = () => {
    heart.classList.add('pink')
    heart.classList.remove('outline')
    // anime.set('#trigger i', {color: '#FF6FAD'})

    anime.timeline({
      autoplay: true,
    })
    .add({
      targets: '#icons',
      opacity: [1, 0],
      delay: 700,
      easing: 'easeInOutCubic',
      complete: () => anime.set('#icons', {
        display: 'none',
      })
    })
    .add({
      targets: '#winners .label',
      opacity: [0, 1],
      translateY: [30, 0],
      delay: anime.stagger(100),
      begin: () => anime.set('#winners', {
        display: 'block',
      })
    })
  }

})

// vim: set ts=2 sw=2 et:
