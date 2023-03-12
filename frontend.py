from tkinter import *
from backend import *



mainWin = Tk()
global devicesOn
devicesOn = 0

def setupHome():
    """
    Creates a new home and adds the correct devices for my UP number(s).
    """
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
    """
    Setup `mainWin` to display the home and its devices.
    Display two buttons that turn on and turn off all devices.
    Calls function to display the devices.
    """
    mainWin.title("Smart Home")
    mainWin.geometry("600x350")
    mainWin.resizable(False, False)
    mainWin.columnconfigure(index=0, weight=2)

    allOffBtn = Button(mainWin, text="Turn all off", command=allOffPressed)
    allOffBtn.grid(row=0, column=0, padx=10, pady = 10, sticky="w")
    
    allOnBtn = Button(mainWin, text="Turn all on", command=allOnPressed)
    allOnBtn.grid(row=1, column=0, padx=10, pady = 10, sticky="w")

    listDevices()
    mainWin.mainloop()

def listDevices():
    """
    For each device in `home`, create a text widget, and two buttons on the `mainWin`.
    The text contains the device's information.
    One button is used to toggle the device.
    The other button is used to configure the device.
    """
    global textList
    textList = []
    global deviceIndex
    for deviceIndex in range(5):
        device = home.getDeviceAt(deviceIndex)

        global deviceTxt
        deviceTxt = Text(mainWin, height=1, width=50)
        deviceTxt.insert("1.0", str(device))
        deviceTxt.grid(row=deviceIndex+2, column=0, padx=10, pady=10, sticky="w")
        textList.append(deviceTxt)

        toggleBtn = Button(mainWin, text="Toggle this", command=lambda index=deviceIndex: togglePressed(index))
        toggleBtn.grid(row=deviceIndex+2, column=1, padx=10, pady = 10, sticky="e")

        def configCmd(i=deviceIndex):
            configWindow(i)
        
        configBtn = Button(mainWin, text="Configure", command=configCmd)
        configBtn.grid(row=deviceIndex+2, column=2, padx=10, pady = 10, sticky="e")

    global devicesOnLabel
    devicesOnLabel = Label(mainWin, text=("Number of devices turned on: {}").format(devicesOn))
    devicesOnLabel.grid(row=7, column=0, padx=10, sticky="w")


def reListDevices():
    """
    After any changes are made to the devices, this function is used instead of listDevices.
    This is because there is no need to draw every widget again over the initially drawn widgets.
    """
    for deviceIndex in range(5):
        device = home.getDeviceAt(deviceIndex)

        textList[deviceIndex].delete("1.0", "2.0")
        textList[deviceIndex].insert("1.0", str(device))
    
    devicesOnLabel.config(text = ("Number of devices turned on: {}").format(devicesOn))
    


def configWindow(deviceIndex):
    """
    Create a new window to configure the device at `deviceIndex` of `home`.
    The window will contain a text, showing the product's information.
    The window will also contain a cancel button to close the config window.
    The window will also contain an entry to change the respective integer value for each device.
    The new value entered into the window can be used to configure the device with the submit button if it is a valid input.
    When the change is submitted, the list of devices in `mainWin` will update.
    """
    configWin = Toplevel()
    configWin.geometry("400x150")
    configWin.resizable(False, False)
    
    device = home.getDeviceAt(deviceIndex)
    configWin.title("Configure Smart Device")

    titleLabelTxt = Label(configWin, text="Configure Smart Device")
    titleLabelTxt.grid(row=0, column=0, padx=10, sticky="w")
    titleLabelTxt.config(font=("TkDefaultFont", 12, "bold"))

    deviceTxt = Text(configWin, height=1, width=45)
    deviceTxt.insert("1.0", str(device))
    deviceTxt.grid(row=1, column=0,columnspan=2, padx=10, pady=10, sticky="w")

    inputEntry = Entry(configWin)
    inputEntry.grid(row=2, column=0, padx=10, pady=10, sticky="w")


    def submitCmd():
        errorLabel = Label(configWin, text="")
        errorLabel.destroy()

        if type(device) is SmartPlug:
            try:
                if 0 <= int(inputEntry.get()) <= 150:
                    newConsumptionRate = int(inputEntry.get())
                    device.setConsumptionRate(newConsumptionRate)
                    reListDevices()
                    configWin.destroy()
                else:
                    errorLabel = Label(configWin, text="Please enter an integer between 0 and 150")
                    errorLabel.grid(row=3, column=0, padx=75, pady=10, sticky="w")
            except ValueError:
                errorLabel = Label(configWin, text="Please enter an integer")
                errorLabel.grid(row=3, column=0, padx=75, pady=10, sticky="w")
        elif type(device) is SmartLight:
            try:
                if 0 <= int(inputEntry.get()) <= 100:
                    newBrightness = int(inputEntry.get())
                    device.setBrightness(newBrightness)
                    reListDevices()
                    configWin.destroy()
                else:
                    errorLabel = Label(configWin, text="Please enter an integer between 0 and 100")
                    errorLabel.grid(row=3, column=0, padx=75, pady=10, sticky="w")
            except ValueError:
                errorLabel = Label(configWin, text="Please enter an integer")
                errorLabel.grid(row=3, column=0, padx=75, pady=10, sticky="w")

    submitBtn = Button(configWin, text="Submit", command=submitCmd)
    submitBtn.grid(row=2, column=0, padx=150, sticky="w")

    cancelBtn = Button(configWin, text="Cancel", command=configWin.destroy)
    cancelBtn.grid(row=3, column=0, padx=10, pady=10, sticky="w")


    

def allOffPressed():
    """
    Turns every device in the home off, regardless of its previous state.
    """
    global devicesOn
    home.turnOffAll()
    devicesOn = 0
    reListDevices()

def allOnPressed():
    """
    Turns every device in the home on, regardless of its previous state.
    """
    global devicesOn
    home.turnOnAll()
    devicesOn = 5
    reListDevices()

def togglePressed(index):
    """
    Toggles the device at the given index on/off.
    """
    global devicesOn
    device = home.getDeviceAt(index)
    device.toggleSwitch()

    if device.getSwitchedOn() == False:
        devicesOn -= 1
    else:
        devicesOn += 1
    reListDevices()

def main():
    setupHome()
    setupMainWin()
    listDevices()

main()