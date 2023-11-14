def on_button_pressed_a():
    global logging
    logging = not (logging)
    if logging:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.hello),
            SoundExpressionPlayMode.UNTIL_DONE)
        basic.show_icon(IconNames.TARGET)
    else:
        basic.clear_screen()
input.on_button_pressed(Button.A, on_button_pressed_a)

logging = False
logging = False

def on_every_interval():
    if logging:
        datalogger.log(datalogger.create_cv("", input.temperature()),
            datalogger.create_cv("", input.light_level()))
loops.every_interval(60000, on_every_interval)
