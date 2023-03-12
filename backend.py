class SmartPlug():
    """
    A class to represent a smart plug.
    A smart plug has a consumption rate and is switched on or off.
    The consumtion rate is 0 by default.
    The smart plug is switched off by default.
    """

    def __init__(self, switchedOn=False, consumptionRate=0):
        self.switchedOn = switchedOn
        self.consumptionRate = consumptionRate

    def getSwitchedOn(self):
        """
        Returns the switched on/off status of the smart plug.
        """
        return self.switchedOn

    def getConsumptionRate(self):
        """
        Returns the consumption rate of the smart plug.
        """
        return self.consumptionRate

    def toggleSwitch(self):
        """
        Toggles the status of the smart plug.
        If the smart plug is switched off, this function will turn the switch on and vice versa.
        """
        self.switchedOn = not self.switchedOn

    def setConsumptionRate(self, newConsumptionRate):
        """
        Sets the consumption rate of the smart plug to the given value.
        If newConsumptionRate is not within the range of 0 and 150, the consumption rate is not changed.
        In the event of an invalid consumption rate, an error is printed.
        """
        if (0 <= newConsumptionRate and newConsumptionRate <= 150):
            self.consumptionRate = newConsumptionRate
        else:
            print("Invalid consumption rate, must be between 0 and 150")
        
    def __str__(self):
        output = "Plug: Switched on = {}, {} consumption".format(self.switchedOn, self.consumptionRate)
        return output

class SmartLight(SmartPlug):
    """
    A class to represent a smart light.
    A smart light has a brightness and is switched on or off.
    The brightness is 0 by default.
    The smart light is switched off by default.
    """
    def __init__(self, switchedOn=False, brightness=0):
        """
        The switchedOn attribute from smart plug is inherited to this class.
        Therefore the getter and setter methods are also inherited, meaning they do not need to be defined here again.
        """
        super().__init__(switchedOn)
        self.brightness = brightness
    
    def getBrightness(self):
        """
        Returns the brightness of the smart plug.
        """
        return self.brightness
    
    def setBrightness(self, newBrightness):
        """
        Sets the brightness of the smart light to the given value.
        If newBrightness is not within the range of 0 and 100, the brightness is not changed.
        In the event of an invalid brightness, an error is printed.
        """
        if (0 <= newBrightness and newBrightness <= 100):
            self.brightness = newBrightness
        else:
            print("Invalid brightness, must be between 0 and 100")

    def __str__(self):
        output = "Light: Switched on = {}, {} brightness".format(self.switchedOn, self.brightness)

        return output

class SmartHome():
    """
    A class to represent a smart home.
    A smart home stores a list of smart plugs and smart lights.
    """
    def __init__(self):
        self.devices = []

    def getDevices(self):
        """
        Returns every smart device in the smart home.
        """
        return self.devices

    def getDeviceAt(self, index):
        """
        Returns the smart device with the given index in the smart home.
        """
        return self.devices[index]

    def addDevice(self, device):
        """
        Adds a smart device to the smart home, at the end of the list.
        """
        self.devices.append(device)

    def toggleSwitch(self, index):
        """
        Toggles the on/off status of the smart device at the given index.
        """
        self.devices[index].toggleSwitch()

    def turnOnAll(self):
        """
        Changes all of the smart devices' on/off statuses to on, regardless of their previous status.
        """
        for i in range(len(self.devices)):
            self.devices[i].switchedOn = True

    def turnOffAll(self):
        """
        Changes all of the smart devices' on/off statuses to off, regardless of their previous status.
        """
        for i in range(len(self.devices)):
            self.devices[i].switchedOn = False

    def __str__(self):
        output = ""
        for device in self.devices:
            output += "{}\n".format(device)
        return output

def testSmartPlug():
    """
    Tests the smart plug class.
    First, a plug is created with the SmartPlug class.
    The plug is switched from its default value of off to on.
    The setConsumptionRate method is then tested by using a non-integer value as an input parameter.
    """
    plug = SmartPlug()

    plug.toggleSwitch()

    print(plug.getSwitchedOn())
    print(plug.getConsumptionRate())

    plug.setConsumptionRate("seven")
    print(plug.getConsumptionRate())

def testSmartLight():
    """
    Tests the smart light class.
    First, a light is created with the SmartLight class.
    The light is switched from its default value of off to on.
    The setBrightness method is then tested by using an integer value as an input parameter.
    """
    light = SmartLight()

    light.toggleSwitch()
    print(light.getSwitchedOn())

    print(light.getBrightness())
    light.setBrightness(50)
    print(light.getBrightness())

    print(light)

def testSmartHome():
    """
    Tests the smart home class.
    First, a home is created with the SmartHome class.
    Several smart devices are created using their respective classes.
    Some of the devices are edited with their own methods.
    All devices are added to the list in the home with the addDevice method.
    Every device that has now been added to the home is now switched on.
    """
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
