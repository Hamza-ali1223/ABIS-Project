import sounddevice as sd
import wavio
import speech_recognition as sr
import os
import time


# Function -  Record audio

def record_audio(duration=5, fs=44100, filename="temp.wav"):
   # Record mic audio and return temp filename

    print("Listening...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    wavio.write(filename, recording, fs, sampwidth=2)
    return filename


# Function: Convert speech to text

def convert_speech_to_text(filename):

   # Convert audio file to text; return text or None.
    r = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return "ERROR"


# Function - Ask user if they want to save recording

def save_recording(temp_filename,choice="no"):

    # Asks the user if they want to save the recording.
    # Returns True if saved, False if discarded.
    if choice == "yes":
        # Save file with a unique timestamp
        timestamp = int(time.time())
        saved_filename = f"recording_{timestamp}.wav"
        os.rename(temp_filename, saved_filename)
        print(f"Recording saved as {saved_filename}\n")
        return True
    else:
        os.remove(temp_filename)
        print("Recording discarded\n")
        return False


# Main Voice Assistant Function

def voice_assistant(stop_word = "stop"):
    print("Voice Assistant started!\n")
    # Ask the user which word should stop the assistant
    while True:
        # Step 1: Record audio
        temp_file = record_audio()

        # Step 2: Convert audio to text
        text = convert_speech_to_text(temp_file)

        # Step 3: Handle recognition results
        if text == "ERROR":
            print("Check your internet connection.\n")
        elif text is None:
            print("Sorry, I didn’t understand.\n")
        else:
            print(f" You said: {text}\n")
            return text

            # Step 4: Check for stop word
            if stop_word in text.lower():
                print("Stop word detected. Ending assistant. Goodbye!")
                # Delete last temp recording if exists
                if os.path.exists(temp_file):
                    os.remove(temp_file)
                break

        # Step 5: Ask user if they want to save this recording
        if os.path.exists(temp_file):
            save_recording(temp_file)


# Run the assistant

if __name__ == "__main__":
    voice_assistant()
