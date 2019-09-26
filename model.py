class Script(object):
    _story = None
    _scene = None
    _line = None
    _character = None
    _text_color = None

    def __init__(self, story, scene, line, character, text_color) -> None:
        super().__init__()
        self._story = story
        self._scene = scene
        self._line = line
        self._character = character
        self._text_color = text_color

    def __str__(self) -> str:
        return self._story

    def show_script(self):
        text = self._character + ': ' + self._line
        return text
