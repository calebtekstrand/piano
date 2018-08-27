import pygame
from pygame.locals import *
from note import Note
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
		pygame.display.update()
	def on_cleanup(self):
		pygame.quit()
 
	def play(self):
		if self.on_init() == False:
			self.running = False
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
