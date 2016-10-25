# Alarm in Python
# Playing Sound on youtube to wake the person up
# I havent really battle tested the program so it might contain bugs
# If you come accross the bugs inform me

from time import sleep,ctime
import datetime
import webbrowser
import random

now = datetime.datetime.now()
linksToSounds = ['https://www.youtube.com/watch?v=6pR5cyH63mA','https://www.youtube.com/watch?v=e12KryuLcbs','https://www.youtube.com/watch?v=nbjwmC8K4K4','https://www.youtube.com/watch?v=UqSww10eeKw','https://www.youtube.com/watch?v=9f06QZCVUHg','https://www.youtube.com/watch?v=kffacxfA7G4'] # remember to add links and test the code

def alarm(h,m,s):
    timeToSleep = h * 3600 + m * 60 + s
    sleepingTime = sleep(timeToSleep)
    playSound = webbrowser.open_new(random.choice(linksToSounds))

# Main code
print(ctime(),'\n')
startOrEnd = str(input('Set alarm or End : '))
if startOrEnd.strip() == 'Set alarm':
    hours = int(input('Hours : '))
    minutes = int(input('Minutes : '))
    seconds = int(input('Seconds : '))
    print('Alarm started at %s : %s'%(now.hour,now.minute))
    print(alarm(hours,minutes,seconds))
    wakedUp = False
    while wakedUp == False:
        get = str(input('Have you waked up : '))
        if get == 'Yes':
            print('Good')
            wakedUp = True
        else:
            sleepMoreTime = sleep(300) # playing sound again in 5 minutes
            playSoundAgain = webbrowser.open_new(random.choice(linksToSounds))
            continue

else :
    quit()
