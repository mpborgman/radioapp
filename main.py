import json
import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton
from radio import Ui_MainForm

FILE_PATH = "resources/settings.json"


class MainForm(QDialog, Ui_MainForm):
    DAB = True
    program_channel = False
    current_channel = 0
    retained_memory = None
    input_stylesheet_active = "color: rgb(255, 255, 255);\n"\
                              "font: 18pt \"Gill Sans\";\n"\
                              "text-align: left;"
    input_stylesheet_inactive = "color: rgb(140, 140, 140);\n"\
                                "font: 18pt \"Gill Sans\";\n"\
                                "text-align: left;"
    program_stylesheet_active = "color: rgb(255, 255, 255);\n"\
                                "font: 100pt \"Gill Sans\";\n"\
                                "text-align: center;"
    program_stylesheet_inactive = "color: rgb(140, 140, 140);\n"\
                                  "font: 100pt \"Gill Sans\";\n"\
                                  "text-align: center;"
    memory_stylesheet_active = "color: rgb(255, 215, 0);\n"\
                               "font: 18pt \"Gill Sans\";"\
                               "text-align: left;"
    memory_stylesheet_inactive = "color: rgb(140, 140, 140);\n"\
                                 "font: 18pt \"Gill Sans\";"\
                                 "text-align: left;"

    def __init__(self):
        super(MainForm, self).__init__()

        # Set up the user interface from Designer.
        self.setupUi(self)

        # Make some local modifications.
        self.slider_volume.setVisible(False)

        # Connect up the buttons.
        self.button_stop.clicked.connect(self.stop)
        self.button_add.clicked.connect(self.add_channel)
        self.button_previous.clicked.connect(self.change_channel)
        self.button_next.clicked.connect(self.change_channel)
        self.button_play.clicked.connect(self.play)
        self.button_volume.clicked.connect(self.show_slider)
        self.button_input_dab.clicked.connect(self.input_dab)
        self.button_input_fm.clicked.connect(self.input_fm)
        self.button_p1.clicked.connect(self.update_channel)
        self.button_p2.clicked.connect(self.update_channel)
        self.button_p3.clicked.connect(self.update_channel)
        self.button_p4.clicked.connect(self.update_channel)
        self.button_p5.clicked.connect(self.update_channel)
        self.button_p6.clicked.connect(self.update_channel)
        self.slider_volume.valueChanged.connect(self.volume_change)

        # ToDo: Retrieve settings from memory and load GUI accordingly
        self.initialize_memory()
        self.initialize_dashboard()
        self.update_activity()

    def initialize_memory(self):
        try:
            with open(FILE_PATH, "r") as f:
                self.retained_memory = json.load(f)
            self.current_channel = self.retained_memory["current_channel"]
            self.DAB = self.retained_memory["current_input"] == "DAB"
        except FileNotFoundError as exc:
            print(f"No initialization can be done. Settings file can't be found! {exc}")
        except json.decoder.JSONDecodeError as exc:
            print(f"No initialization can be done. Settings file is corrupt! {exc}")

    def initialize_dashboard(self):
        _translate = QtCore.QCoreApplication.translate
        self.set_input_style()
        self.set_memory_buttons()
        self.label_frequency.setText(_translate("MainForm", self.current_channel["frequency"]))
        self.label_info.setText(_translate("MainForm", ""))

    def update_activity(self):
        # ToDo: Activate last chosen channel to be active
        print(f"Active channel set!")

    @staticmethod
    def set_input(input_type: str):
        if input_type == "dab":
            # stream from DAB+ radio
            print("DAB Selected!")
        else:
            # stream from FM radio
            print("FM Selected!")

    def stop(self):
        app.exit()

    def add_channel(self):
        self.program_channel = True
        self.button_add.setStyleSheet(self.program_stylesheet_active)

    def change_channel(self):
        forward = True if self.sender().objectName() == "button_next" else False
        # Search for channel
        if self.DAB:
            self.change_channel_DAB(forward)
            print(f"Searching for next DAB channel: forward: {forward}")
        else:
            self.change_channel_FM(forward)
            print(f"Searching for next FM channel: forward: {forward}")

    def play(self):
        print(f"Playing some music now")

    def show_slider(self):
        self.slider_volume.setVisible(True)

    def input_dab(self):
        self.DAB = True
        self.set_input("dab")
        self.set_input_style()

    def input_fm(self):
        self.DAB = False
        self.set_input("fm")
        self.set_input_style()

    def change_channel_DAB(self, forward: bool):
        print(f"Search next DAB+ channel")

    def change_channel_FM(self, forward: bool):
        print(f"Search next FM channel")

    def update_channel(self):
        pos = int(self.sender().objectName()[-1])
        mem_start = 1 if self.DAB else 7
        if self.program_channel:
            self.retained_memory["channel_mem"][str(pos + mem_start)] = self.current_channel
            self.program_channel = False
            self.button_add.setStyleSheet(self.program_stylesheet_inactive)

        self.current_channel = self.retained_memory["channel_mem"][str(pos + mem_start)]
        self.retained_memory["current_channel"] = self.current_channel
        self.set_memory_style(pos)

    def volume_change(self):
        # ToDo: Adjust volume
        self.slider_volume.setVisible(True)
        print(f"Volume changed: {self.slider_volume.value()}")

    def set_memory_buttons(self):
        mem_start = 1 if self.DAB else 7
        _translate = QtCore.QCoreApplication.translate
        for i in range(1, 7):
            button_p = self.findChild(QPushButton, "button_p" + str(i))
            name = self.retained_memory["channel_mem"][str(i + mem_start)]["name"] or ""
            button_p.setText(_translate("MainForm", f"P{i}: {name}"))
            if self.current_channel == self.retained_memory["channel_mem"][str(i + mem_start)]:
                pos = i

        self.set_memory_style(pos)

    def set_input_style(self):
        if self.DAB:
            self.button_input_dab.setStyleSheet(self.input_stylesheet_active)
            self.button_input_fm.setStyleSheet(self.input_stylesheet_inactive)
        else:
            self.button_input_dab.setStyleSheet(self.input_stylesheet_inactive)
            self.button_input_fm.setStyleSheet(self.input_stylesheet_active)

    def set_memory_style(self, pos: int):
        for i in range(1, 7):
            button_p = self.findChild(QPushButton, "button_p" + str(i))
            button_p.setStyleSheet(self.memory_stylesheet_inactive)
        button_p = self.findChild(QPushButton, "button_p" + str(pos))
        button_p.setStyleSheet(self.memory_stylesheet_active)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainForm()
    widget.show()
    sys.exit(app.exec_())
