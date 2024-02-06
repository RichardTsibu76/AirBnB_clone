This is the readme file describing the projects 0x00. AirBnB clone - The console

LET DESCRIBE THE COMMAND INTERPRETER:

This actually is interface or also called the console where commands are being interpreted

The command interpreter serves as the frontend of web app where users can interact with the backend developed using the python object oriented programming(OOP)

So having built it with as backend by deploying the python object oriented programming, the variouscommands show, create, update, delete can used interactively.

LET DIVE A LITTLE DEEPER ABOUT HOW TO START.
-Create the designated repo on the remote server.
- Clone the repository created locally by using this command: git clone https://access_token@github.com/name_of_author_on_github/Airbandb.git.
-Go ahead to work the files given to work with. e.g console.py

HOW TO USE IT.

it actually works into two different mode
We have the interactive mode and the non interactive mode.
In the interactive mode, the console would show aprompt like the shell for the required interaction.

./console.py

(hbnb) help
Documented commands(type help)
----------------------
----------------------
You see these EOF help quit
(hbnb) quit
$

n Non-interactive mode, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
