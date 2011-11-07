// DOM-ready
$(function(){
  $('#cancel_button')
    .click(
      function () {
        var tournament_id = $('#tournament_id').val();
        window.location.href = '/tourney/sports/' + tournament_id;
      });
});
