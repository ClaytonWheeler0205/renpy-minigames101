define e = Character("Eileen")

label start:
    scene bg room
    e "Let's play a rhythm game!"

    # 0.75 for easy
    # 1.0 for medium
    # 2.0 for hard
    default game_difficulty = 1.0

    menu difficulty_selector:
        e "Please Select your difficulty!"
        "Easy":
            $ game_difficulty = 0.75
        "Medium":
            $ game_difficulty = 1.0
        "Hard":
            $ game_difficulty = 2.0     

    # start the rhythm game
    # window hide
    $ quick_menu = False

    # avoid rolling back and losing game state
    $ renpy.block_rollback()
    
    call screen rhythm_game(
        'audio/my-music.ogg',
        'audio/my-music.beatmap.txt',
        game_difficulty
    )

    # avoid rolling back and entering the game again
    $ renpy.block_rollback()

    # restore rollback from this point on
    $ renpy.checkpoint()

    $ quick_menu = True
    window show

    $ num_hits, num_notes = _return
    e "You hit [num_hits] notes out of [num_notes]. Good work!"

    return
