import speech_recognition as sr

r = sr.Recognizer()

with sr.Microphone(device_index=1) as source:
    r.adjust_for_ambient_noise(source)
    print("Speak anything")
    audio = r.listen(source)
    print('audio')
    try:
        print('inside loop')
        text = r.recognize_google(audio)
        print('You said:{}'.format(text))
        file1 = open('D:\MLWorkspace\speech.txt','a')
        file1.writelines('{}'.format(text))
        file1.close()
    except:
        print("Print Sorry We cannot recognize yor voce")
