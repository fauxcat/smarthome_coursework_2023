from tkinter import *
from backend import *



mainWin = Tk()


def setupHome():
    global home 
    home = SmartHome()
    plug1_1 = SmartPlug()
    light1_2 = SmartLight()
    plug2_3 = SmartPlug()
    plug3_4 = SmartPlug()
    light2_5 = SmartLight()

    home.addDevice(plug1_1)
    home.addDevice(light1_2)
    home.addDevice(plug2_3)
    home.addDevice(plug3_4)
    home.addDevice(light2_5)


def setupMainWin():
    mainWin.title("Smart Home")
    mainWin.geometry("500x350")
    mainWin.resizable(False, False)
    mainWin.columnconfigure(index=0, weight=2)

    allOffBtn = Button(mainWin, text="Turn all off", command=allOffPressed)
    allOffBtn.grid(row=0, column=0, padx=10, pady = 10, sticky="w")
    
    allOnBtn = Button(mainWin, text="Turn all on", command=allOnPressed)
    allOnBtn.grid(row=1, column=0, padx=10, pady = 10, sticky="w")

    listDevices()
    mainWin.mainloop()

def listDevices():
    global textList
    textList = []
    global deviceIndex
    for deviceIndex in range(5):
        device = home.getDeviceAt(deviceIndex)

        global deviceTxt
        deviceTxt = Text(mainWin, height=1, width=50)
        deviceTxt.insert("1.0", str(device))
        deviceTxt.grid(row = deviceIndex+2, column = 0, padx=10, pady=10)
        textList.append(deviceTxt)

        toggleBtn = Button(mainWin, text="Toggle this", command=lambda index=deviceIndex: togglePressed(index))
        toggleBtn.grid(row=deviceIndex+2, column=1, padx=10, pady = 10, sticky="e")


def reListDevices():
    for deviceIndex in range(5):
        device = home.getDeviceAt(deviceIndex)

        textList[deviceIndex].delete("1.0", "2.0")
        textList[deviceIndex].insert("1.0", str(device))


def allOffPressed():
    home.turnOffAll()
    reListDevices()

def allOnPressed():
    home.turnOnAll()
    reListDevices()

def togglePressed(index):
    
    device = home.getDeviceAt(index)
    device.toggleSwitch()
    reListDevices()

def main():
    setupHome()
    setupMainWin()
    listDevices()

main()