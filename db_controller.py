import sqlite3
from model import Script


class DBController:
    db_name = 'script.db'
    connection = None
    table = """CREATE TABLE SCRIPT(
                            STORY TEXT,
                            SCENE TEXT,
                            CHARACTER TEXT,
                            LINE TEXT,
                            TEXT_COLOR TEXT)"""

    insert = "INSERT INTO SCRIPT(STORY, SCENE, CHARACTER, LINE, TEXT_COLOR) VALUES(?,?,?,?,?)"

    select = "SELECT * FROM SCRIPT"

    select_where = "SELECT * FROM SCRIPT WHERE STORY = '?'"

    def __init__(self) -> None:
        super().__init__()
        self.connection = sqlite3.connect(self.db_name)
        cursor = self.connection.cursor()

        try:
            cursor.execute(self.table)
            self.connection.commit()
        except:
            print('Database already created! Creation ignored.')

        cursor.close()

    def save_script(self, script):
        register = (script.story, script.scene, script.line, script.character, script.text_color)
        cursor = self.connection.cursor()
        cursor.execute(self.insert, register)
        self.connection.commit()
        cursor.close()

    def all_scripts(self):
        cursor = self.connection.cursor()
        cursor.execute(self.select)
        script_list = cursor.fetchall()
        self.connection.commit()
        cursor.close()

        return script_list
    
    def read_script(self, story):
        cursor = self.connection.cursor()
        cursor.execute(self.select_where)
        script = cursor.fetchall()
        self.connection.commit()
        cursor.close()

        return script
