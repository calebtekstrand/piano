import pygame
from pygame.locals import *
from Piano import Piano
from sqlite3 import connect

def login():
	login_db = "LoginInfo.db"
	connection = connect(login_db)
	cursor = connection.cursor()
	
	command = "CREATE TABLE IF NOT EXISTS 'Login Info' "
	command+= "(username TEXT PRIMARY KEY, "
	command+= "password TEXT)"
	print(command)
	cursor.execute(command)
	
	notdone = True
	while notdone:
		userinput = raw_input("Login(1) or Signup(2): ")
		if userinput == "1":
			username = raw_input("Username: ")
			command = "SELECT username "
			command+= "FROM 'Login Info' "
			command+= "WHERE username='{}'".format(username)
			print(command)
			cursor.execute(command)
			#print(cursor.fetchone())
			if str(cursor.fetchone()) == "None":
				print("Username does not exist. Please make an account or try again.")
			else:
				password = raw_input("Password: ")
				command = "SELECT password "
				command+= "FROM 'Login Info' "
				command+= "WHERE username='{}'".format(username)
				print(command)
				cursor.execute(command)
				check = cursor.fetchone()[0]
				print(check)
				if check == password:
					notdone = False
				else:
					print("Try Again")
		elif userinput == "2":
			username = raw_input("Username: ")
			command = "SELECT username "
			command+= "FROM 'Login Info' "
			command+= "WHERE username='{}'".format(username)
			print(command)
			cursor.execute(command)
			#print(cursor.fetchone())
			if str(cursor.fetchone()) == "None":
				password = raw_input("Password: ")
				command = "INSERT INTO 'Login Info' (username, password) "
				command+= "VALUES ('{0}', '{1}')".format(username, password)
				print(command)
				cursor.execute(command)
				notdone = False
			else:
				print("Try Again")
		elif userinput == "3":
			notdone = False
		else:
			print("Try Again")
		
	connection.commit()
	cursor.close()
	connection.close()
login()

# Initialize pygame and set up display, color variables, buttons and button text
pygame.init()
white = (255,255,255)
black = (0,0,0)
display_width = 640
display_heigth = 400
menuDisplay = pygame.display.set_mode((display_width, display_heigth))
startButton = pygame.Rect(270,175,100,50)
startFont = pygame.font.SysFont(None, 48)
startText = startFont.render('Start', True, white, black)
startTextRect = startText.get_rect()
startTextRect.centerx = startButton.centerx
startTextRect.centery = startButton.centery
def menu():
  menu = True
  while menu:
    for event in pygame.event.get():
      # print(event)
      if event.type == pygame.QUIT:
        pygame.quit()
        quit()
      elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = event.pos
        print(mouse_pos)
        if startButton.collidepoint(mouse_pos):
          # print("HI!")
          myPiano = Piano()
          myPiano.play()
          quit()
      menuDisplay.fill(white)
      pygame.draw.rect(menuDisplay, black, startButton)
      menuDisplay.blit(startText, startTextRect)
      pygame.display.update()
menu()