import pyttsx3

if __name__ == '__main__':
    engine = pyttsx3.init()
    print("Welcome to RoboSpeaker 0.1 Created by Krishna!!!")
    while True:
        x = input("Enter what you want me to speak")
        if x == "q":
            engine.say("bye bye friend")
            engine.runAndWait()
            
            break
        engine.say({x})
        engine.runAndWait()
    