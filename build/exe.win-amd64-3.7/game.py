import pygame
import sys
import random
import time
import os
pygame.init()
pygame.mixer.init()
def text_screen(text,color,x,y):
	screen_text=font.render(text,True,color)
	win.blit(screen_text,[x,y])
def welcome():
	exit_game=False
	bgimg1=pygame.image.load("bg1.jpg")
	bgimg1=pygame.transform.scale(bgimg1,(1080,650)).convert_alpha()   #convert alpha is used,so that it wont affect the game during again again... loading
	while not exit_game:
		win.fill(green)
		win.blit(bgimg1,(0,0))
		text_screen("Welcome to Word Typing Game by KingbondL",black,260,250)
		text_screen("Press Space to Play",green,260,300)
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit_game=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_SPACE:
						gameloop()
			pygame.display.update()
with open("highscore_stored.txt","r") as f:
		highscore=f.read()

if(not os.path.exists("highscore_stored.txt")):
		with open("highscore_stored.txt","w") as f:
			f.write("0")			
def new_word():
	global word_x,word_y,text,chosen_word,press_word,speed
	word_x=random.randint(100,600)
	word_y=0
	chosen_word=random.choice(llist)
	press_word=''
	speed+=0.2
	text=font.render(chosen_word,True,black)

#Colors
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
black=(0,0,0)

#var
x=1080
y=650
speed=0.8
point=0

llist=['kingbondl','mausam','singh','coder','kingbond','Afghanistan','algeria','andorra','angola','antigua','argentina','armenia','australia','austria','azerbaijan','bahamas','bahrain','bangladesh','barbados','belarus','belgium','belize','benin','bhutan','bolivia','bosnia','botswana','brazil','brunei','bulgaria','burkina','burundi','caboverde','cambodia','cameroon','canada','chad','chile','china','colombia','comoros','congo','costarica','cotedivoire','croatia','cuba','cyprus','czechia','denmark','djibouti','dominica','dominican','ecuador','egypt','salvador','equatorial','eritrea','estonia','eswatini','ethiopia','fiji','finland','france','gabon','gambia','georgia','germany','ghana','greece','grenada','guatemala','guinea','guineabissau','guyana','haiti','honduras','hungary','iceland','india','indonesia','iran','iraq','ireland','israel','italy','jamaica','japan','jordan','kazakhstan','kenya','kiribati','kosovo','kuwait','kyrgyzstan','laos','latvia','lebanon','lesotho','liberia','libya','liechtenstein','lithuania','luxembo','malawi','malaysia','maldives','mali','malta','marshall','mauritania','mauritius','mexico','micronesia','moldova','monaco','mongolia','montenegro','morocco','mozambique','myanmar','namibia','nauru','nepal','netherlands','newzealand','nicaragua','niger','nigeria','northkorea','northmacedonia','norway','oman','pakistan','palau','palestine','panama','papua','newguinea','paraguay','peru','philippines','poland','portugal']
font=pygame.font.SysFont('Arial',45)
with open("highscore_stored.txt","w") as f:
				f.write(str(highscore))
				
text1=font.render('Press Space to play again !!',True,red)
#screen
win=pygame.display.set_mode((x,y))
pygame.display.set_caption("Typing Game By kingbondl")

#images
logo=pygame.image.load('bg_snake.jpg')
pygame.display.set_icon(logo)
background1=pygame.image.load('bg1.jpg')
background2=pygame.image.load('bg.jpg')
background3=pygame.image.load('bg2.jpg')
cloud1=pygame.image.load('cluod1.png')
matchimg=pygame.image.load('cluod2.gif') #gif format
#Calling function
new_word()

#game loop
def gameloop():
	global point,word_x,word_y,word_caption,press_word,text,text1,speed,highscore
	#sounds
	pygame.mixer.music.load('back_music.mp3')
	pygame.mixer.music.play()
	pygame.mixer.music.set_volume(0.2)
	channel0=pygame.mixer.Channel(0)
	channel1=pygame.mixer.Channel(1)
	while True:
		if(point>=20 and point<50):
			win.blit(background1,(0,0))
		elif(point>=50 and point<75):
			win.blit(background3,(0,0))
		elif(point>75 and point<100):
			win.blit(background2,(0,0))
		elif(point>=100 and point<150):
			win.blit(background1,(0,0))
		elif(point>150):
			win.blit(background3,(0,0))
		else:
			win.blit(logo,(0,0))
		win.blit(cloud1,(word_x-45,word_y-35))
		win.blit(text,(word_x,word_y))
		word_y+=speed
		word_caption=font.render(chosen_word,True,blue)
		win.blit(word_caption,(10,50))
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				pygame.quit()
				sys.exit()
			elif(event.type==pygame.KEYDOWN):
				press_word+=pygame.key.name(event.key)
				if chosen_word.startswith(press_word):
					text=font.render(press_word,True,blue)
					if(chosen_word==press_word):
						point+=len(chosen_word)
						channel0.play(pygame.mixer.Sound('blas.wav'),maxtime=1000)
						channel0.set_volume(0.1)
						win.blit(matchimg,(word_x+50,word_y+50))
						if point>int(highscore):
							highscore=point
						pygame.display.update()
						time.sleep(0.1)
						new_word()
				else:
					text=font.render(press_word,True,red)
					press_word=''
		
		text_screen("Score:"+str(point)+" HS:"+str(highscore),red,10,10)
			
		#point_caption=font.render(str(point),True,red)
		#win.blit(point_caption,(10,20))
		if(word_y<y-4):
			pass
		else:
			bb=pygame.mixer.Channel(1).get_busy()
			if bb==1:
				pass
			else:
				channel1.play(pygame.mixer.Sound('game_over1.wav'),maxtime=4000)
			win.blit(text1,(100,260))
			pygame.display.update()
			event=pygame.event.wait()
			if(event.type==pygame.QUIT):
				pygame.quit()
				sys.exit()
			if(event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE):
				point=0
				speed=0.8
				new_word()		
		pygame.display.update()
welcome()