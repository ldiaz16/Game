import pygame

#Constants
#Sprite sizes
CRAB_SIZE = [55,45.8]
CLOUD_SIZE = [150,120]
SPRITE_SIZE = [50,125]

# Scale the images before defining the Sprite class and adding them to a list
WALK_LIST = [pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/walk/Walk_1.png'),SPRITE_SIZE),pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/walk/Walk_2.png'),SPRITE_SIZE),pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/walk/Walk_3.png'),SPRITE_SIZE),pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/walk/Walk_4.png'),SPRITE_SIZE),pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/walk/Walk_5.png'),SPRITE_SIZE),pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/walk/Walk_6.png'),SPRITE_SIZE)]

JUMP_LIST = [pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/jump/Jump_2.png'),SPRITE_SIZE), pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/jump/Jump_3.png'),SPRITE_SIZE)]

CRAB_LIST = [pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/idle/crab1.png'),CRAB_SIZE),pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/idle/crab2.png'),CRAB_SIZE),pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/idle/crab3.png'),CRAB_SIZE),pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/idle/crab4.png'),CRAB_SIZE),pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/idle/crab5.png'),CRAB_SIZE),pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/idle/crab6.png'),CRAB_SIZE)]

CLOUD = pygame.transform.scale(pygame.image.load('/Users/lucasdiaz/Downloads/Game/assets/constants/cloud.png'), CLOUD_SIZE)


class Sprite:
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    pygame.init()
    self.width, self.height = 800, 430
    self.screen = pygame.display.set_mode(size = (self.width, self.height))
    self.sprite_x = 50
    self.sprite_y = 220
    self.sprite_rect = pygame.Rect(self.sprite_x + 7.5, self.sprite_y, (SPRITE_SIZE[0]-15), SPRITE_SIZE[1]-15)
    self.crab_x = [520,799]
    self.crab_y = 297
    self.cloud_x = [50,320,600]
    self.cloud_y = 25
    self.crab_rects = []
    self.sprite_index = 0
    self.jump_index = 10
    self.counter = 0
    self.score_label = ''
    self.is_jumping = False
    self.initial_sprite_speed = 10
    self.sprite_speed = self.initial_sprite_speed
    self.game_over = False
    for x in self.crab_x:
      rect = pygame.Rect((x+4), (self.crab_y+3), (CRAB_SIZE[0]-8), (CRAB_SIZE[1] - 8))
      self.crab_rects.append(rect)
    self.crab_image = CRAB_LIST[0]
    self.sprite_image = WALK_LIST[0]
    self.jump_image = JUMP_LIST[0]

  def draw(self):
    for x in range(len(self.crab_x)):
        if self.crab_x[x] <= -40:
          self.counter += 1
          self.crab_rects[x].x = 800
          self.crab_x[x] = 800
    for y in range(len(self.cloud_x)):
        if self.cloud_x[y] <= -130:
          self.cloud_x[y] = 800

    for i in range(len(self.crab_x)):
      self.screen.blit(self.crab_image,(self.crab_x[i], self.crab_y))
      self.crab_rects[i].x = self.crab_x[i]
    for i in range(len(self.cloud_x)):
      self.screen.blit(CLOUD, (self.cloud_x[i], self.cloud_y))
    if self.is_jumping == False:
      self.screen.blit(self.sprite_image,(self.sprite_x, self.sprite_y))
    else:
      self.screen.blit(self.jump_image,(self.sprite_x,self.sprite_y))

    pygame.draw.rect(self.screen, (255, 255, 255), self.sprite_rect, 1)

  def count(self):
    font = pygame.font.Font(None, 30)
    self.score_label = "Your score: " + str(self.counter)
    text = font.render(self.score_label, True, (255, 255, 255))
    self.screen.blit(text, (650, 10))



  def walking(self,pos):
    if pos != 0:
      for x in range(len(self.crab_x)):
        self.crab_x[x] += pos
      for y in range(len(self.cloud_x)):
        self.cloud_x[y] += (pos + 1)
      self.sprite_speed -= 1
      if self.sprite_speed == 0:
        self.sprite_speed = self.initial_sprite_speed
        if self.sprite_index == (len(CRAB_LIST)) - 1:
          self.sprite_index = 0
        else:
          self.sprite_index += 1
      self.crab_image = CRAB_LIST[self.sprite_index]
      self.sprite_image = WALK_LIST[self.sprite_index]


  def jumping(self, var):
      if self.is_jumping:
        if self.jump_index >= -10:
          neg = 1
          self.jump_image = JUMP_LIST[0]
          if self.jump_index < 0:
            neg = -1
            self.jump_image = JUMP_LIST[1]
          self.sprite_rect.y -= self.jump_index**2 * var * neg
          self.sprite_y -= self.jump_index**2 * var * neg
          self.jump_index -= 1
        else:
          self.is_jumping = False

          self.jump_index = 10
        self.sprite_rect = pygame.Rect(self.sprite_x, self.sprite_y, SPRITE_SIZE[0], SPRITE_SIZE[1]-10)




  def collision(self):
    if self.sprite_rect.collidelist(self.crab_rects) != -1:
        self.game_over = True
        return self.counter
  # Check if the sprite and crab are colliding
    #return self.game_over












