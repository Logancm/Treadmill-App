from tkinter import*
from tkinter import messagebox
import random

#set window frame settings
root = Tk()
root.title('My treadmill')
root.geometry("580x440")
root.maxsize(580, 440)
root.minsize(580, 440) 
root.configure(bg="#ADD8E6")

#set global variables
minutes = 0
seconds = 0
running = False
speed = 0
calories = 0
miles = 0.0
milesPerSecond = 0.0
caloriesPerSecond = 0.0


#function to start workout
def startWorkout():
    global running
    if not running:
        running = True
        update()


#function to pause workout
def pauseWorkout():
    global running
    if running:
        running = False

#function to end workout
def endWorkout():
    caloriesDone = int(calories)
    milesDone = format(miles, ".2f")
    messagebox.showinfo("RESULTS", "Here is your workout results:" + 
                        "\nYou ran for " + str(minutes) + " minutes and " + str(seconds) + " seconds."
                        + "\nYou burned " + str(caloriesDone) + " calories." + "\n" 
                        + "You ran for " + str(milesDone) + " totals miles.")
    root.quit()

#function to show workout results
def showWorkoutresults():
    return

#function to update the running workout timer
def update():
    global minutes, seconds
    #figure out minutes and seconds
    if running:
        seconds += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
        if minutes == 60:
            minutes = 0
            
    
    
    ## makes sure there is leading zeros when need be for the clock
        minutes_string = f'{minutes}' if minutes > 9 else f'0{minutes}'
        seconds_string = f'{seconds}' if seconds > 9 else f'0{seconds}'
        
        #weird algorithm to get the pace into a string
        if speed > 0:
            paceMinutes = int(60/speed)
            paceSeconds = int(((60/speed) - paceMinutes) * 60)
            paceMinutesString = f'{paceMinutes}' if paceMinutes > 9 else f'0{paceMinutes}'
            paceSecondsString = f'{paceSeconds}' if paceSeconds > 9 else f'0{paceSeconds}'
            paceLabel.config(text= paceMinutesString + ":" + paceSecondsString + "\nPace")
            #solves miles problem
            global milesPerSecond
            global miles
            milesPerSecond = speed/3600
            miles = miles + milesPerSecond
            milesFormatted = float(format(miles, ".2f"))
            milesLabel.config(text= str(milesFormatted) + "\nMiles")
            #solves calories problem
            global calories
            global caloriesPerSecond
            randomAvgCalories = random.randint(100, 200)#average number of calries per mile vary
            caloriesPerSecond = (randomAvgCalories * milesPerSecond)
            calories = calories + caloriesPerSecond
            caloriesFormatted = int(calories)
            caloriesLabel.config(text= str(caloriesFormatted) + "\nCalories")
        
        clockLabel.config(text="Time elapsed " + minutes_string + ":" + seconds_string, )
        clockLabel.after(1000, update)

def speedUp():
    global speed
    if speed <12:
        speed = speed + 1
        speedLabel.config(text= str(speed) + "\nMPH\nSPEED",)


def slowDown():
    global speed
    if speed >0:
        speed = speed - 1
        speedLabel.config(text= str(speed) + "\nMPH\nSPEED",)


#create start button and place on screen
startButton = Button(root, text="Start", command = startWorkout, bg = "#96CEB4", font = ("Times New Roman",10))
startButton.place(x=90, y=400)

#create pause button and place on screen
pauseButton = Button(root, text="Pause", command = pauseWorkout, bg = "#D9534F", font = ("Times New Roman",10))
pauseButton.place(x=290, y=400)

#create end workout button and place on screen
endWorkoutButton = Button(root, text="End workout", command = endWorkout, bg = "#FFEEAD", font = ("Times New Roman",10))
endWorkoutButton.place(x=490, y=400)

#create speed up button and place on screen
speedUpButton = Button(root, text="+", command = speedUp, bg="#96CEB4", font = ("Times New Roman",12), padx= 30)
speedUpButton.place(x=487, y=163)

#create slow down button and place on screen
slowDownButton = Button(root, text="-", command = slowDown, bg="#D9534F", font = ("Times New Roman",12), padx = 30)
slowDownButton.place(x=487, y=309)

#create the timer with a label
clockLabel = Label(root, text=("Time elapsed 00:00" ))
clockLabel.config(pady=10, 
                  font = ("Times New Roman",32), 
                  bg="#ADD8E6")
clockLabel.pack()

#create speed label
speedLabel = Label(root, 
                   text= str(speed) + "\nMPH\nSPEED",
                   font = ("Times New Roman",22), 
                   bg="#FFEEAD",
                   relief="groove")
speedLabel.place(x=480, y=200)

#creat Calories label
caloriesLabel = Label(root, 
                      text= str(calories) + "\nCalories", 
                      font = ("Times New Roman",22),
                      bg = "#FFAD60",
                      relief="groove",
                      padx = 5, pady = 18)
caloriesLabel.place(x=50,y=200)

#create Miles label
milesLabel = Label(root, 
                      text= str(miles) + "\nMiles", 
                      font = ("Times New Roman",22),
                      bg = "#FFAD60",
                      relief="groove",
                      padx = 20, pady = 18)
milesLabel.place(x=200,y=200)

#create Pace label
paceLabel = Label(root, 
                      text= "00:00\nPace", 
                      font = ("Times New Roman",22),
                      bg = "#FFAD60",
                      relief="groove",
                      padx = 25, pady = 18)
paceLabel.place(x=350,y=200)


root.mainloop()