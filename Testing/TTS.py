import pyttsx3

text_string = input("Enter text: ")

speaker = pyttsx3.init()

speaker.setProperty('rate',150)
speaker.setProperty('volume',0.5)
speaker.setProperty('voice.id','English')

speaker.say(text_string)
speaker.runAndWait()