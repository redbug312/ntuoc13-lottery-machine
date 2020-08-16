Array.prototype.sample = function(){
  return this[Math.floor(Math.random() * this.length)];
};
var colors = ['rgba(62,65,92,.8)',
              'rgba(244,152,27,.8)'];

$(document).ready(function(){

  var canvas = document.querySelector('.canvas');
  var grid = document.querySelectorAll('.grid');
  var central = grid[24];
  var surrounds = [
     8,  9, 10, 11, 12,
    15, 16, 17, 18, 19,
    22, 23,     25, 26,
    29, 30, 31, 32, 33,
    36, 37, 38, 39, 40,
  ].map(i => grid[i]);

  /* burst */

  var burst = anime.timeline({
    // autoplay: false,
    easing: 'easeInOutCubic',
    begin: () => canvas.style.overflow = 'visible',
  })
  .add({  // Highlight central border-color
    targets: central,
    borderColor: () => ['rgba(100,100,100,.8)', colors.sample()],
    duration: 1000,
  })

  surrounds.forEach(item => {
    var color = colors.sample();
    burst
    .add({  // Highlight surrounding border-color
      targets: item,
      borderColor: () => ['rgba(100,100,100,.8)', color],
      duration: 1000,
    }, 0)
    .add({  // Highlight surrounding background-color
      targets: item,
      backgroundColor: Math.random() < 0.7 ? color : 'transparent',
      delay: anime.random(200, 1000),
      duration: 1000,
    }, 1000)
  });

  burst
  .add({  // Rotate and scatter surrounding grids
    targets: surrounds,
    opacity: .3,
    translateX: () => anime.random(-8, 8) * 2.5 + 'rem',
    rotateZ: () => anime.random(-4, 4) * 15,
    delay: 500,
    duration: 1000,
  })
  .add({  // Scale up central grid
    targets: central,
    opacity: .5,
    scale: 5,
    borderWidth: [4/16 + 'rem', 2/16 + 'rem'],
    duration: 1000,
    complete: () => last.play(),
  }, '-=1000')
  .add({  // Fade in winner name
    targets: 'article#bingo .winner',
    opacity: [0, 1],
    easing: 'easeInOutCubic',
    duration: 1000,
  });

  /* last */

  var last = anime.timeline({
    autoplay: false,
    loop: true,
  })
  .add({  // Keep rotating central grid
    targets: central,
    keyframes: [
      {scale: 1, duration: 1},
      {scale: [5, 5], duration: 9999},
    ],
    rotateZ: 360,
    easing: 'linear',
    duration: 10000,
  });

});

// vim: set ts=2 sw=2 et:
