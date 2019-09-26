from view import App
from model import Script
from database_controller import DB_Controller


class Controller(object):
    scriptView = None
    db_ctrl = None
    written = None
    textList = []

    def insert(self):
        self.written = self.scriptView.read()
        self.db_ctrl.save(self.written)
        self.scriptView.create_script(self.written)
        self.textList.append(self.written)

    def retrieve(self):
        _list = self.db_ctrl.showScript()

        for line in _list:
            script = Script(line[0], line[1], line[2])
            self.scriptView.save(script)
            self.textList.append(script)

    def run(self):
        self.db_ctrl = DB_Controller()
        self.scriptView = App(self.insert, self.retrieve)

        self.scriptView.ru
