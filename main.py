import pygame               # For playing the generated MP3 audio
import random               # For selecting a polite message if the text is long
import asyncio              # To run async text-to-speech operations
import edge_tts             # Microsoft Edge neural TTS engine
import os                   # For optional file operations (if needed)
from pathlib import Path    # For clean and cross-platform file paths
from dotenv import dotenv_values  # To load configuration from .env file
import pyttsx3              # Offline TTS fallback

# Load voice name from .env file
env_vars = dotenv_values(".env")
AssistantVoice = env_vars["AssistantVoice"]

# Asynchronous function to convert text to audio and save as an MP3 file
async def TextToAudioFile(text) -> None:
    file_path = Path("Data") / "speech.mp3"

    if file_path.exists():
        file_path.unlink()  # Delete existing file

    communicate = edge_tts.Communicate(text, AssistantVoice, pitch="+1Hz", rate="+3%")
    await communicate.save(str(file_path))

# Fallback offline TTS using pyttsx3
def speak_offline(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 160)
    engine.say(text)
    engine.runAndWait()

# Main TTS handler: handles playback and fallback
def TTS(Text, func=lambda r=None: True):
    while True:
        try:
            asyncio.run(TextToAudioFile(Text))  # Generate speech and save as file

            file_path = Path("Data") / "speech.mp3"
            pygame.mixer.init()
            pygame.mixer.music.load(str(file_path))
            pygame.mixer.music.play()

            while pygame.mixer.music.get_busy():
                if func() == False:
                    break
                pygame.time.Clock().tick(10)

            return True
        
        except Exception as e:
            print(f"Error in TTS: {e}") # You can Comment this error message.
            print("Switching to offline speech.")
            speak_offline(Text)
            return True

        finally:
            try:
                func(False)
                pygame.mixer.music.stop()
                pygame.mixer.quit()
            except Exception as e:
                print(f"Error in cleanup: {e}")

# High-level function to decide whether to read full or partial text
def TextToSpeech(Text, func=lambda r=None: True):
    if not Text.strip().strip(".!?"):
        print("No meaningful text provided. Please enter some valid text.")
        return

    Data = str(Text).split(".")

    responses = [
        "Please check the chat screen for more details, sir.",
        "The rest of the result is shown in the chat. Please check it, sir.",
        "You can read the remaining text in the chat, sir.",
        "The remaining answer is in the chat. Kindly take a look, sir.",
        "Sir, you can find the rest of the text in the chat screen.",
        "The other part of the text is now in the chat. Please have a look, sir.",
        "There is more to read in the chat. Kindly check it, sir.",
        "Please read the remaining text in the chat, sir.",
        "You can find more text in the chat screen, sir.",
        "Sir, please look at the chat screen to read the rest.",
        "Sir, the chat contains the rest of the message.",
        "Sir, the next part of the message is in the chat screen.",
        "You can see the full answer in the chat, sir.",
        "More text has been printed on the chat screen. Kindly check it, sir.",
        "There is more information in the chat. Please check it, sir.",
        "Please review the chat for the rest of the answer, sir.",
        "You will find the rest of the message in the chat, sir.",
        "The chat screen shows the full message, sir.",
        "Sir, the full response is now available in the chat.",
        "The complete message has been printed in the chat, sir. Please read it."
    ]


    if len(Data) > 4 and len(Text) >= 250:
        partial_text = " ".join(Text.split(".")[0:2]) + ". " + random.choice(responses)
        TTS(partial_text, func)
    else:
        TTS(Text, func)

# For testing: prompt user input in a loop
if __name__ == "__main__":
    while True:
        TextToSpeech(input("Enter the text: "))
