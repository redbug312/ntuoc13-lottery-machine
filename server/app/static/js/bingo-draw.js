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


$(document).ready(function(){

  var canvas = document.querySelector('#canvas');
  var winner = document.querySelector('#winner');
  var cubes = document.querySelectorAll('#canvas .cube');

  var origin_color = anime.get(cubes[0], 'border-top-color');
  var colors = [
    anime.get(document.querySelector('#canvas .cube.color1'), 'border-top-color'),
    anime.get(document.querySelector('#canvas .cube.color2'), 'border-top-color'),
  ];

  var central = CENTRAL.map(i => cubes[i]);
  var surrounds = SURROUNDS.map(i => cubes[i]);
  var bingo = new Set(BINGOS.sample().map(i => cubes[i]));

  /* saturate */

  var saturate = anime.timeline({
    // autoplay: false,
    easing: 'easeInOutCubic',
    // complete: () => burst.play(),  // lazy evaluate
  })
  .add({  // Highlight central border-color
    targets: central,
    borderColor: () => [origin_color, colors.sample()],
    duration: 1000,
  })

  surrounds.forEach(item => {
    var color = colors.sample();
    saturate
    .add({  // Highlight surrounding border-color
      targets: item,
      borderColor: () => [origin_color, color],
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

  /* burst */

  var burst = anime.timeline({
    autoplay: false,
    easing: 'easeInOutCubic',
  })
  .add({  // Rotate and scatter surrounding cubes
    targets: surrounds,
    opacity: .3,
    translateX: () => anime.random(-8, 8) * 2.5 + 'rem',
    rotateZ: () => anime.random(-4, 4) * 15,
    delay: 400,
    duration: 800,
  })
  .add({  // Scale up central cube
    targets: central,
    opacity: .5,
    scale: 6,
    borderWidth: [4/16 + 'rem', 1/16 + 'rem'],
    boxShadow: '0 0 0 0',
    duration: 800,
    complete: () => rotate.play(),
  }, '-=800')
  .add({  // Fade in winner name
    targets: winner,
    opacity: [0, 1],
    duration: 800,
  });

  // Avoid trigger complete() in reverse animation
  saturate.finished.then(burst.play);

  /* rotate */

  var rotate = anime({
    autoplay: false,
    loop: true,
    targets: central,
    keyframes: [
      {scale: 1, duration: 1},
      {scale: [6, 6], duration: 9999},
    ],
    rotateZ: 180,
    easing: 'linear',
    duration: 10000,
  });

  /* rectify */

  cubes[24].onclick = () => {
    var degree = anime.get(central[0], 'rotateZ', 'deg');
    degree = parseInt(degree, 10);

    var rectify = anime({
      targets: central,
      rotateZ: [degree, degree - degree % 90],
      duration: 400 * (degree % 90) / 90,
      easing: 'easeInCubic',
      begin: () => rotate.pause(),
    });

    rectify.finished.then(() => {
      burst.reverse();
      burst.play();
      return burst.finished;
    }).then(() => {
      saturate.children.forEach(sub => {
        sub.delay = 0;
        sub.reverse();
        sub.play();
      });
      return saturate.children[0].finished;
    }).then(() => {
      var next_url = canvas.getAttribute('data-nexturl');
      window.location.href = next_url;
    });
  }

});

// vim: set ts=2 sw=2 et:
