var zebra_stripe_tables = function () {
    $('.tablerow:even').addClass('highlight');
}

//
// DOM-ready
//
$(function(){
  zebra_stripe_tables();

  $('#id_round_number')
    .change(
      function () {
        var tournament_id = $('#id_tournament').val();
        var round_number = $(this).val();
        window.location.href = '/tourney/games/' + tournament_id + '/' + round_number;
      });

  $('[id^=delete_round]')
    .click(
      function () {
        var round = $(this).attr('id').split('_').slice(2);
        if (confirm('Really delete Round ' + round + ' and all of its games?')){
          var tournament_id = $('#id_tournament').val();
          window.location.href = '/tourney/games/' + tournament_id + '/' + round + '/delete';
        }
        });

  $('input')
    .focus(
      function(){
        $(this).select();
      });

  $('.editable_battle_points')
    .click(
      function(){
        var id = $(this).attr('id');
        var game_id = id.slice(5);
        game_id = game_id.slice(0,-3);
        var player_num = id.slice(-1);
        $('[name=game_id]').val(game_id);
        $('[name=player_num]').val(player_num);
        var offset = $(this).offset();
        $.getJSON(
          '/tourney/games/' + game_id + '/player_scores/' + player_num,
          {},
          function(data, textStatus, jqXHR){
            $('#player_name').html(data.data.player_name + ' (' + data.data.player_army + ')');
            $('[name=primary_objective_points]').val(data.data.primary_objective_points);
            $('[name=secondary_objective_points]').val(data.data.secondary_objective_points);
            $('[name=tertiary_objective_points]').val(data.data.tertiary_objective_points);
            $('[name=bonus_points]').val(data.data.bonus_points);
            $('[name=penalty_points]').val(data.data.penalty_points);
            $('[name=naughty_points]').val(data.data.naughty_points);
            $('[name=nice_points]').val(data.data.nice_points);
            $('#battle_points_edit')
                .css('top', offset.top-20)
                .css('left', offset.left-200) 
                .show();
            $('[name=primary_objective_points]').focus();
          }
          );
      });

  $('#close_battle_points_edit')
    .click(
      function(){
        $('#battle_points_edit').hide();
      });

  $('#battle_points_edit_form')
    .submit(
      function(ev){
        ev.preventDefault();
        $.post(
          '/tourney/games/update',
          {game_id:$('[name=game_id]').val(),
           player_num:$('[name=player_num]').val(),
           primary_objective_points:$('[name=primary_objective_points]').val(),
           secondary_objective_points:$('[name=secondary_objective_points]').val(),
           tertiary_objective_points:$('[name=tertiary_objective_points]').val(),
           bonus_points:$('[name=bonus_points]').val(),
           penalty_points:$('[name=penalty_points]').val(),
           naughty_points:$('[name=naughty_points]').val(),
           nice_points:$('[name=nice_points]').val()},
          function(data, textStatus, jqXHR){
            $('#game_' + data.data.game_id + '_p' + data.data.player_num)
              .html(data.data.battle_points);
            $('#battle_points_edit').hide();
          }
          );
        return false;
      });

  $('input[name^=sports_]')
    .click(
      function () {
        var element = $(this);
        var id_pieces = element.attr('name').split('_');
        var player_id = id_pieces[1];
        var rated_by_id = id_pieces[2];
        var score = element.val();
        $.post(
          '/tourney/sports/' + player_id + '/' + rated_by_id + '/edit',
          {score:score}
          );
      });

  $('[id^=printable_games]')
    .click(
      function () {
        var id_pieces = $(this).attr('id').split('_');
        var tournament_id = id_pieces[2];
        var round_number = id_pieces[3];
        window.open('/tourney/games/' + tournament_id + '/' + round_number + '/printable',
                    'PrintableGames',
                    'width=600,height=600,scrollbars=yes,left=200,top=200');
      });

});
