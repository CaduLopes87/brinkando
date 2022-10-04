import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="BrinkAnDo v0.0.2")
        self.set_default_size(1280, 720)

        # base grid for layout
        self.grid = Gtk.Grid.new()
        self.grid.set_row_spacing(4)
        self.grid.set_column_spacing(4)

        # a grid which will hold the selected commands and other items
        # currently meant to be an item of each one of the menu buttons
        self.cmdGrid = Gtk.Grid.new()
        self.cmdGrid.set_row_spacing(4)
        self.cmdGrid.set_column_spacing(4)

        self.grid.attach(self.cmdGrid, 0, 0, 10, 2)

        # the box which will hold the selected commands
        self.cmdBox = Gtk.FlowBox()
        self.cmdBox.set_valign(Gtk.Align.START)
        self.cmdBox.set_max_children_per_line(10)
        self.cmdBox.set_min_children_per_line(10)
        self.cmdBox.set_selection_mode(Gtk.SelectionMode.NONE)

        # a cute little car icon
        cmdCarIcon = Gtk.Image.new_from_file("assets/little-car.png")
        self.cmdGrid.attach(cmdCarIcon, 0, 0, 1, 2)

        self.cmdGrid.attach_next_to(self.cmdBox, cmdCarIcon, 1, 9, 2)

        # the box which will hold the command options (buttons)
        self.cmdFlowbox = Gtk.FlowBox()
        self.cmdFlowbox.set_valign(Gtk.Align.END)
        self.cmdFlowbox.set_max_children_per_line(2)
        self.cmdFlowbox.set_min_children_per_line(2)
        self.cmdFlowbox.set_selection_mode(Gtk.SelectionMode.NONE)

        # each of the command buttons
        self.leftBttn = Gtk.Button()
        self.leftBttn.set_image(Gtk.Image.new_from_file('assets/turn-left-arrow.png'))
        self.cmdFlowbox.add(self.leftBttn)

        self.rightBttn = Gtk.Button()
        self.rightBttn.set_image(Gtk.Image.new_from_file('assets/turn-right-arrow.png'))
        self.cmdFlowbox.add(self.rightBttn)

        self.uTurnBttn = Gtk.Button()
        self.uTurnBttn.set_image(Gtk.Image.new_from_file('assets/u-turn-arrow.png'))
        self.cmdFlowbox.add(self.uTurnBttn)

        self.forwardBttn = Gtk.Button()
        self.forwardBttn.set_image(Gtk.Image.new_from_file('assets/forward-arrow.png'))
        self.cmdFlowbox.add(self.forwardBttn)

        # fill the cmdBox with drop-down menus
        for i in range(20):
            self.cmdSelect = Gtk.MenuButton()

            menu = Gtk.Menu()
            menu.attach(self.cmdFlowbox, 0, 0, 0, 0)

            self.cmdSelect.set_popup(menu)

            self.cmdBox.add(self.cmdSelect)

        self.add(self.grid)       

win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

# SOME CODE FORM VERSION 0.0.1
## YOU SHOULD NOT RUN THIS CODE AS IT IS, SINCE IT'S CURRENTLY MESSY.
### USE IT AS INSPIRATION FOR A DIFFERENT LAYOUT IDEA.

# self.separator = Gtk.Separator.new(0)
        # self.grid.attach_next_to(self.separator, self.cmdGrid, 3, 10, 1)

        # self.bttnsBox = Gtk.FlowBox()
        # self.bttnsBox.set_valign(Gtk.Align.END)
        # self.bttnsBox.set_max_children_per_line(2)
        # self.bttnsBox.set_min_children_per_line(2)
        # self.bttnsBox.set_selection_mode(Gtk.SelectionMode.NONE)
        # self.grid.attach_next_to(self.bttnsBox, self.separator, 3, 10, 1)

        # self.startBttn = Gtk.Button(label="VAI!")
        # self.startBttn.connect("clicked", self.on_startBttn_clicked)
        # self.grid.attach_next_to(self.startBttn, self.bttnsBox, 1, 1, 1)

        # def on_leftBttn_clicked(self, widget):
    #     print("ESQUERDA")

    #     # if (self.cmdBox.get_child_at_index(19)):
    #     #     return


    #     for i in range(20):
    #         print(type(self.cmdBox.get_child_at_index(i)))
    #         if (type(self.cmdBox.get_child_at_index(i)) == Gtk.Button):
    #             self.cmdBox.insert(Gtk.Image.new_from_file('assets/turn-left-arrow.png'))
                
 
    #     self.grid.show_all()
            
    # def on_rightBttn_clicked(self, widget):
    #     print("DIREITA")

    #     if (self.cmdBox.get_child_at_index(19)):
    #         return

    #     self.cmdBox.add(Gtk.Image.new_from_file('assets/turn-right-arrow.png'))
    #     self.grid.show_all()

    # def on_uTurnBttn_clicked(self, widget):
    #     print("MEIA-VOLTA")

    #     if (self.cmdBox.get_child_at_index(19)):
    #         return

    #     self.cmdBox.add(Gtk.Image.new_from_file('assets/u-turn-arrow.png'))
    #     self.grid.show_all()

    # def on_forwardBttn_clicked(self, widget):
    #     print("PARA FRENTE")

    #     if (self.cmdBox.get_child_at_index(19)):
    #         return

    #     self.cmdBox.add(Gtk.Image.new_from_file('assets/forward-arrow.png'))
    #     self.grid.show_all()

    # def on_startBttn_clicked(self, widget):
    #     print("Iniciando...")
    #     self.startDialog = Gtk.MessageDialog()
    #     self.startDialog.set_markup("Confira o resultado...")
    #     self.startDialog.show()