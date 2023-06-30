import speech_recognition as sr

def reconhecer_fala():
    microfone = sr.Recognizer()

    with sr.Microphone() as source:
        microfone.adjust_for_ambient_noise(source)
        print('Diga alguma coisa: ')
        audio = microfone.listen(source)

        try: 
            frase = microfone.recognize_google(audio, language='pt-BR')
            print('Você disse: '+ frase)
        except:
            print('Não entendi o que você quis dizer :/')
        return frase
    
reconhecer_fala()