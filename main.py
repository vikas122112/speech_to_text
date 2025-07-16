import speech_recognition as sr

def transcribe_audio_file(audio_file_path):
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file_path) as source:
            print("🔊 Reading audio file...")
            audio_data = recognizer.record(source)
            print("🧠 Transcribing...")
            text = recognizer.recognize_google(audio_data, language='en-IN')  # or 'en-US'
            print("✅ Transcription successful:")
            print(text)
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ API error: {e}")

def transcribe_live_microphone():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎙️ Speak something... (say something clearly)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🧠 Transcribing...")
        text = recognizer.recognize_google(audio, language='en-IN')
        print("✅ You said:")
        print(text)
    except sr.UnknownValueError:
        print("❌ Could not understand your voice.")
    except sr.RequestError as e:
        print(f"❌ API error: {e}")

# Choose one of the following options:
# For audio file transcription:
# transcribe_audio_file("audio.wav")

# For live microphone transcription:
transcribe_live_microphone()
