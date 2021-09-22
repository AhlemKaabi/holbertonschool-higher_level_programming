const $ = window.$;

$(document).ready(function () {
  $('#red_header').one('click', function () {
    $('header').addClass('red');
  });
});
