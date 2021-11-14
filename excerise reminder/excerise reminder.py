from pygame import mixer
from datetime import datetime, time
import time
import speech_recognition as sr
import pyttsx3

def getdate():
    import datetime
    return datetime.datetime.now()
r=str(getdate())

print("Hello I am your HEALTHTRACKER")
engine=pyttsx3.init()
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('Hello i am your healthtracker ')
engine.runAndWait()
i=1
while(True):
   now = datetime.now()
   k= now.strftime("%H.%M")
   a=float(k)
  
 
   
   if a==03.53:
      
       while (True):
           
           mixer.init()
           mixer.music.load("song.mp3")
           

# Setting the volume
           mixer.music.set_volume(0.7)

# Start playing the song
           mixer.music.play()
          
           print("enter r to stop")
           query = input()
           
           if query=="r":
               
               mixer.music.stop()
               print("We are waiting for you to drink water")
               time.sleep(50)
               print("did u drink?")
               a=input()
               if a=="yes":
                      
                      f=open("water.txt" , "a" )
                      f.write( a)
                      f.write(r)
                      f.close()
                      print("Wait for next task")
                      break
               elif a=="skip":
                      f=open("water.txt" , "a" )
                      f.write( a)
                      f.write(r)
                      f.close()
                      print("Wait for next task")
                      break         
   elif a==03.58:
	   while (True):
           
            mixer.init()
            mixer.music.load("song2.mp3")

# Setting the volume
            mixer.music.set_volume(0.7)

# Start playing the song
            mixer.music.play()
          
            print("enter r to stop")
            query = input()
           
            if query=="r":
               
               mixer.music.stop()
               print("We are waiting for you to complete your eye excerise")
               time.sleep(50)
               print("have you done your eye-excerise?")
               a=input()
               if a=="yes":
                      
                      f=open("eye.txt" , "a" )
                      f.write( a)
                      f.write(r)
                      f.close()
                      print("Wait for next task")
                      break
               elif a=="skip":
                      f=open("eye.txt" , "a" )
                      f.write( a)
                      f.write(r)
                      f.close()
                      print("Wait for next task")
                      break  
   elif a==04.00:
	   while (True):
           
            mixer.init()
            mixer.music.load("song3.mp3")

# Setting the volume
            mixer.music.set_volume(0.7)

# Start playing the song
            mixer.music.play()
          
            print("enter r to stop")
            query = input()
           
            if query=="r":
               
               mixer.music.stop()
               print("We are waiting for you to complete your excerise")
    
               time.sleep(50)
               print("have you done your excerise?")
               a=input()
               if a=="yes":
                      
                      f=open("excerise.txt" , "a" )
                      f.write( a)
                      f.write(r)
                      f.close()
                      print("Wait for next task")
                
                      break
               elif a=="skip":
                      f=open("excerise.txt" , "a" )
                      f.write( a)
                      f.write(r)
                      f.close()
                      print("Wait for next task")
                      break                
   elif a==04.05:
       
    
        engine.say('Congratulations you have completed all your tasks')
        engine.runAndWait()
        engine.endLoop()
        
      
        
  
   
       
           
    
       
       
    
		       

           
       
       





# infinite loop
"""while True:
           
	
	       print("Press 'p' to pause, 'r' to resume")
	       print("Press 'e' to exit the program")
	       query = input(" ")
	
	       if query == 'p':

		# Pausing the music
		       mixer.music.pause()	
	       elif query == 'r':

		# Resuming the music
		       mixer.music.unpause()
	       elif query == 'e':

		# Stop the mixer
		       mixer.music.stop()
		       break"""
