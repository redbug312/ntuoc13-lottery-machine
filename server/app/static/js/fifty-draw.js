$(document).ready(function(){

  anime.set('#icons', {display: 'none'})

  var waves = anime.timeline({
    autoplay: true,
    delay: 100,
  })
  .add({
    targets: '#winners .label',
    opacity: [0, 1],
    translateY: [30, 0],
    delay: anime.stagger(100),
  })

})

// vim: set ts=2 sw=2 et:
