import PySimpleGUI as sg
import toml
from random import choice



with open('config.toml','r') as f :
	config = toml.load(f)
sg.theme(config['Theme'])
List = [sg.Checkbox(c,k=c,
font =["Helvetica", 12],enable_events = True,**config['CHECKBOX']) for c in config['LISTS']]

Window = sg.Window(config['Title'],[
[sg.Text('Name',k='name',
font =["Helvetica", 22],**config['TEXT']),sg.Button(font =["Helvetica", 22],**config['BUTTON'])],
List],
finalize = True,
**config['WINDOW'])
for k in config['KEY_BINDING']['Return']:
	Window.bind(k,'RETURN')

def Generate(Dict : dict):
	List = []
	for k,it in Dict.items() :
		if it : List += config['LISTS'][k]
	return List

while True:
	event, values = Window.read()
	match event :

		case sg.WIN_CLOSED | 'Cancel': break
		case 'RUN'|"RETURN" if any([c for _,c in values.items()]) :
			Window['name'].update(choice(Generate(values)))
		
Window.close()

