import speech_recognition as sr


class Artemis:
   
   
 def reconhecimento_de_voz():       
   #reconhecedor
   #habilita o microfone 
   reconhecedor = sr.Recognizer()

   #abrir microfone para capitura de voz
   with sr.Microphone() as source: 
   
    reconhecedor.adjust_for_ambient_noise(source)   #Chama a funcao de reducao de ruido disponivel na speech_recognition
    print("Diga alguma coisa: ")

    while True:
     audio = reconhecedor.listen(source) #define microfone como arquivo de audio
    
     try:
      #Passa o audio para o reconhecedor de padroes do speech_recognition
       palavra = reconhecedor.recognize_google(audio,language='pt-BR')

       
      #Após alguns segundos, retorna a frase falada
       print("Artemis: Você disse: " + palavra)
   
       
       if palavra == 'brisa': #termia execusão ao dizer brisa
           exit()
     #Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
     except sr.UnknownValueError:
      
       print("Artemis: Não entendi")
     
 reconhecimento_de_voz()
   

