# coding: utf-8
# Author : Donghoon Gwag
# Version : 1.0.0
# Date : 2020-03-12

 
import sys
from PyQt5 import QtWidgets
from PyQt5 import uic
from Phidget22.PhidgetException import *
from Phidget22.Phidget import *
from Phidget22.Devices.Log import *
from Phidget22.LogLevel import *
from Phidget22.Devices.DigitalOutput import *
import traceback
import time

RC_Serial = 520892

class Relay_Channel() :
    def __init__(self, chno, parent):
        self.ch_no = chno
        self.parent = parent

        #Create your Phidget channels
        self.digitalOutput = DigitalOutput();

        #Set addressing parameters to specify which channel to open (if any)
        self.digitalOutput.setDeviceSerialNumber(RC_Serial)
        self.digitalOutput.setChannel(self.ch_no)

    def onDigitalOutput_Connect(self):

        #Assign any event handlers you need before calling open so that no events are missed.
        self.digitalOutput.setOnAttachHandler(self.onDigitalOutput_Attach)
        self.digitalOutput.setOnDetachHandler(self.onDigitalOutput_Detach)
        self.digitalOutput.setOnErrorHandler(self.onDigitalOutput_Error)

        try :
            #Open your Phidgets and wait for attachment
            self.digitalOutput.openWaitForAttachment(500)
            return True

        except PhidgetException as ex:
            #We will catch Phidget Exceptions here, and print the error informaiton.
            return False
            traceback.print_exc()
            print("")
            print("PhidgetException " + str(ex.code) + " (" + ex.description + "): " + ex.details)

    def onDigitalOutput_On(self):
        #Do stuff with your Phidgets here or in your event handlers.
        self.digitalOutput.setDutyCycle(1)

    def onDigitalOutput_Off(self):
        #Do stuff with your Phidgets here or in your event handlers.
        self.digitalOutput.setDutyCycle(0)

    def onDigitalOutput_Attach(self, none):
        print("Attach [" + str(self.ch_no) + "]!")
        self.parent.attached(self.ch_no)

    def onDigitalOutput_Detach(self, none):
        print("Detach [" + str(self.ch_no) + "]!")
        self.parent.detached(self.ch_no)

    def onDigitalOutput_Error(self, code, description, none):
        print("Code [" + str(self.ch_no) + "]: " + ErrorEventCode.getName(code))
        print("Description [" + str(self.ch_no) + "]: " + str(description))
        print("----------")

