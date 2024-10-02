import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initializing recognizer and text-to-speech engine
listener = sr.Recognizer()
machine = pyttsx3.init()

def talk(text):
    machine.say(text)
    machine.runAndWait()

def input_instruction():
    global instruction

    try:
        with sr.Microphone() as source:
            print("Listening...")
            speech = listener.listen(source)
            instruction = listener.recognize_google(speech)
            instruction = instruction.lower()
            if "jarvis" in instruction:
                instruction = instruction.replace('jarvis', "")
                print(instruction)
    except Exception as e:
        print(f"Error: {e}")
        return ""
    return instruction

def play_jarvis():
    while True:
        instruction = input_instruction()
        if not instruction:
            continue
        print(instruction)

        if "play" in instruction:
            song = instruction.replace('play', "")
            talk("Playing " + song)
            pywhatkit.playonyt(song)

        elif 'time' in instruction:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
            print(time)

        elif 'date' in instruction:
            date = datetime.datetime.now().strftime('%d/%m/%Y')
            talk("Today's date is " + date)
            print(date)

        elif 'how are you' in instruction:
            talk('I am fine, how about you?')

        elif 'what is your name' in instruction:
            talk('I am Jarvis, what can I do for you?')

        elif 'who is' in instruction:
            human = instruction.replace('who is', "").strip()
            info = wikipedia.summary(human, 1)
            print(info)
            talk(info)

        else:
            talk('Please repeat.')

# Running the assistant
play_jarvis()
   
         
      
       
     
     