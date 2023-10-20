import pygame
import math

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reflex Racer")

FPS = 60

def tile_background(screen: pygame.display, image: pygame.Surface) -> None:
    screen_width, screen_height = screen.get_size()
    image_width, image_height = image.get_size()
    # Calculate how many tiles we need to draw in x axis and y axis
    tiles_x = math.ceil(screen_width / image_width)
    tiles_y = math.ceil(screen_height / image_height)
    # Loop over both and blit accordingly
    for x in range(tiles_x):
        for y in range(tiles_y):
            screen.blit(image, (x * image_width, y * image_height))
            
def render_obj(img, x, y):
    global win
    win.blit(img, (x,y))

def main():
    #Setting up the background
    bg = pygame.image.load('backg.png')
    bg = pygame.transform.scale(bg, (400, 300))
    
    #Setting up the players
    car_left = pygame.image.load('Player_left.png')
    car_left = pygame.transform.scale(car_left, (100, 100))
    car_right = pygame.image.load('Player_Right.png')
    car_right = pygame.transform.scale(car_right, (100, 100))
    
    #main loop
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
                break
            
        #displaying objects
        tile_background(win, bg) 
        render_obj(car_right,70,500)
        render_obj(car_left,470,500)
        
        pygame.display.update()
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()