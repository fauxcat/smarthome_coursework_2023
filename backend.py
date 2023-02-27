class SmartPlug():

    def __init__(self, switchedOn=False, consumptionRate=0):
        self.switchedOn = switchedOn
        self.consumptionRate = consumptionRate

    def getSwitchedOn(self):
        return self.switchedOn

    def getConsumptionRate(self):
        return self.consumptionRate

    def toggleSwitch(self):
        self.switchedOn = not self.switchedOn

    def setConsumptionRate(self, newConsumptionRate):
        if (0 <= newConsumptionRate <= 150):
            self.consumptionRate = newConsumptionRate
        
    def __str__(self):
        output = "Plug: Switched on = {}, {} consumption".format(self.switchedOn, self.consumptionRate)
        return output

class SmartLight(SmartPlug):
    def __init__(self, switchedOn=False, brightness=0):
        super().__init__(switchedOn)
        self.brightness = brightness
    
    def getBrightness(self):
        return self.brightness
    
    def setBrightness(self, newBrightness):
        if (0 <= newBrightness <= 100):
            self.brightness = newBrightness

    def __str__(self):
        output = "Light: Switched on = {}, {} brightness".format(self.switchedOn, self.brightness)

        return output

class SmartHome():
    def __init__(self):
        self.devices = []

    def getDevices(self):
        return self.devices

    def getDeviceAt(self, index):
        return self.devices[index]

    def addDevice(self, device):
        self.devices.append(device)

    def toggleSwitch(self, index):
        self.devices[index].toggleSwitch()

    def turnOnAll(self):
        for i in range(len(self.devices)):
            self.devices[i].switchedOn = True

    def turnOffAll(self):
        for i in range(len(self.devices)):
            self.devices[i].switchedOn = False

    def __str__(self):
        output = ""
        for device in self.devices:
            output += "{}\n".format(device)
        return output

def testSmartPlug():
    plug = SmartPlug()

    plug.toggleSwitch()

    print(plug.getSwitchedOn())
    print(plug.getConsumptionRate())

    plug.setConsumptionRate("seven")
    print(plug.getConsumptionRate())

def testSmartLight():
    light = SmartLight()

    light.toggleSwitch()
    print(light.getSwitchedOn())

    print(light.getBrightness())
    light.setBrightness(50)
    print(light.getBrightness())

    print(light)

def testSmartHome():
    home = SmartHome()
    plug1 = SmartPlug()
    plug2 = SmartPlug()
    light1 = SmartLight()

    plug2.toggleSwitch()
    plug2.setConsumptionRate(45)
    light1.setBrightness(12)

    home.addDevice(plug1)
    home.addDevice(plug2)
    home.addDevice(light1)

    print(home)

    home.turnOnAll()

    print(home)


