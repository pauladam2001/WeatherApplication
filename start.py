from userinterface.graphicalUserInterface import GUI
from controller.controller import Controller


controller = Controller()
gui = GUI(controller)
gui.start()
