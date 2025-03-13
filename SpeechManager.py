import os
from google.cloud import texttospeech
from google.cloud import speech
import speech_recognition as sr
from PlaySound import playSound
import pyttsx3


def speechSaying(text):
    engine = pyttsx3.init()

    engine.setProperty('rate', 200)

    voiceId = 'HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_PL-PL_Paulina_11.0'
    engine.setProperty('voice', voiceId)

    engine.say(text)

    engine.runAndWait()


def speechRecognition():
    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 400

    while True:
        try:
            with sr.Microphone(sample_rate=16000) as mic:
                print("Listening")
                recognizer.adjust_for_ambient_noise(mic)
                audio = recognizer.listen(mic)

                text = recognizer.recognize_google(audio, language="pl-PL")
                return text.lower()

        except sr.UnknownValueError:
            print("Nie zrozumiałem")
        except sr.RequestError as e:
            print("Błąd połączenia z serwerem rozpoznawania mowy:", e)
            break


def speechRecognition_google_cloud(): #to swapp if need better
    recognizer = sr.Recognizer()

    recognizer.energy_threshold = 400

    while True:
        try:
            with sr.Microphone(sample_rate=16000) as mic:
                print("Listening")
                recognizer.adjust_for_ambient_noise(mic)
                audio = recognizer.listen(mic)

                audio = audio.get_wav_data()
                return audioRecognition_google_cloud(audio)

        except sr.RequestError as e:
            print("Błąd połączenia z serwerem rozpoznawania mowy:", e)
            break


def speechSaying_google_cloud(text):  #to swapp if need better
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'alpine-comfort-450522-r7-5220dba41876.json'

    client = texttospeech.TextToSpeechClient()

    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="pl-PL",
        name="pl-PL-Wavenet-A",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        effects_profile_id=['small-bluetooth-speaker-class-device'],
        speaking_rate=1,
        pitch=1
    )

    response = client.synthesize_speech(
        input=synthesis_input,
        voice=voice,
        audio_config=audio_config
    )

    with open("outputSpeech.mp3", 'wb') as out:
        out.write(response.audio_content)

    playSound("outputSpeech.mp3")


def audioRecognition_google_cloud(audio):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'alpine-comfort-450522-r7-5220dba41876.json'

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content=audio)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.MP3,
        sample_rate_hertz=16000,
        audio_channel_count=1,
        enable_automatic_punctuation=True,
        language_code="pl-PL",
        model='latest_short'
    )

    response = client.recognize(config=config, audio=audio)

    for result in response.results:
        return result.alternatives[0].transcript.lower()


