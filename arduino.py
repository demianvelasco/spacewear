from Tkinter import *
from BreakfastSerial import Arduino, Buzzer, Sensor, setInterval, Led
import time

board = Arduino()
led = Led(board, 12)
buzzer = Led(board, 8)

master = Tk()
master.title("SpaceWear - KSC")


f = Frame(master, height=500, width=600)
f.pack_propagate(0) # don't shrink
f.pack()

def alert():
	print"Hello peeps"
	led.blink(500)
	buzzer.blink(250)

def oxygenAlert():
	led.off()
	buzzer.off()
	led.on()
	time.sleep(2)
	led.off()

	print"Current Oxygen level: ||||||||"
def dangerAlert():
	alert()
	print"Danger Approaching. Return to base"
def co2Alert():
	print"Oxygen level too low |     "

def stopAlert():
	led.off()
	buzzer.off()
	print"Return to base"



if __name__ == "__main__":
	alertButton = Button(master, text="Alert!!!", command=alert)
	alertButton.pack()
	alertButton.place(bordermode=OUTSIDE, height=100, width=100)

	oxygenButton = Button(master, text="Oxygen Levels", command=oxygenAlert)
	oxygenButton.pack()
	#oxygenButton.place(bordermode=OUTSIDE, height=200, width=200)


	stopAlertButton = Button(master, text="Stop Alert", command=stopAlert)
	stopAlertButton.pack()
	mainloop()
