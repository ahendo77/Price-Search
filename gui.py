from PySimpleGUI import *


form = FlexForm('My first GUI')

layout = [ [Text('Enter your name'), InputText()],
           [OK()] ]

button, (name,) = form.LayoutAndRead(layout)
