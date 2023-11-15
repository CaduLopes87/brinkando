import RPi.GPIO as gpio
import serial

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

# serial port data to comunicate with arduino
arduino = None
serial_port = '/dev/ttyUSB0'
baud_rate = 9600

# connect to arduino
arduino = serial.Serial(serial_port, baud_rate)

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="BrinkAnDo v0.0.3")
        self.set_default_size(1280, 720)
        
        # serial port datas to comunicate with arduino
        #self.arduino = None
        #self.serial_port = '/dev/ttyUSB0'
        #self.baud_rate = 9600

        # base grid for layout
        self.grid = Gtk.Grid.new()
        self.grid.set_row_spacing(4)
        self.grid.set_column_spacing(4)

        # a cute little car icon
        cmdCarIcon = Gtk.Image.new_from_file("assets/little-car.png")
        self.grid.attach(cmdCarIcon, 0, 0, 1, 1)

        # a grid for the command options: left, right, forward and turn around
        cmdOpts = Gtk.Grid.new()
        cmdOpts.set_row_spacing(4)
        cmdOpts.set_column_spacing(4)

        # creating a button for each command, with cute icons
        leftBttn = Gtk.Button()
        leftBttn.set_image(
                Gtk.Image.new_from_file("assets/turn-left-arrow.png"))
        leftBttn.connect("clicked", self.on_leftBttn_clicked)
        cmdOpts.attach(leftBttn, 0, 0, 1, 1)

        rightBttn = Gtk.Button()
        rightBttn.set_image(
                Gtk.Image.new_from_file("assets/turn-right-arrow.png"))
        rightBttn.connect("clicked", self.on_rightBttn_clicked)
        cmdOpts.attach(rightBttn, 1, 0, 1, 1)

        forwardBttn = Gtk.Button()
        forwardBttn.set_image(
                Gtk.Image.new_from_file("assets/forward-arrow.png"))
        forwardBttn.connect("clicked", self.on_forwardBttn_clicked)
        cmdOpts.attach(forwardBttn, 0, 1, 1, 1)

        uTurnBttn = Gtk.Button()
        uTurnBttn.set_image(
                Gtk.Image.new_from_file("assets/u-turn-arrow.png"))
        uTurnBttn.connect("clicked", self.on_uTurnBttn_clicked)
        cmdOpts.attach(uTurnBttn, 1, 1, 1, 1)

        # attaching the command options grid to the base grid
        self.grid.attach(cmdOpts, 1, 0, 1, 1)

        # creating a start button, to send the selected commands
        startBttn = Gtk.Button(label="VAI!")
        startBttn.connect("clicked", self.on_startBttn_clicked)

        self.grid.attach(startBttn, 2, 0, 1, 1)

        # creating an input box to hold the selected commands
        self.inputBox = Gtk.FlowBox()
        self.inputBox.set_valign(Gtk.Align.START)
        self.inputBox.set_max_children_per_line(10)
        self.inputBox.set_min_children_per_line(10)
        self.inputBox.set_selection_mode(Gtk.SelectionMode.NONE)

        # attaching the input box to the base grid
        self.grid.attach(self.inputBox, 0, 1, 3, 1)

        # adding the base grid to the window
        self.add(self.grid)
    
    # function to save the state of clicked buttons
    button_Position = []  

    def get_Bttn_position(self, Bttn_Number):
        self.button_Position.append(Bttn_Number)
        print(self.button_Position)

    # functions to add the selected commands to the input box
    def on_leftBttn_clicked(self, widget):
        self.inputBox.add(Gtk.Image
                          .new_from_file("assets/turn-left-arrow.png"))
        self.grid.show_all()
        # pass 1 for left direction
        self.get_Bttn_position(1) 

    def on_rightBttn_clicked(self, widget):
        self.inputBox.add(Gtk.Image
                          .new_from_file("assets/turn-right-arrow.png"))
        self.grid.show_all()
        # pass 2 for right direction
        self.get_Bttn_position(2)


    def on_forwardBttn_clicked(self, widget):
        self.inputBox.add(Gtk.Image
                          .new_from_file("assets/forward-arrow.png"))
        self.grid.show_all()
        # pass 3 for forward direction
        self.get_Bttn_position(3)


    def on_uTurnBttn_clicked(self, widget):
        self.inputBox.add(Gtk.Image
                          .new_from_file("assets/u-turn-arrow.png"))
        self.grid.show_all()
        # pass 4 for turn direction
        self.get_Bttn_position(4)
        
    #Function to close connection
    def close_connection(self):
        if self.arduino:
            self.arduino.close()
    
    #Function to convert the numbers array in a string
    def convert_to_byte(self, num_array):
        byte_numbers = []
        
        for number in num_array:
            byte_value = number.to_bytes(1, byteorder='big')
            byte_numbers.append(byte_value)
        
        return byte_numbers
        
    #Function to stream data to the car bot
    def send_message(self):
        message = self.convert_to_byte(self.button_Position)
        
        for byte in message:
            if arduino:
                try:
                    #message = self.button_Position
                    #message = b'1'
                    #arduino.write(b'1')
                    arduino.write(byte)
                    print("Sent Byte: ", byte)
                except serial.SerialException as e:
                    print(f"Fail to send mesage: {e}")
                    
        print('Mensagem enviada: ', self.button_Position)
        self.button_Position = []
        
    # function to display a message when start button is pressed
    def on_startBttn_clicked(self, widget):
        self.startDialog = Gtk.MessageDialog()
        self.startDialog.set_markup("Acelerando...")
        self.startDialog.show()
        # pass 5 to start move
        self.get_Bttn_position(5)
        self.send_message()

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()