# contents of test_player_mechanics.py
def test_player_hit():
    player = create_player()
    assert player.health == 100
    undead = create_undead()
    undead.hit(player)
    assert player.health == 80