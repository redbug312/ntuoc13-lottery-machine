$(document).ready(function(){

  var trigger = document.querySelector('#timer-trigger');
  var label = document.querySelector('#timer-progress .label');
  var timespan = 5 * 60 * 1000;

  var timing = anime.timeline({
    autoplay: false,
  })
  .add({
    targets: '#timer-progress .bar',
    width: [0, '100%'],
    easing: 'linear',
    duration: timespan,
  }, 0)
  .add({
    targets: '#timer-progress .bar',
    keyframes: [
      {backgroundColor: '#2ECC40', duration: timespan * .4},
      {backgroundColor: '#EECD2F', duration: timespan * .4},
      {backgroundColor: '#FF695E', duration: timespan * .2},
    ],
    duration: timespan,
    update: (anim) => {
      var left = timespan / 1000 * (100 - anim.progress) / 100;
      var mins = Math.trunc(left / 60);
      var secs = Math.trunc(left % 60);
      label.innerHTML = '剩餘：' + mins + ' 分 ' + secs + ' 秒';
    }
  }, 0)

  trigger.onclick = () => {
    timing.pause();
    timing.restart();
  }

});

// vim: set ts=2 sw=2 et:
