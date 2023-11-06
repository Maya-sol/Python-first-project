import pygame as pg
from Objects import *
import sys

class Game:
  def __init__(self):
    pg.init()
    self.window = pg.display.set_mode([800, 500])
    self.time = pg.time.Clock()
    self.new_game()
    
  def draw_net(self):
    for x in range(20, 800, 20):
      pg.draw.line(self.window, 'white', (x,0), (x,500))
    for x in range(20, 500, 20):
      pg.draw.line(self.window, 'white', (0,x), (800,x))
    
  def draw(self):
    self.window.fill('black')
    self.draw_net()
    self.snake.draw()
    self.food.draw()

  def update(self):
    acceleration = pg.time.get_ticks()
    self.snake.update()
    pg.display.flip()
    self.time.tick(acceleration/10000)
    
  def check_event(self):
    for event in pg.event.get():
      if event.type == pg.QUIT:
        pg.quit()
        sys.exit()
      self.snake.control(event)
        
  def run(self):
    while True:
      self.check_event()
      self.update()
      self.draw()
      
  def new_game (self):
    self.snake = Snake(self)
    self.food = Food(self)
    
      
game = Game()
game.run()