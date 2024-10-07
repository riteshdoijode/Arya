import openai
import pyttsx3
import speech_recognition as sr
import time
import sys

openai.api_key = "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"

engine = pyttsx3.init()
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print('Skipping unkown error')

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response["choices"][0]["text"]

def speak_text(text):
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        print("Say 'Arya' to start recording your question...")
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source)
            try:
             transcription = recognizer.recognize_google(audio)
             if transcription.lower() == "arya":
                 
               filename = "input.wav"
               print("Say your question...")
               with sr.Microphone() as soruce:
                  recognizer = sr.Recognizer()
                  source.pause_threshold = 1
                  audio = recognizer.listen(source, phrase_time_limit=None, timeout=None)
                  with open(filename, "wb") as f:
                      f.write(audio.get_wav_data())
             
                
                #Transcribe audio to text
                  text = transcribe_audio_to_text(filename)
                  if text:
                    print(f"You said: {text}")

                    response = generate_response(text)
                    print(f"GPT-3 says: {response}")

                    speak_text(response)

             elif transcription.lower() == "exit":
                  sys.exit(0)

            except Exception as e:
               print("An error occurred: {}".format(e))

if __name__ == "__main__":
   main()
