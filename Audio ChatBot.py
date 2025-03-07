import speech_recognition as sr
import pyttsx3
import os
import time

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_and_convert():
    # Use the microphone as the audio source
    with sr.Microphone() as source:
        print("Say something...")
        speak("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for the first phrase

    try:
        # Recognize speech using Google's speech recognition API
        print("Google Speech Recognition thinks you said:")
        text = recognizer.recognize_google(audio)
        print(f"Text: {text}")
        return text

    except sr.UnknownValueError:
        # Handle error if speech is unintelligible
        print("Sorry, I could not understand the audio.")
        speak("Sorry, I could not understand the audio.")
        return None

    except sr.RequestError:
        # Handle error if there's an issue with the API or network
        print("Could not request results from Google Speech Recognition service.")
        speak("Could not request results from Google Speech Recognition service.")
        return None

def save_text_to_file(text):
    if text:
        with open("recognized_text.txt", "a") as file:
            file.write(f"{time.ctime()}: {text}\n")
        print("Text saved to file.")
        speak("Text has been saved to file.")

def execute_commands(text):
    # Simple voice commands to execute actions
    if text.lower() == "open google":
        print("Opening Google...")
        speak("Opening Google...")
        os.system("start https://www.google.com")

    elif text.lower() == "play music":
        print("Playing music...")
        speak("Playing music...")
        os.system("start https://www.youtube.com/watch?v=dQw4w9WgXcQ")  # Example music link

    elif text.lower() == "tell me the time":
        current_time = time.strftime("%H:%M:%S")
        print(f"The current time is: {current_time}")
        speak(f"The current time is {current_time}")

    elif text.lower() == "exit":
        print("Exiting program...")
        speak("Goodbye!")
        exit()

# Main loop to keep listening for commands
def main():
    while True:
        # Convert speech to text
        recognized_text = listen_and_convert()
        
        if recognized_text:
            # Execute actions based on recognized text
            execute_commands(recognized_text)
            
            # Save the recognized text to a file
            save_text_to_file(recognized_text)
            
            # Provide feedback to the user
            speak(f"You said: {recognized_text}")
            
if __name__ == "__main__":
    main()
