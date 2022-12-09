
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
      self.start_menu()
  def start_menu(self):
      self.menu = pygame_menu.Menu("Jumpy Crab", WIDTH, HEIGHT, position=(10,10),theme=pygame_menu.themes.THEME_BLUE)
      self.menu.add.label('Welcome', font_name = FONT)
      self.menu.add.button("Set your difficulty", font_name = FONT)
      self.menu.add.button("Easy", self.game_stage1, 0.54, 10, font_name = FONT)
      self.menu.add.button("Medium", self.game_stage1, 0.38, 8, font_name = FONT)
      self.menu.add.button("Hard", self.game_stage1, 0.22, 6, font_name = FONT)
      self.high_score = 0
      pygame.display.update()
      self.menu.mainloop(SCREEN)


  def quit_menu(self,count):
      if count > self.high_score:
          self.high_score = count
      self.menu = pygame_menu.Menu("Death by crab", WIDTH, HEIGHT, position=(10,10), theme=pygame_menu.themes.THEME_ORANGE)
      self.menu.add.label('You died but its ok crabs are difficult', font_name = FONT, font_size = 22)
      high_score_statement = 'Your High Score Is ' + str(self.high_score)
      self.menu.add.label(high_score_statement, font_name = FONT, font_size = 24)
      self.menu.add.button("Play Again", self.start_menu, font_name = FONT)
      self.menu.add.label('Or', font_name = FONT)
      self.menu.add.button("Quit", self.quit_game, font_name = FONT)
      pygame.display.update()
      self.menu.mainloop(SCREEN)

  def quit_game(self,x):

    exit() 
  
  def mainloop(self):
    running = True
    while running:
      events = pygame.event.get()
      for event in events:
        if event.type == pygame.QUIT:
          exit()
             

  def game_stage1(self, x, y):
    sprite = Sprite()
    pos = -6.5
    gravity = x
    grav2 = y
    while True:
      CLOCK.tick(FPS)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          exit()
          pygame.display.update()
        elif event.type == pygame.KEYDOWN:
          if event.key == pygame.K_SPACE:
            pos = -1 * grav2
            sprite.is_jumping = True

      sprite.count()
      sprite.draw()
      sprite.walking(pos)
      sprite.jumping(gravity)
      sprite.collision()
      if sprite.game_over:
        self.quit_menu(sprite.collision())
      pygame.display.update()
      SCREEN.blit(BACKGROUND, BACKGROUND.get_rect())
      SCREEN.blit(FLOOR, (0,330))


      
  
