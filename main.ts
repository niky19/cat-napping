input.onButtonPressed(Button.A, function () {
    logging = !(logging)
    if (logging) {
        music.playSoundEffect(music.builtinSoundEffect(soundExpression.hello), SoundExpressionPlayMode.UntilDone)
        basic.showIcon(IconNames.Target)
    } else {
        basic.clearScreen()
    }
})
let logging = false
logging = false
loops.everyInterval(60000, function () {
    if (logging) {
        datalogger.log(
        datalogger.createCV("", input.temperature()),
        datalogger.createCV("", input.lightLevel())
        )
    }
})
