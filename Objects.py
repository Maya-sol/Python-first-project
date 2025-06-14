import pygame as pg
import random

class Snake:
  def __init__(self, game):
    self.game = game
    self.size = 20
    self.rect = pg.rect.Rect([0,0,20,20])
    self.rect.center = self.random_position()
    self.direction = pg.math.Vector2(0,0)
    self.length = 1
    self.segments = []
    self.allowed_direction = {pg.K_w: 1, pg.K_s: 1, pg.K_d: 1, pg.K_a: 1}
    self.color = 'cyan'
    
  def move(self):
    self.rect.move_ip(self.direction)
    self.segments.append(self.rect.copy())
    self.segments = self.segments[-self.length:]
    
  def update(self):
    self.self_eating()
    self.borders()
    self.check_food()
    self.move()
      
  def draw(self):
    [pg.draw.rect(self.game.window, self.color, segment) for segment in self.segments]
  
  def random_position(self):
    return [random.randrange (10, 790, 20) , random.randrange(10, 490, 20)]
  
  def control (self, event):
    if event.type == pg.KEYDOWN:
      if event.key == pg.K_w and self.allowed_direction[pg.K_w]:
        self.direction = pg.math.Vector2(0,-20)
        self.allowed_direction = {pg.K_w: 1, pg.K_s: 0, pg.K_d: 1, pg.K_a: 1}
      if event.key == pg.K_a and self.allowed_direction[pg.K_a]:
        self.direction = pg.math.Vector2(-20,0)
        self.allowed_direction = {pg.K_w: 1, pg.K_s: 1, pg.K_d: 0, pg.K_a: 1}
      if event.key == pg.K_d and self.allowed_direction[pg.K_d]:
        self.direction = pg.math.Vector2(20, 0)
        self.allowed_direction = {pg.K_w: 1, pg.K_s: 1, pg.K_d: 1, pg.K_a: 0}
      if event.key == pg.K_s and self.allowed_direction[pg.K_s]:
        self.direction = pg.math.Vector2(0,20)
        self.allowed_direction = {pg.K_w: 0, pg.K_s: 1, pg.K_d: 1, pg.K_a: 1}
        
  def check_food(self):
    if self.rect.center == self.game.food.rect.center:
      if self.game.food.colour == 'green':
        self.length +=2
        self.game.score +=15
      elif self.game.food.colour == 'yellow':
        self.color = random.choice(['white', ' blue', 'cyan', 'magenta'])
        self.length +=2
        self.game.score +=10
      elif self.game.food.colour == 'red':
        if self.length > 1:
          self.length -= 1
        self.game.score +=5
      self.game.food.colour = random.choice(['red', 'yellow', 'green'])
      self.game.food.rect.center = self.random_position()
      
  def borders(self):
    if self.rect.left < 0 or self.rect.right > 800:
      self.game.new_game()
    if self.rect.top < 0 or self.rect.bottom > 500:
      self.game.new_game()
  def self_eating(self):
    if len(self.segments) != len( set(segment.center for segment in self.segments)):
      self.game.new_game()                        

class Food:
  def __init__(self, game):
    self.game = game
    self.size = 20
    self.rect = pg.rect.Rect([0,0,20,20])
    self.rect.center = self.game.snake.random_position()
    self.colour = random.choice(['red', 'yellow', 'green'])
    
  def draw(self):
    pg.draw.rect(self.game.window, self.game.food.colour, self.rect)
