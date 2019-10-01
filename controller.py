from view import App
from model import Script
from db_controller import DBController
from time import sleep
import jinja2
import webbrowser


class Controller(object):
    scriptView = None
    db_ctrl = None
    saved = None
    textList = []

    def insert(self):
        self.saved = self.scriptView.read()
        self.db_ctrl.save_script(self.saved)
        self.scriptView.create_script(self.saved)
        self.textList.append(self.saved)

    def load(self):
        _list = self.db_ctrl.return_script_as_list()

        with open('./template.html', 'r') as file:
            script_file = file.read().replace('\n', '')

        for line in _list:
            script = Script(line[0], line[1], line[2], line[3], line[4])

            jinja2.Template(script_file).render(
                    story=script.story,
                    scene=script.scene,
                    character=script.character,
                    line=script.line,
                    text_color=script.text_color
            )

        return webbrowser.open('file:///home/jg/python-script-app/template.html')

    def play(self):
        _list = self.db_ctrl.return_script_as_list()

        for line in _list:
            script = Script(line[0], line[1], line[2], line[3], line[4])
            self.scriptView.read()
            self.textList.append(script)

            print(self.textList); sleep(2.0)

    def exec(self):
        self.db_ctrl = DBController()
        self.scriptView = App(self.insert, self.load(), self.play())

        self.scriptView.exec()
