Array.prototype.sample = function(){
  return this[Math.floor(Math.random() * this.length)];
};

var ROWS = [
  [ 7,  8,  9, 10, 11, 12, 13],
  [14, 15, 16, 17, 18, 19, 20],
  [21, 22, 23, 24, 25, 26, 27],
  [28, 29, 30, 31, 32, 33, 34],
  [35, 36, 37, 38, 39, 40, 41],
];
var COLS = [
  [ 1,  8, 15, 22, 29, 36, 43],
  [ 2,  9, 16, 23, 30, 37, 44],
  [ 3, 10, 17, 24, 31, 38, 45],
  [ 4, 11, 18, 25, 32, 39, 46],
  [ 5, 12, 19, 26, 33, 40, 47],
];
var DIRECTIONS = [
  { lines: ROWS, x: -5, y: 0, in: 6, out: 1 },  // RIGHT
  { lines: COLS, x: 0, y: -5, in: 6, out: 1 },  // UP
  { lines: ROWS, x: +5, y: 0, in: 0, out: 5 },  // LEFT
  { lines: COLS, x: 0, y: +5, in: 0, out: 5 },  // DOWN
];


$(document).ready(function(){

  var canvas = document.querySelector('.canvas');
  var square = document.querySelectorAll('.square');

  function animation() {

    var shift = anime.timeline({
      autoplay: true,
      easing: 'easeInOutCubic',
      begin: () => canvas.style.overflow = 'hidden',
    });

    DIRECTIONS.forEach(item => {
      var line = item.lines.sample().map(i => square[i]);
      shift
      .add({
        targets: line,
        keyframes: [
          {translateX: 0, translateY: 0, duration: 0},
          {translateX: item.x + 'rem', translateY: item.y + 'rem', duration: 1000},
          {translateX: 0, translateY: 0, duration: 0},
        ],
        duration: 1000,
        endDelay: 100,
      })
      .add({
        targets: line[item.in],
        keyframes: [
          {opacity: [0, 1], duration: 600, delay: 200},
        ],
        duration: 1000,
      }, '-=1000')
      .add({
        targets: line[item.out],
        keyframes: [
          {opacity: [1, 0], duration: 600, delay: 200},
          {opacity: 1, duration: 0},
        ],
        duration: 1000,
      }, '-=1000')
    })

    shift.finished.then(animation);
  }

  animation();

});


// vim: set ts=2 sw=2 et:
