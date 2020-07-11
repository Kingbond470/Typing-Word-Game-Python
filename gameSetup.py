from cx_Freeze import *
includefiles=['kingbondl.ico','highscore_stored.txt','bg.jpg','bg1.jpg','back_music.mp3','bg2.jpg','bg_snake.jpg','blas.wav','cluod1.png','cluod2.gif','game_over1.wav','game.py']
excludes=[]
packages=[]
base=None
if sys.platform=='win32':
	base='Win32GUI'
shortcut_table=[(
	'DesktopShortcut', #Shortcut
	'DesktopFolder', #Directory_
	'Word Typing Game', #Name
	'TARGETDIR', #Component_
	'[TARGETDIR]\game.exe', #Target
	None, #Arguments
	None, #Description
	None, #Hottkey
	None, #Icon
	None, #IconIndex
	None, #ShowCmd
	'TARGETDIR', #WkDir
	)
]
msi_data={'Shortcut':shortcut_table}
bdist_msi_options={'data':msi_data}
setup(
	version='0.1',
	Description='It is a beta version of Word Typing Game and It is developed for educational purpose.If you have any other project ideas or some modification required in this application then you can contact me on my social account social account: insta-kingbondl,github-kingbond470,twitter-@mausamsingh470',
	author='Mausam Singh',
	name='KingbondL Word Typing Game',
	options={'build_exe':{'include_files':includefiles},'bdist_msi':bdist_msi_options,},
	executables=[
	Executable(
		script='game.py',
		base=base,
		icon='kingbondl.ico',
		)
	]
)