class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)

        self.relay0 = Relay_Channel(0, self)
        self.relay1 = Relay_Channel(1, self)
        self.relay2 = Relay_Channel(2, self)
        self.relay3 = Relay_Channel(3, self)

        self.ui = uic.loadUi("RC.ui")

        self.ui.label_ch1_3.setStyleSheet("color: red")
        self.ui.label_ch2_3.setStyleSheet("color: red")
        self.ui.label_ch3_3.setStyleSheet("color: red")
        self.ui.label_ch4_3.setStyleSheet("color: red")

        self.ui.label_ch1_3.setText("Disconnected")
        self.ui.label_ch2_3.setText("Disconnected")
        self.ui.label_ch3_3.setText("Disconnected")
        self.ui.label_ch4_3.setText("Disconnected")

        self.ui.pushButton_ch1.setStyleSheet("background-color: red")
        self.ui.pushButton_ch2.setStyleSheet("background-color: red")
        self.ui.pushButton_ch3.setStyleSheet("background-color: red")
        self.ui.pushButton_ch4.setStyleSheet("background-color: red")

        self.ui.pushButton_ch1.clicked.connect(self.clickMethod1)
        self.ui.pushButton_ch2.clicked.connect(self.clickMethod2)
        self.ui.pushButton_ch3.clicked.connect(self.clickMethod3)
        self.ui.pushButton_ch4.clicked.connect(self.clickMethod4)

        while(not self.relay0.onDigitalOutput_Connect()) :
            if QtWidgets.QMessageBox.Yes == QtWidgets.QMessageBox.question(self,"Error","Relay No Connection\nretry?",QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No) :
                pass
            else :
                sys.exit()

        while(not self.relay1.onDigitalOutput_Connect()) :
            if QtWidgets.QMessageBox.Yes == QtWidgets.QMessageBox.question(self,"Error","Relay No Connection\nretry?",QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No) :
                pass
            else :
                sys.exit()

        while(not self.relay2.onDigitalOutput_Connect()) :
            if QtWidgets.QMessageBox.Yes == QtWidgets.QMessageBox.question(self,"Error","Relay No Connection\nretry?",QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No) :
                pass
            else :
                sys.exit()

        while(not self.relay3.onDigitalOutput_Connect()) :
            if QtWidgets.QMessageBox.Yes == QtWidgets.QMessageBox.question(self,"Error","Relay No Connection\nretry?",QtWidgets.QMessageBox.Yes, QtWidgets.QMessageBox.No) :
                pass
            else :
                sys.exit()

        self.ui.show()

    def clickMethod1(self) :
        if(self.ui.label_ch1_3.text() != "Disconnected") : 
            if(self.ui.pushButton_ch1.text() == "ON") :
                self.relay0.onDigitalOutput_Off()
                self.ui.pushButton_ch1.setStyleSheet("background-color: red")
                self.ui.pushButton_ch1.setText("OFF")
            else :
                self.relay0.onDigitalOutput_On()
                self.ui.pushButton_ch1.setStyleSheet("background-color: green")
                self.ui.pushButton_ch1.setText("ON")
        else :
            QtWidgets.QMessageBox.about(self,"Error","Relay is not connected")

    def clickMethod2(self) :
        if(self.ui.label_ch2_3.text() != "Disconnected") : 
            if(self.ui.pushButton_ch2.text() == "ON") :
                self.relay1.onDigitalOutput_Off()
                self.ui.pushButton_ch2.setStyleSheet("background-color: red")
                self.ui.pushButton_ch2.setText("OFF")
            else :
                self.relay1.onDigitalOutput_On()
                self.ui.pushButton_ch2.setStyleSheet("background-color: green")
                self.ui.pushButton_ch2.setText("ON")
        else :
            QtWidgets.QMessageBox.about(self,"Error","Relay is not connected")

    def clickMethod3(self) :
        if(self.ui.label_ch3_3.text() != "Disconnected") : 
            if(self.ui.pushButton_ch3.text() == "ON") :
                self.relay2.onDigitalOutput_Off()
                self.ui.pushButton_ch3.setStyleSheet("background-color: red")
                self.ui.pushButton_ch3.setText("OFF")
            else :
                self.relay2.onDigitalOutput_On()
                self.ui.pushButton_ch3.setStyleSheet("background-color: green")
                self.ui.pushButton_ch3.setText("ON")
        else :
            QtWidgets.QMessageBox.about(self,"Error","Relay is not connected")

    def clickMethod4(self) :
        if(self.ui.label_ch4_3.text() != "Disconnected") : 
            if(self.ui.pushButton_ch4.text() == "ON") :
                self.relay3.onDigitalOutput_Off()
                self.ui.pushButton_ch4.setStyleSheet("background-color: red")
                self.ui.pushButton_ch4.setText("OFF")
            else :
                self.relay3.onDigitalOutput_On()
                self.ui.pushButton_ch4.setStyleSheet("background-color: green")
                self.ui.pushButton_ch4.setText("ON")
        else :
            QtWidgets.QMessageBox.about(self,"Error","Relay is not connected")

    def attached(self, ch) :
        if(ch == 0) :
            self.relay0.onDigitalOutput_Off()
            self.ui.label_ch1_3.setStyleSheet("color: green")
            self.ui.label_ch1_3.setText("Connected")
            self.ui.pushButton_ch1.setStyleSheet("background-color: red")
            self.ui.pushButton_ch1.setText("OFF")

        elif(ch == 1) :
            self.relay1.onDigitalOutput_Off()
            self.ui.label_ch2_3.setStyleSheet("color: green")
            self.ui.label_ch2_3.setText("Connected")
            self.ui.pushButton_ch2.setStyleSheet("background-color: red")
            self.ui.pushButton_ch2.setText("OFF")

        elif(ch == 2) :
            self.relay2.onDigitalOutput_Off()
            self.ui.label_ch3_3.setStyleSheet("color: green")
            self.ui.label_ch3_3.setText("Connected")
            self.ui.pushButton_ch3.setStyleSheet("background-color: red")
            self.ui.pushButton_ch3.setText("OFF")

        elif(ch == 3) :
            self.relay3.onDigitalOutput_Off()
            self.ui.label_ch4_3.setStyleSheet("color: green")
            self.ui.label_ch4_3.setText("Connected")
            self.ui.pushButton_ch4.setStyleSheet("background-color: red")
            self.ui.pushButton_ch4.setText("OFF")

    def detached(self, ch) :
        if(ch == 0) :
            self.ui.label_ch1_3.setStyleSheet("color: red")
            self.ui.label_ch1_3.setText("Disconnected")
            self.ui.pushButton_ch1.setStyleSheet("background-color: red")
            self.ui.pushButton_ch1.setText("OFF")

        elif(ch == 1) :
            self.ui.label_ch2_3.setStyleSheet("color: red")
            self.ui.label_ch2_3.setText("Disconnected")
            self.ui.pushButton_ch2.setStyleSheet("background-color: red")
            self.ui.pushButton_ch2.setText("OFF")

        elif(ch == 2) :
            self.ui.label_ch3_3.setStyleSheet("color: red")
            self.ui.label_ch3_3.setText("Disconnected")
            self.ui.pushButton_ch3.setStyleSheet("background-color: red")
            self.ui.pushButton_ch3.setText("OFF")

        elif(ch == 3) :
            self.ui.label_ch4_3.setStyleSheet("color: red")
            self.ui.label_ch4_3.setText("Disconnected")
            self.ui.pushButton_ch4.setStyleSheet("background-color: red")
            self.ui.pushButton_ch4.setText("OFF")

 
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())