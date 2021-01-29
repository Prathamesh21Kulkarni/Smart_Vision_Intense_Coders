def textToSpeech():
    from gtts import gTTS
    import os

    # The text that you want to convert to audio
    f1 = open("static/speech.txt", "r")
    output = f1.readline()
    f1.close()
    mytext = output

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome.mp3")

    # Playing the converted file
    return (os.system("welcome.mp3"))
