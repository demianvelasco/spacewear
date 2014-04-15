from Tkinter import *
from BreakfastSerial import Arduino, Buzzer, Sensor, setInterval, Led
import time


board = Arduino()
led = Led(board, 12)
buzzer = Led(board, 8)

def alert():
	print"Return to base"
	led.blink(100)
	buzzer.blink(100)

def oxygenAlert():
	led.off()
	buzzer.off()
	led.on()
	#time.sleep(2)
	print"Current Oxygen level: |||||||||| 86 %"

def dangerAlert():
	led.blink(1000)
	buzzer.blink(800)
	print"Danger Approaching. Return to base"
def co2Alert():
	led.blink(1000)
	buzzer.blink(800)
	print"Oxygen level too low ||||        23% "

def batteryStatus():
	led.blink(200)
	print"Battery Status: ||||||||||||    65%"

def stopAlert():
	led.off()
	buzzer.off()
	print"No current alerts"

if __name__ == "__main__":
	master = Tk()
	master.title("SpaceWear - KSC")
	f = Frame(master, height=200, width=500)
	f.pack_propagate(0) # don't shrink
	f.pack()
	alertButton = Button(master, text="Alert", command=dangerAlert)
	alertButton.pack()
	alertButton.place(bordermode=OUTSIDE, height=100, width=200)
	oxygenButton = Button(master, text="Oxygen Levels", command=oxygenAlert)
	oxygenButton.pack()
	#oxygenButton.place(bordermode=OUTSIDE, height=200, width=200)
	stopAlertButton = Button(master, text="Stop Alert", command=stopAlert)
	stopAlertButton.pack()

	alertButton2 = Button(master, text="Return to base", command=alert)
	alertButton2.pack()

	alertButton3 = Button(master, text="Battery Status", command=batteryStatus)
	alertButton3.pack()

	alertButton4 = Button(master, text="CO2 Status", command=co2Alert)
	alertButton4.pack()

	master.mainloop()

