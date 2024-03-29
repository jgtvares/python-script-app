class Script(object):
    def __init__(self, story, scene, line, character, text_color) -> None:
        super().__init__()
        self.story = story
        self.scene = scene
        self.line = line
        self.character = character
        self.text_color = text_color

    def __str__(self) -> str:
        return self.story

    def return_scene(self):
        return self.scene

    def return_line(self):
        return self.line

    def return_character(self):
        return self.character

    def return_text_color(self):
        return self.text_color

    def file(self):
        line = self.story + ', ' + self.scene + ', ' + self.character + ', ' + self.line
        return line

    def show_script(self):
        text = self.story + '\n' + self.scene + ' - ' + self.character + ': ' + self.line
        return text
