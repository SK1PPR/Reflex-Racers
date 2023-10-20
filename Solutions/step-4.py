import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reflex Racer")

FPS = 60
VEL = 7
obstacles = []

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
    
def spawn():
    im = pygame.image.load('Police.png')
    im = pygame.transform.scale(im, (100,100))
    return im
    
def spawn_obstacle_left():
    im = spawn()
    xs = [70, 220]
    pos = random.choice(xs)
    obstacles.append([im,pos,-20])
    
def spawn_obstacle_right():
    im = spawn()
    xs = [470, 620]
    pos = random.choice(xs)
    obstacles.append([im,pos,-20])
    
def randomize():
    return random.randint(60,120)

def main():
    
    #Setting up the background
    bg = pygame.image.load('backg.png')
    bg = pygame.transform.scale(bg, (400, 300))
    
    #Setting up the players
    car_left = pygame.image.load('Player_left.png')
    car_left = pygame.transform.scale(car_left, (100, 100))
    car_right = pygame.image.load('Player_Right.png')
    car_right = pygame.transform.scale(car_right, (100, 100))
    car_left_lane = False #False means left, True means right
    car_right_lane = False
    
    #obstacle spawwnig
    min_time = 60
    max_time = 300
    random_left = random.randint(min_time,max_time)
    random_right = random.randint(min_time,max_time)
    frames = 0
    
    #main loop
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        global VEL
        
        #spawn obstacle randomized
        frames+=1
        if frames == random_left:
            spawn_obstacle_left()
            random_left = frames + random.randint(min_time,max_time)
        if frames == random_right:
            spawn_obstacle_right()
            random_right = frames + random.randint(min_time,max_time)
        
        #listening for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
                break
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LSHIFT:
                    car_left_lane = not car_left_lane
                if event.key == pygame.K_RSHIFT:
                    car_right_lane=not car_right_lane
            
        #displaying objects
        tile_background(win, bg)
        if car_left_lane:
            x_left = 70
        else:
            x_left = 220
        if car_right_lane:
            x_right = 470
        else:
            x_right = 620
        render_obj(car_right,x_left,500)
        render_obj(car_left,x_right,500)
        for obstacle in obstacles:
            obstacle[2]+=VEL
            render_obj(obstacle[0], obstacle[1], obstacle[2])
            if obstacle[2] >= HEIGHT:
                obstacles.remove(obstacle)
        
        pygame.display.update()
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()