import openai
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecgnition


openai.api_key = "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"

engine = pyttsx3.init('sapi5') #what is sapi5? It is used to take voices from computer.
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)

#start of the code for open ai

r = sr.Recognizer()
mic = sr.Microphone(device_index=1)

conversation = ""
user_name = "Ritesh"
bot_name = "Arya"

while True:
    with mic as source:
        print("\n Listening...")
        r.adjust_for_ambient_noise(source,duration=0.2)
        audio = r.listen(source)
    print("no longer listening")


    try:
        user_input = r.recognize_google(audio)
    except:
        continue


    prompt = user_name+":"+user_input + "\n"+bot_name+":"
    conversation += prompt

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=conversation,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    response_str = response["choices"][0]["text"].replace("\n","")
    response_str = response_str.split(
        user_name + ":" ,1)[0].split(bot_name+ ":",1)[0]
    
    conversation+= response_str +"\n"
    print(response_str)

    engine.say(response_str)
    engine.runAndWait()


    