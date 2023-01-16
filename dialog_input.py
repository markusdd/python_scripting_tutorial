#!/usr/bin/env python3
from dialog import Dialog
import sys

d = Dialog()
name = ""

# now we use a nice TUI-input-box for asking
# check the Dialog documentation, there is several cool widgets like checklists, yes/no dialogs,
# comboboxes etc. to really easily build e.g. a simple configuration TUI
while not name:
    code, name = d.inputbox(text="What is your name?", width=80)
    if code == d.CANCEL:
        # cancel has been pressed, exit
        sys.exit(0)

# we now ask how we should print the name
code, choice = d.radiolist(text="How should I print your name?", choices=[
    ("upper", "Print the name in uppercase.", True),
    ("lower", "Print the name in lowercase.", False),
    ("normal", "Print the name unchanged.", False),
])

if code == d.CANCEL:
    sys.exit(0)
if choice == "upper":
    name = name.upper()
elif choice == "lower":
    name = name.lower()

d.msgbox(text=f"Hello {name}!", width=30)
