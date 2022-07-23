import pygame
from random import randrange

FULLSCREEN = True # whether or not to run fullscreen
WINDOW_WIDTH, WINDOW_HEIGHT = 1000, 1000 # if not fullscreen, this resolution will be used
BACKGROUND_COLOR = pygame.Color("#FFFFFF") # '#FFFFFF' = White

WINDOW_CAPTION = "⚪🔵🟢🟠⚫" # caption of the created window

EXIT_KEY = pygame.K_ESCAPE # ESC to exit game
RESTART_KEY = pygame.K_F5 # F5 to reset the game (changes BG back to BACKGROUND_COLOR)

INITIAL_GROWTH = 0.65 # rate at which the circles grow UNTIL their diameter reaches DIAMETER_FOR_LATTER_GROWTH
LATTER_GROWTH = 0.3 # rate at which the circles grow AFTER their diameter reaches DIAMETER_FOR_LATTER_GROWTH
DIAMETER_FOR_LATTER_GROWTH = 150 # diameter for growth rates (pixels)

CIRCLE_BORDER_SIZE = 5 # circle border thickness (percent of the circle diameter)

NO_DRAW_BORDER_SIZE = 9 # window border where circles will not originate from (percent of the window size)

"""
List of circle colors. First value in each tuple is the circle's bg color,
second value is the outline color
"""
CIRCLE_COLORS = [
    (pygame.Color("#9ADCFF"), pygame.Color("#34B9FF")),
    (pygame.Color("#FFF89A"), pygame.Color("#FFF134")),
    (pygame.Color("#FFB2A6"), pygame.Color("#FF573D")),
    (pygame.Color("#FF8AAE"), pygame.Color("#FF286A")),
]

running = True

def main():
    def drawCircle(c_ret, color):
        if c_ret[0] == 0:
            rand_h = randrange(int(HEIGHT*(NO_DRAW_BORDER_SIZE/100)), int(HEIGHT-(HEIGHT*(NO_DRAW_BORDER_SIZE/100))))
        else:
            rand_h = c_ret[0]
        
        if c_ret[1] == 0:
            rand_w = randrange(int(WIDTH*(NO_DRAW_BORDER_SIZE/100)), int(WIDTH-(WIDTH*(NO_DRAW_BORDER_SIZE/100))))
        else:
            rand_w = c_ret[1]
            
        if c_ret[2] == 0:
            radius = 1
        else:
            if c_ret[2] < DIAMETER_FOR_LATTER_GROWTH:
                radius = c_ret[2] + INITIAL_GROWTH
            else:
                radius = c_ret[2] + LATTER_GROWTH
        
        pygame.draw.circle(screen, color[1], (rand_w, rand_h), radius * (1 + CIRCLE_BORDER_SIZE / 100))
        pygame.draw.circle(screen, color[0], (rand_w, rand_h), radius)
        
        return (rand_h, rand_w, radius)
    
    global running, screen, HEIGHT, WIDTH, keys_pressed, c_ret, color_index, color_change
    c_ret = (0,0,0)
    color_index = 0
    color_change = False
    
    pygame.init()
    
    if FULLSCREEN:
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    pygame.display.set_caption(WINDOW_CAPTION)
    screen.fill(BACKGROUND_COLOR)
    
    dinfo = pygame.display.Info()
    HEIGHT = dinfo.current_h
    WIDTH = dinfo.current_w
    
    pygame.display.update()
    
    while running:
        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == EXIT_KEY:
                    running = False
                elif event.key == RESTART_KEY:
                    screen.fill(BACKGROUND_COLOR)

        keys_pressed = pygame.key.get_pressed()  #checking pressed keys
        if not keys_pressed[EXIT_KEY] and not keys_pressed[RESTART_KEY]:
            if len([k for k in keys_pressed if k]) > 0:
                if color_change:
                    if color_index < len(CIRCLE_COLORS)-1:
                        color_index += 1
                    else:
                        color_index = 0
                color = CIRCLE_COLORS[color_index]
                c_ret = drawCircle(c_ret, color)
                color_change = False
            else:
                c_ret = (0,0,0)
                color_change = True
        else:
            c_ret = (0,0,0)
            color_change = True
                
                
        pygame.display.update()


if __name__ == '__main__':
    main()