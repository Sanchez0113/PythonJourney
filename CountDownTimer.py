
#importing the time library
import time
#Builds the function being called and asks for the seconds as the argument
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        #This calls into the time library and formats the time per minutes and seconds and formats it as so
        timer = '{:02d}:{:02d}'.format(mins,secs)
        #This displays the timer in the terminal 
        print(timer, end = '\r')
        #This tells the final number of the timer before endind the function
        time.sleep(1)
        #This ticks the countdown by -1
        t -= 1
  #At the end of the timer it prints "Alarm" to the terminal  
    print('Alarm!')
#Asks for an input from the user that is saved into 't' which is then used as the argument for the countdown function
t = input('Enter the time in seconds')

#Calling the function
countdown(int(t))