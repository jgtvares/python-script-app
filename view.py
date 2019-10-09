from tkinter import Tk, Label, Entry, Button, Listbox, END
from model import Script
import webbrowser


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
    all_scriptsListBox = None

    # Labels
    storyLabel = None
    sceneLabel = None
    lineLabel = None
    text_colorLabel = None
    characterLabel = None
    textListBoxLabel = None
    all_scriptsListBoxLabel = None

    # Buttons
    createButton = None
    loadButton = None
    playButton = None

    def read(self):
        story = self.storyEntry.get()
        scene = self.sceneEntry.get()
        line = self.lineEntry.get()
        username = self.characterEntry.get()
        text_color = self.text_colorEntry.get()

        script = Script(story, scene, line, username, text_color)

        return script

    def create_script(self, script):
        self.textListBox.insert(END, script)

    def load_scripts(self, scripts):
        for item in enumerate(scripts):
            sep = item.__str__()
            _sep = item[1][0]
            self.all_scriptsListBox.insert(END, _sep)

    def play(self, script):
        story = script.__str__()
        scene = script.return_scene()
        line = script.return_line()
        character = script.return_character()
        text_color = script.return_text_color()
        color = str(text_color)

        html = '<html><body><h2>' + str(story) + '</h2><br>' + '<p><strong>Scene:</strong> ' + str(scene) + '</p><br>' + '<p><strong>Character:</strong> ' + str(character) + '</p><br>'  + '<p><strong>Line: </strong><a style="color: ' + color + '";>' + str(line) + '</a></p><br>'
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'

        with open('./template.html', 'w') as f:
            page = f.write(html)

        webbrowser.get(chrome_path).open('./template.html')

    def __init__(self, create_cmd, load_cmd, play_cmd) -> None:
        super().__init__()
        self.storyLabel = Label(master=self.window, text='Story:')
        self.storyEntry = Entry(master=self.window, width=20)

        self.sceneLabel = Label(master=self.window, text='Scene:')
        self.sceneEntry = Entry(master=self.window, width=20)

        self.characterLabel = Label(master=self.window, text='Character:')
        self.characterEntry = Entry(master=self.window, width=20)

        self.lineLabel = Label(master=self.window, text='Line:')
        self.lineEntry = Entry(master=self.window, width=20)

        self.text_colorLabel = Label(master=self.window, text='Text color:')
        self.text_colorEntry = Entry(master=self.window, width=10)

        self.createButton = Button(master=self.window, text='Create Script', command=create_cmd)
        self.loadButton = Button(master=self.window, text='Load Scripts', command=load_cmd)
        self.playButton = Button(master=self.window, text='Play Story', command=play_cmd)

        self.textListBoxLabel = Label(master=self.window, text='Recently Created Scripts')
        self.textListBox = Listbox(master=self.window, width=50)

        self.all_scriptsListBoxLabel = Label(master=self.window, text='Loaded From Database')
        self.all_scriptsListBox = Listbox(master=self.window, width=50)

        self.storyLabel.grid(row=1, column=1)
        self.storyEntry.grid(row=1, column=2)

        self.sceneLabel.grid(row=2, column=1)
        self.sceneEntry.grid(row=2, column=2)

        self.characterLabel.grid(row=3, column=1)
        self.characterEntry.grid(row=3, column=2)

        self.lineLabel.grid(row=4, column=1)
        self.lineEntry.grid(row=4, column=2)

        self.text_colorLabel.grid(row=5, column=1)
        self.text_colorEntry.grid(row=5, column=2)

        self.createButton.grid(row=6, column=1)
        self.loadButton.grid(row=6, column=2)
        self.playButton.grid(row=6, column=3)

        self.textListBoxLabel.grid(row=8, column=1)
        self.textListBox.grid(row=9, column=1, columnspan=3)

        self.all_scriptsListBoxLabel.grid(row=10, column=1)
        self.all_scriptsListBox.grid(row=11, column=1, columnspan=3)

    def exec(self):
        self.window.mainloop()
