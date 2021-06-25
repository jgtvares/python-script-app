from view import App
from model import Script
from db_controller import DBController

class Controller(object):
    scriptView = None
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

    def read_and_play(self):
        self.saved = self.scriptView.read()
        self.scriptView.read_and_play(self.saved)

    def load_and_play(self):
        scripts = self.db_ctrl.all_scripts()
        self.scriptView.load_and_play(scripts)

    def exec(self):
        self.db_ctrl = DBController()
        self.scriptView = App(self.insert, self.load, self.read_and_play, self.load_and_play)

        self.scriptView.exec()
