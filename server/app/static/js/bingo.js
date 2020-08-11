Array.prototype.sample = function(){
  return this[Math.floor(Math.random() * this.length)];
};
var colors = ['rgba(214, 89, 89,.8)',
              'rgba(213,168,109,.8)',
              'rgba( 74,136,154,.8)'];

$(document).ready(function() {

  var canvas = document.querySelector('.canvas');
  var grid = document.querySelectorAll('.grid');
  var centered = grid[24];
  var surround = [
    08, 09, 10, 11, 12,
    15, 16, 17, 18, 19,
    22, 23,     25, 26,
    29, 30, 31, 32, 33,
    36, 37, 38, 39, 40,
  ].map(i => grid[i]);

  /* shift */

  var left_shift = anime.timeline({
    // autoplay: false,
    easing: 'easeInOutCubic',
    loop: true,
    begin: () => canvas.style.overflow = 'hidden',
  })
  .add({  // Move the whole row
    targets: '.grid:nth-child(n+22):nth-child(-n+28)',
    translateX: -1 * (3 + 1.25) + 'rem',
    duration: 700,
  })
  .add({  // Fade in pushed grid
    targets: '.grid:nth-child(n+22):nth-child(-n+28):nth-child(7n+7)',
    opacity: [0, 1],
    duration: 500,
  }, 100)
  .add({  // Fade out poped grid
    targets: '.grid:nth-child(n+22):nth-child(-n+28):nth-child(7n+2)',
    opacity: 0,
    duration: 500,
  }, 100);

  /* burst */

  var burst = anime.timeline({
    // autoplay: false,
    easing: 'easeInOutCubic',
    begin: () => left_shift.pause(),
  })
  .add({  // Highlight border-color
    targets: [centered, surround],
    borderColor: () => ['rgba(100,100,100,.8)', colors.sample()],
    duration: 1000,
  })
  .add({  // Rotate and scatter surrounding grids
    targets: surround,
    opacity: .3,
    translateX: () => anime.random(-20, 20) + 'rem',
    rotateZ: () => anime.random(-4, 4) * 15,
    begin: () => canvas.style.overflow = 'visible',
  })
  .add({  // Scale up centered grid
    targets: centered,
    opacity: .5,
    scale: 5,
    borderWidth: [4/16 + 'rem', 4/16 / 5 + 'rem'],
    duration: 1000,
    complete: () => last.play(),
  }, 1000)
  .add({  // Fade in winner name
    targets: '.winner p',
    opacity: [0, 1],
    easing: 'easeInOutCubic',
    duration: 1000,
  });

  /* last */

  var last = anime.timeline({
    autoplay: false,
    loop: true,
  })
  .add({  // Fix scale init at 5
    targets: centered,
    scale: 1,
    duration: 0,
  })
  .add({  // Keep rotating centered grid
    targets: centered,
    scale: [5, 5],
    rotateZ: 360,
    easing: 'linear',
    duration: 10000,
  });

});

// vim: set ts=2 sw=2 et:
