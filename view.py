from tkinter import Tk,Label,Entry,Button, Listbox, END
from model import Script

class App(object):
    window = Tk()

    # Entries
    storyEntry = None
    sceneEntry = None
    lineEntry = None
    characterEntry = None
    text_colorEntry = None

    # List Box
    textListBox = None

    # Labels
    storyLabel = None
    sceneLabel = None
    lineLabel = None
    text_colorLabel = None
    characterLabel = None

    # Buttons
    playButton = None
    loadButton = None




    def read(self):
        story = self.storyEntry.get()
        scene = self.sceneEntry.get()
        line = self.lineEntry.get()
        username = self.usernameEntry.get()
        text_color = self.text_colorEntry.get()

        script = Script(story, scene, line, username, color)

        return script

    def create_script(self, script):
        self.textListBox.insert(END, script)

    def __init__(self, insert_cmd, load_cmd):
        super().__init__()
        self.storyLabel = Label(master=self.window)
        self.sceneLabel = Label(master=self.window)
        self.text_colorLabel = Label(master=self.window)
        self.characterLabel = Label(master=self.window)
