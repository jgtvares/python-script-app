# Script App

This is a **python** app, based on the *MVC* concept that creates a script, kind of like a movie script.

It uses a simple **Tkinter** interface window, that grabs user input to make the script structure.

This is a college project and it's far from perfect, but it meets the functionality expectations!
    I'll probably keep working and tweaking it for a while!

I've made this public 'cause it could help the community somehow, and you guys (*the internet*) are free to use!

Hope it helps someone, after all...we're all eternal students!

## Script Sctructure

- Story
- Scene
- Character
- Line

## Requirements

1. **Tkinter**

If you intend to run it from VS Code you'll need to install **Tkinter**.

It should come with Python3.* already. But I was using **Python 3.7** in this project
    and somehow, VS Code was not finding *tkinter* module. Anyway, make sure you have it!

- Installing on Fedora (*python3*):

```bash
    sudo dnf install python3-tk
```

- Installing on Ubuntu (*python3*):

```bash
sudo apt-get install python3-tk
```

2. **Set Chrome as Default Browser**

The app opens a **HTML** page showing the full scructure of a selected script.

**Internet Explorer** doesn't handle it very well and sometimes it might show a blank page (*depending on the version you're using*).

So, to be certain that everything will work smoothly, I advise you to set Chrome as your default browser!

If you set Chrome for default but the app keeps opening IE, you'll need to tell Python's **webbrowser** method where the *chrome* executable is.

- **Windows**:

```python
page = './page.html' # HTML file in the working directory

chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s' # path to Chrome

webbrowser.get(chrome_path).open(page) # opens the HTML file with Chrome
```

*If this is not working for you, try 'Program Files (x86)' instead*

- **Mac OS**:

```python
page = './page.html' # HTML file in the working directory

chrome_path = 'open -a /Applications/Google\ Chrome.app %s' # path to Chrome executable

webbrowser.get(chrome_path).open(page) # opens the HTML file with Chrome
```

- **Linux**:

```python
page = './page.html' # HTML file in the working directory

chrome_path = '/usr/bin/google-chrome %s' # path to Chrome executable

webbrowser.get(chrome_path).open(page) # opens the HTML file with Chrome
```

## What You Can Do

1. **Create a Story**

You can create a story, entering the story name, the scene, the character in that scene and the character's line!

2. **Save Stories**

Once a story is created the app creates a database file (**script.db**) and saves it in there, so you can use them later!

The database here is Python's **SQLite**!

3. **Load Stories**

You can load stories that are already stored in the database!

4. **Play Stories**

This option opens a **HTML** page with the whole story info!

You can either play a story from input or load one from database, select it and play it!
