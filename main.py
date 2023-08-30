from rpi_rf import RFDevice
import RPi.GPIO as gpio

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

button_Position = []

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="BrinkAnDo v0.0.3")
        self.set_default_size(1280, 720)

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

    def get_Bttn_position(self, Bttn_Number):
        self.button_Position.append(Bttn_Number)
        print(self.button_Position)

    # functions to add the selected commands to the input box
    def on_leftBttn_clicked(self, widget):
        self.inputBox.add(Gtk.Image
                          .new_from_file("assets/turn-left-arrow.png"))
        self.grid.show_all()
        self.get_Bttn_position(0)

    def on_rightBttn_clicked(self, widget):
        self.inputBox.add(Gtk.Image
                          .new_from_file("assets/turn-right-arrow.png"))
        self.grid.show_all()
        self.get_Bttn_position(1)


    def on_forwardBttn_clicked(self, widget):
        self.inputBox.add(Gtk.Image
                          .new_from_file("assets/forward-arrow.png"))
        self.grid.show_all()
        self.get_Bttn_position(2)


    def on_uTurnBttn_clicked(self, widget):
        self.inputBox.add(Gtk.Image
                          .new_from_file("assets/u-turn-arrow.png"))
        self.grid.show_all()
        self.get_Bttn_position(3)

    # function to display a message when start button is pressed
    # in the future, this might be used to stream data to the car bot
    def on_startBttn_clicked(self, widget):
        self.startDialog = Gtk.MessageDialog()
        self.startDialog.set_markup("Acelerando...")
        self.startDialog.show()
        self.get_Bttn_position(4)

gpio.setmode(gpio.BCM)

rfDevice = RFDevice(4)
rfDevice.enable_tx()
rfDevice.tx_repeat = 10

rfDevice.tx_code(button_Position)
rfDevice.cleanup()

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()