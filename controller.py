from view import App
from model import Script
from db_controller import DBController
from time import sleep
import jinja2
import webbrowser


class Controller(object):
    scriptView = App(create_cmd=None, load_cmd=None, play_cmd=None)
    db_ctrl = None
    saved = None
    textList = []
    all_scripts_list = []

    def insert(self):
        self.saved = self.scriptView.read()
        self.db_ctrl.save_script(self.saved)
        self.scriptView.create_script(self.saved)
        self.textList.append(self.saved)

    def load(self):
        scripts = self.db_ctrl.all_scripts()
        self.scriptView.load_scripts(scripts)
        self.all_scripts_list.append(scripts)

        print(scripts)

    def play(self):
        self.saved = script = self.scriptView.read()
        self.scriptView.play(s)
        """_list = self.db_ctrl.all_scripts()

        for line in _list:
            script = Script(line[0], line[1], line[2], line[3], line[4])
            self.scriptView.read()
            self.textList.append(script)

            print(self.textList)"""

    def exec(self):
        self.db_ctrl = DBController()
        self.scriptView = App(self.insert, self.load(), self.play())

        self.scriptView.exec()
