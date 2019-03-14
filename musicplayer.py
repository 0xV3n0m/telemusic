import os
import pygame
import telepot
from telepot.loop import MessageLoop
import config


#bot key
bot = telepot.Bot('ENTER YOUR KEY HERE')
#que
q = []
#if queue is empty or not
empty = False
#directory name
dir_name = "MUSIC LOCATION"
#variable to hold listing
a = os.listdir(dir_name)
#store all the msuic files
listall = """Music archive."""
#list all the music in directory
for i in range(0,len(a)):
   print('{}.{}'.format(i,a[i]))
   listall = listall + '\n{}.{}'.format(i,a[i])
#Send message to user with their user ID
def sms(ID, str):
	bot.sendMessage(ID, str)
#reply message to user with their user ID and to the message ID
def reply(ID, msgID, str):
	bot.sendMessage(ID, str, None, None, None, msgID)
#handling all new messages, like the getUpdates()
def handle(msg):
   user_id = msg['chat']['id']
   msg_id = msg['message_id']
   command = msg['text'].encode('utf-8')
   #output the whole directory
   if command == '/help':
     sms(user_id, listall)
     return
   if command == '/all':
     for i in range(0, len(a)):
      q.insert(0,i)
     sms(user_id, "Successfully inserted all songs. Size:{}".format(len(q)))
     return
   if command == '/stop':
     pygame.mixer.music.stop()
       
#Checking for new messages
MessageLoop(bot, handle).run_as_thread()
while 1:
    if (len(q) > 0):
        try:
            empty = False
            song = q.pop()
            loc = str(dir_name) + str(a[int(song)])
            pygame.init()
            pygame.mixer.init()     
            pygame.mixer.music.load(loc)
            pygame.mixer.music.play()
            #bot.sendMessage(user_id,"Playing {}".format(a[int(song)]))
            while pygame.mixer.music.get_busy() == True: 
              MessageLoop(bot, handle).run_as_thread()
              continue
        except:
            print('ERROR')
    else:
        if empty == False:
            print('Queue is empty. Nothing to play')
            #bot.sendMessage(user_id,"Playlist finished!")
            empty = True
time.sleep(1)	

   
