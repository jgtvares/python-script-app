from macpath import norm_error

from view import App
from model import Script
from db_controller import DBController

class Controller(object):
    scriptView = None # App(create_cmd=None, load_cmd=None, play_cmd=None)
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

    def play(self):
        self.saved = self.scriptView.read()
        story = self.saved.__str__()
        self.db_ctrl.read_script(story)
        self.scriptView.play(self.saved)

    def exec(self):
        self.db_ctrl = DBController()
        self.scriptView = App(self.insert, self.load, self.play)

        self.scriptView.exec()
