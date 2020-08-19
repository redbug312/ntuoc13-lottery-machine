Array.prototype.sample = function(){
  return this[Math.floor(Math.random() * this.length)];
};

var CENTRAL = [24];
var SURROUNDS = [
   8,  9, 10, 11, 12,
  15, 16, 17, 18, 19,
  22, 23,     25, 26,
  29, 30, 31, 32, 33,
  36, 37, 38, 39, 40,
];
var BINGOS = [
  [ 8,  9, 10, 11, 12],
  [15, 16, 17, 18, 19],
  [29, 30, 31, 32, 33],
  [36, 37, 38, 39, 40],
  [ 8, 15, 22, 29, 36],
  [ 9, 16, 23, 30, 37],
  [11, 18, 25, 32, 39],
  [12, 19, 26, 33, 40],
];
var COLORS = [
  'rgba(62,65,92,.8)',
  'rgba(244,152,27,.8)'
];

$(document).ready(function(){

  var canvas = document.querySelector('.canvas');
  var square = document.querySelectorAll('.square');

  var central = CENTRAL.map(i => square[i]);
  var surrounds = SURROUNDS.map(i => square[i]);
  var bingo = new Set(BINGOS.sample().map(i => square[i]));

  /* burst */

  var burst = anime.timeline({
    // autoplay: false,
    easing: 'easeInOutCubic',
    begin: () => canvas.style.overflow = 'visible',
  })
  .add({  // Highlight central border-color
    targets: central,
    borderColor: () => ['rgba(100,100,100,.8)', COLORS.sample()],
    duration: 1000,
  })

  console.log(bingo);
  surrounds.forEach(item => {
    var color = COLORS.sample();
    burst
    .add({  // Highlight surrounding border-color
      targets: item,
      borderColor: () => ['rgba(100,100,100,.8)', color],
      duration: 1000,
    }, 0)
    .add({  // Highlight surrounding background-color
      targets: item,
      backgroundColor: bingo.has(item) || Math.random() < 0.6
                       ? color : 'transparent',
      delay: anime.random(0, 800),
      duration: 600,
    }, 1000)
  });

  burst
  .add({  // Rotate and scatter surrounding squares
    targets: surrounds,
    opacity: .3,
    translateX: () => anime.random(-8, 8) * 2.5 + 'rem',
    rotateZ: () => anime.random(-4, 4) * 15,
    delay: 400,
    duration: 800,
  })
  .add({  // Scale up central square
    targets: central,
    opacity: .5,
    scale: 6,
    borderWidth: [4/16 + 'rem', 1/16 + 'rem'],
    boxShadow: '0 0 0 0',
    duration: 800,
    complete: () => last.play(),
  }, '-=800')
  .add({  // Fade in winner name
    targets: 'article#bingo .winner',
    opacity: [0, 1],
    // easing: 'easeInOutCubic',
    duration: 800,
  });

  /* last */

  var last = anime.timeline({
    autoplay: false,
    loop: true,
  })
  .add({  // Keep rotating central square
    targets: central,
    keyframes: [
      {scale: 1, duration: 1},
      {scale: [6, 6], duration: 9999},
    ],
    rotateZ: 180,
    easing: 'linear',
    duration: 10000,
  });

});

// vim: set ts=2 sw=2 et:
