import { createPopper } from '@popperjs/core';

const popcorn = document.querySelector('#popcorn');
const tooltip = document.querySelector('#tooltip');

$(function () {
  $('[data-toggle="popover"]').popover()
})

$(function () {
  $('.example-popover').popover({
    container: 'body'
  })
})

