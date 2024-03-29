from django.conf.urls.defaults import *

urlpatterns = patterns(
    'tourney.views',

    (r'^tournament/(?P<tournament_id>\d+)$', 'tournament'),
    (r'^tournament/update$', 'tournament_update'),
    (r'^tournament/(?P<tournament_id>\d+)/notes/?$', 'tournament_notes'),
    (r'^tournament/(?P<tournament_id>\d+)/notes/new/?$', 'create_tournament_note'),

    (r'^players/?$', 'players'),
    (r'^players/(?P<tournament_id>\d+)$', 'players_list'),
    (r'^players/(?P<tournament_id>\d+)/(?P<player_id>\d+)$', 'player_edit'),
    (r'^players/(?P<tournament_id>\d+)/(?P<player_id>\d+)/add_to_tournament$', 'player_add_to_tournament'),
    (r'^players/(?P<tournament_id>\d+)/(?P<tplayer_id>\d+)/remove_from_tournament$', 'player_remove_from_tournament'),
    (r'^players/(?P<tournament_id>\d+)/(?P<tplayer_id>\d+)/toggle_active$', 'player_toggle_active'),
    (r'^players/(?P<tournament_id>\d+)/(?P<tplayer_id>\d+)/toggle_ringer$', 'player_toggle_ringer'),
    (r'^players/(?P<tournament_id>\d+)/(?P<tplayer_id>\d+)/army_list$', 'player_army_list'),
    (r'^player/update$', 'player_update'),
    (r'^players/(?P<tournament_id>\d+)/(?P<player_id>\d+)/notes$', 'player_notes'),
    (r'^players/(?P<tournament_id>\d+)/(?P<player_id>\d+)/notes/new/?$', 'create_player_note'),

    (r'^armylist/update$', 'army_list_update'),
    (r'^armylist/create_unit$', 'army_list_create_unit'),
    (r'^armylist/units/delete/(?P<unit_id>\d+)$', 'army_list_delete_unit'),
    (r'^armylist/(?P<list_id>\d+)/printable', 'armylist_printable'),

    (r'^games/?$', 'games'),
    (r'^games/update', 'game_update'),
    (r'^games/(?P<game_id>\d+)/player_scores/(?P<player_num>\d+)$', 'fetch_player_game_scores'),
    (r'^games/(?P<tournament_id>\d+)/(?P<round_number>\d+)$', 'games_list'),
    (r'^games/(?P<tournament_id>\d+)/(?P<round_number>\d+)/pairings$', 'games_pairings'),
    (r'^games/(?P<tournament_id>\d+)/(?P<round_number>\d+)/pairings/update', 'games_pairings_update'),
    (r'^games/(?P<tournament_id>\d+)/(?P<round_number>\d+)/delete$', 'games_delete_round'),
    (r'^games/(?P<tournament_id>\d+)/new_round', 'games_new_round'),
    (r'^games/(?P<tournament_id>\d+)/(?P<round_number>\d+)/printable', 'games_printable'),
    (r'^games/(?P<tournament_id>\d+)/(?P<game_id>\d+)/notes$', 'game_notes'),
    (r'^games/(?P<tournament_id>\d+)/(?P<game_id>\d+)/notes/new/?$', 'create_game_note'),

    (r'^standings/?$', 'standings'),
    (r'^standings/(?P<tournament_id>\d+)/(?P<round_number>\d+)$', 'standings_list'),
    (r'^standings/(?P<tournament_id>\d+)/(?P<round_number>\d+)/printable', 'standings_printable'),

    (r'^appearance/?$', 'appearance'),
    (r'^appearance/(?P<tournament_id>\d+)/?$', 'appearance_list'),
    (r'^appearance/(?P<tournament_id>\d+)/printable', 'appearance_printable'),
    (r'^appearance/(?P<tournament_id>\d+)/(?P<tplayer_id>\d+)/?$', 'appearance_edit'),
    (r'^appearance/update$', 'appearance_update'),
    (r'^appearance/(?P<tournament_id>\d+)/(?P<tplayer_id>\d+)/notes/?$', 'appearance_notes'),
    (r'^appearance/(?P<tournament_id>\d+)/(?P<tplayer_id>\d+)/notes/new/?$', 'create_appearance_note'),

    (r'^sports/?$', 'sportsmanship'),
    (r'^sports/update', 'sportsmanship_update'),
    (r'^sports/(?P<tournament_id>\d+)/?$', 'sportsmanship_list'),
    (r'^sports/(?P<tournament_id>\d+)/printable/?$', 'sportsmanship_printable'),
    (r'^sports/(?P<player_id>\d+)/(?P<rated_by_id>\d+)/edit/?$', 'sportsmanship_edit_base'),
    (r'^sports/(?P<tournament_id>\d+)/(?P<tplayer_id>\d+)/discretionary/?$', 'sportsmanship_edit_discretionary'),
    (r'^sports/(?P<tournament_id>\d+)/(?P<tplayer_id>\d+)/blackmarks/?$', 'sportsmanship_edit_blackmarks'),
    (r'^sports/blackmarks/new/?$', 'sportsmanship_new_blackmark'),
    (r'sports/blackmarks/update/?$', 'sportsmanship_update_blackmark'),
    (r'sports/blackmarks/delete/(?P<id>\d+)/?$', 'sportsmanship_delete_blackmark'),
    (r'^sports/discretionary/update/?$', 'sportsmanship_update_discretionary'),
    (r'^sports/(?P<tournament_id>\d+)/(?P<tplayer_id>\d+)/notes/?$', 'sportsmanship_notes'),
    (r'^sports/(?P<tournament_id>\d+)/(?P<tplayer_id>\d+)/notes/new/?$', 'create_sportsmanship_note'),

    (r'^overall/?$', 'overall'),
    (r'^overall/(?P<tournament_id>\d+)/?$', 'overall_list'),
    (r'^overall/(?P<tournament_id>\d+)/printable/?$', 'overall_printable'),

    (r'^note/update/note', 'note_update_note'),
    (r'^note/update/effective_date', 'note_update_effective_date'),
    (r'^note/delete/(?P<id>\d+)$', 'note_delete'),
)
