const $ = window.$;

$(document).ready(function () {
  $('#red_header').one('click', function () {
    $(this).css('color', '#FF0000');
  });
});
