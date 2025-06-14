# Python-first-project
Snake game
This game is a simple snake game, it starts with a window, on that window you can see 2 squares - the cyan one is the snake, the second one is the food.
there are 3 types of food:
1- green: it increases length by 2 and increases score by 15.
2- yellow: it also increses length by 2, but it also changes color to one of {'white', ' blue', 'cyan', 'magenta'} randomly, but it adds only 10 to the score.
3- red: it decreases length by 1 if the snake is longer than one and adds 5 to the score.
you can move using {A,W,S,D} keys.
you lose if you run into yourself or run into the borders of the net.
the final score is displayed on the top right and it resets when you start a new game.
the speed of the snake increases with time.


Now explaining the code:

For the main file:
1-aftre importing pygame library and our object file, we have "__init__(self):" function, which initiates the library variables, the window that pops up and the time.
2-draw_net(self): just draws a net on the window that pops up by drawing lines with given indentation.
3-draw(self): it fills the window black and call other drawing functions, in the end we initialized the score_text - which would be displayed on the screen as score (we chose type of font, size, color.) then displayed it on the window using window blit with the coordinates we wanted it on.
4-check_event(self): it checks for any keys pressed like the moving buttons and the exit button, and closes the window in case of exit.
5-run(self): it runs our game by calling the needed functions by order.
6-new_game (self): resets the food and snake to the initial state when the game starts.

For the objects file:
1-in the class snake, we started by initiating the game, the size of the snake, the vertices of the rectangle representing the snake, and its features.
2-move(self): it moves the snake using move_ip with the direction (that is a mathematical vector) and divides segment into parts.
3-draw(self): it draws the rectangles of the snake square by square.
4-random_position(self): returns a random coordinates pair.
5-control (self, event): checks if any buttons were pressed and changes the diraction accordingly if allowed (the snake can't suddenly start moving in the opposite direction.
6-check_food(self): checks when an overlap between the snake and food happens then creates a new food in a random position if so. it also checks the type of food and change accordingly.
7-borders(self): checks if the snake ran into the borders of the window's net and starts a new game if so.
8-in the class food we initiated the food features and have only one function that draws the food in the given position.
