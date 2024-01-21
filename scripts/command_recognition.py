import speech_recognition as sr
import os
import asyncio

async def recognize_command(onRecognition):
    trigger_command = os.getenv("TRIGGER_COMMAND")
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        if(text.lower() == trigger_command):
            task = asyncio.create_task(onRecognition())
            await task
        
    except sr.UnknownValueError:
        print("Could not understand audio.")
        return None
    except sr.RequestError as e:
        print(f"Google Speech Recognition request failed: {e}")
        return None

