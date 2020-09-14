// PRELOADER
var preloader = document.getElementById('loading')

function myFunction() {
  preloader.style.display = 'none';
}

$(document).ready(function () {

  $('.first-button').on('click', function () {

    $('.animated-icon1').toggleClass('open');
  });
  $('.second-button').on('click', function () {

    $('.animated-icon2').toggleClass('open');
  });
  $('.third-button').on('click', function () {

    $('.animated-icon3').toggleClass('open');
  });
});


const date = new Date();
document.querySelector('.year').innerHTML = date.getFullYear();

setTimeout(function () {
  $('#message').fadeOut('slow');
}, 3000);

$('.datepicker').datepicker({
  max: new Date(2020, 08, 07)
})