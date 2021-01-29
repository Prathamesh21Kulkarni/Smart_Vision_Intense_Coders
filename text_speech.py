def textToSpeech():
    import pyttsx3

    # The text that you want to convert to audio
    f1 = open("static/speech.txt", "r")
    output = f1.readline()
    f1.close()
    mytext = output

    engine = pyttsx3.init()
    engine.say(mytext)
    return engine.runAndWait()
