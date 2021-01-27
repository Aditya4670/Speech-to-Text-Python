import speech_recognition as sr
import pyautogui

recogniser = sr.Recognizer()


def order():
    try:
        with sr.Microphone() as source:
            recogniser.adjust_for_ambient_noise(source, duration=1)
            print('listening...')
            voice = recogniser.listen(source)

            command = recogniser.recognize_google(voice).lower()

            print(command)
            return command
    except:
        print("Sorry, something went wrong!")


while True:
    query = order()
    if "assistant quit" in query:
        quit()
    else:
        pyautogui.typewrite(query)
