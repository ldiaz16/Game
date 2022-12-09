import pygame
import pygame_menu
from src.sprite import Sprite
pygame.init()
WIDTH, HEIGHT = 800, 430
SCREEN = pygame.display.set_mode(size = (WIDTH,HEIGHT))
FPS = 60
FONT = pygame_menu.font.FONT_8BIT	
BACKGROUND = pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/constants/Backgroundpy.png'),(WIDTH,HEIGHT))
FLOOR = pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/constants/Groundfloor.png'),(WIDTH,100))
CLOCK = pygame.time.Clock()

class controller:
  def __init__(self):
      self.menu = pygame_menu.Menu("Jumpy Crab", WIDTH, HEIGHT, position=(10,10),theme=pygame_menu.themes.THEME_BLUE)
      # Create a font object with the FONT_8BIT font and size
      self.menu.add.label('Welcome', font_name = FONT)
      self.menu.add.button("Press to Begin", self.game_stage1, font_name = FONT)
      pygame.display.update()
      self.menu.mainloop(SCREEN)

  def quit_menu(self):
      self.menu = pygame_menu.Menu("Death by crab", WIDTH, HEIGHT, position=(10,10), theme=pygame_menu.themes.THEME_ORANGE)
      self.menu.add.label('You died but its ok crabs are difficult', font_name = FONT, font_size = 22)
      self.menu.add.button("Play Again", self.game_stage1, font_name = FONT)
      self.menu.add.label('Or', font_name = FONT)
      self.menu.add.button("Quit", self.quit_game, font_name = FONT)
      pygame.display.update()
      self.menu.mainloop(SCREEN)

  def quit_game(self):
    exit() 
  
  def mainloop(self):
    running = True
    while running:
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.QUIT:
          exit()
             

  def game_stage1(self):
    sprite = Sprite()
    pos = -6.5
    font = pygame.font.Font(None, 30)
    while True:
      CLOCK.tick(FPS)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          exit()
          pygame.display.update()
        elif event.type == pygame.KEYUP:
            pos = -6.5
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            sprite.is_jumping = True
            pos = -6.5



      sprite.draw()
      sprite.walking(pos)
      sprite.jumping()
      sprite.collision()
      sprite.count()
      if sprite.game_over:
        self.quit_menu()
      pygame.display.update()
      SCREEN.blit(BACKGROUND, BACKGROUND.get_rect())
      SCREEN.blit(FLOOR, (0,330))


      
  
