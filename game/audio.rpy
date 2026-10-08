# All audio is optional. Missing files produce silence, never a missing-file error.
init python:
    renpy.music.register_channel('ambience', mixer='sfx', loop=True)
    AUDIO = dict(menu='audio/menu.ogg', daily='audio/daily.ogg', evening='audio/evening.ogg', campus='audio/campus.ogg', button='audio/button.ogg')
    def play_optional(key, channel='music', fadein=1.0):
        path = AUDIO[key]
        if renpy.loadable(path):
            renpy.music.play(path, channel=channel, fadein=fadein)
        else:
            renpy.music.stop(channel=channel, fadeout=.5)
    config.main_menu_music = AUDIO['menu'] if renpy.loadable(AUDIO['menu']) else None
    def stop_campus_audio():
        renpy.music.stop(channel='ambience')


label before_main_menu:
    $ stop_campus_audio()
    return
