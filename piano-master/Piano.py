import pygame
from pygame.locals import *
from sqlite3 import connect
class Piano:
	white = (255,255,255)
	black = (0,0,0)
	
	def __init__(self):
		self.running = True
		
		self.size = self.weight, self.height = 640, 400
		self.screen = pygame.display.set_mode(self.size)
		self.screen.fill(self.white)
		
	def on_init(self):
		pygame.init()
		self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self.running = True

 
	def on_event(self, event):
		if event.type == pygame.QUIT:
			self.running = False
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_pos = event.pos
			print(mouse_pos)
			if self.abutton.collidepoint(mouse_pos):
				self.anote.play()
			elif self.bbutton.collidepoint(mouse_pos):
				self.bnote.play()
			elif self.cbutton.collidepoint(mouse_pos):
				self.cnote.play()
			elif self.dbutton.collidepoint(mouse_pos):
				self.dnote.play()
			elif self.ebutton.collidepoint(mouse_pos):
				self.enote.play()
			elif self.fbutton.collidepoint(mouse_pos):
				self.fnote.play()
			elif self.gbutton.collidepoint(mouse_pos):
				self.gnote.play()
			elif self.playbutton.collidepoint(mouse_pos):
				self.playsong()
			elif self.recordbutton.collidepoint(mouse_pos):
				self.makesong()
	def playsong(self):
		song_db = "Song.db"
		connection = connect(song_db)
		cursor = connection.cursor()
		
		songname = raw_input("Song Title: ")
		command = "SELECT notecode "
		command+= "FROM 'Song' "
		command+= "WHERE songname='{}'".format(songname)
		print(command)
		cursor.execute(command)
		notecode = cursor.fetchone()[0]
		print(notecode)
		
		
		command = "SELECT restcode "
		command+= "FROM 'Song' "
		command+= "WHERE songname='{}'".format(songname)
		print(command)
		cursor.execute(command)
		restcode = cursor.fetchone()[0]
		print(restcode)
		
		
		for i in range(len(notecode)):
			print(notecode[i])
			current = int(notecode[i])
			if current == 0:
				self.anote.play()
			elif current == 1:
				self.bnote.play()
			elif current == 2:
				self.cnote.play()
			elif current == 3:
				self.dnote.play()
			elif current == 4:
				self.enote.play()
			elif current == 5:
				self.fnote.play()
			elif current == 6:
				self.gnote.play()
			else:
				print("error")
			print("i= " + str(i))
			print(restcode[i*4:i*4+4])
			current = int(restcode[i*4:i*4+4])
			pygame.time.wait(current)
		connection.commit()
		cursor.close()
		connection.close()
	def makesong(self):
		print("hi")
		clock = pygame.time.Clock()
		notecode = ""
		restcode = ""
		notdone = True
		clock.tick()
		while notdone:
			
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
					notdone = False
				elif event.type == pygame.MOUSEBUTTONDOWN:
					mouse_pos = event.pos
					print(mouse_pos)
					if self.abutton.collidepoint(mouse_pos):
						self.anote.play()
						notecode+= "0"
						clock.tick()
						print(clock.get_time())
						restcode+= ('00' + str(clock.get_time()))[-4:]
						clock.tick()
					elif self.bbutton.collidepoint(mouse_pos):
						self.bnote.play()
						notecode+= "1"
						clock.tick()
						print(clock.get_time())
						restcode+= ('00' + str(clock.get_time()))[-4:]
						clock.tick()
					elif self.cbutton.collidepoint(mouse_pos):
						self.cnote.play()
						notecode+= "2"
						clock.tick()
						print(clock.get_time())
						restcode+= ('00' + str(clock.get_time()))[-4:]
						clock.tick()
					elif self.dbutton.collidepoint(mouse_pos):
						self.dnote.play()
						notecode+= "3"
						clock.tick()
						print(clock.get_time())
						restcode+= ('00' + str(clock.get_time()))[-4:]
						clock.tick()
					elif self.ebutton.collidepoint(mouse_pos):
						self.enote.play()
						notecode+= "4"
						clock.tick()
						print(clock.get_time())
						restcode+= ('00' + str(clock.get_time()))[-4:]
						clock.tick()
					elif self.fbutton.collidepoint(mouse_pos):
						self.fnote.play()
						notecode+= "5"
						clock.tick()
						print(clock.get_time())
						restcode+= ('00' + str(clock.get_time()))[-4:]
						clock.tick()
					elif self.gbutton.collidepoint(mouse_pos):
						self.gnote.play()
						notecode+= "6"
						clock.tick()
						print(clock.get_time())
						restcode+= ('00' + str(clock.get_time()))[-4:]
						clock.tick()
					elif self.recordbutton.collidepoint(mouse_pos):
						notdone = False
						print("bye")
						clock.tick()
						print(clock.get_time())
						restcode+= ('00' + str(clock.get_time()))[-4:]
						clock.tick()
		restcode = restcode[4:]
		print("notecode: " + notecode)
		print("restcode: " + restcode)
		if self.running == True:
			song_db = "Song.db"
			connection = connect(song_db)
			cursor = connection.cursor()
		
			songname = raw_input("New Song Title: ")
			command = "INSERT INTO 'Song' (songname, notecode, restcode)  "
			command+= "VALUES ('{0}', '{1}', '{2}')".format(songname, notecode, restcode)
			print(command)
			cursor.execute(command)	

			connection.commit()
			cursor.close()
			connection.close()
		
	def on_loop(self):
		pass
	def on_render(self):
		self.screen.blit(pygame.image.load('keyboard.png'), [50,100])
		pygame.draw.rect(self.screen, [250,0,0], self.abutton)
		pygame.draw.rect(self.screen, [250,0,0], self.bbutton)
		pygame.draw.rect(self.screen, [250,0,0], self.cbutton)
		pygame.draw.rect(self.screen, [250,0,0], self.dbutton)
		pygame.draw.rect(self.screen, [250,0,0], self.ebutton)
		pygame.draw.rect(self.screen, [250,0,0], self.fbutton)
		pygame.draw.rect(self.screen, [250,0,0], self.gbutton)
		pygame.draw.rect(self.screen, [0,250,0], self.playbutton)
		pygame.draw.rect(self.screen, [0,0,250], self.recordbutton)
		pygame.display.update()
	def on_cleanup(self):
		pygame.quit()
 
	def play(self):
		if self.on_init() == False:
			self.running = False
			
		song_db = "Song.db"
		connection = connect(song_db)
		cursor = connection.cursor()
	
		command = "CREATE TABLE IF NOT EXISTS 'Song' "
		command+= "(songname TEXT PRIMARY KEY, "
		command+= "notecode TEXT, "
		command+= "restcode TEXT)"
		print(command)
		cursor.execute(command)
		
		connection.commit()
		cursor.close()
		connection.close()
		
		self.anote = pygame.mixer.Sound('notes/a.wav')
		self.bnote = pygame.mixer.Sound('notes/b.wav')
		self.cnote = pygame.mixer.Sound('notes/c.wav')
		self.dnote = pygame.mixer.Sound('notes/d.wav')
		self.enote = pygame.mixer.Sound('notes/e.wav')
		self.fnote = pygame.mixer.Sound('notes/f.wav')
		self.gnote = pygame.mixer.Sound('notes/g.wav')
		self.abutton = pygame.Rect(212,227,30,61)
		self.bbutton = pygame.Rect(244,227,30,61)
		self.cbutton = pygame.Rect(277,227,30,61)
		self.dbutton = pygame.Rect(308,227,30,61)
		self.ebutton = pygame.Rect(340,227,30,61)
		self.fbutton = pygame.Rect(372,227,30,61)
		self.gbutton = pygame.Rect(404,227,30,61)
		self.playbutton = pygame.Rect(212,300,30,30)
		self.recordbutton = pygame.Rect(404,300,30,30)
		
		while( self.running ):
			for event in pygame.event.get():
				self.on_event(event)
			self.screen.fill(self.white)
			self.on_loop()
			self.on_render()
		self.on_cleanup()

# # if __name__ == "__main__" :
	# # myPiano = Piano()
	# # myPiano.play()
