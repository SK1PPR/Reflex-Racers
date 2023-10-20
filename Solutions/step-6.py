import pygame
import math
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reflex Racers")

FPS = 60
VEL = 7
SCORE = 0
MAX_VEL = 13
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

def display_text(text):
    font = pygame.font.SysFont("comicsans", 40)
    text_render = font.render(text, 1, "red")
    win.blit(text_render, (WIDTH/2 - text_render.get_width() / 2, HEIGHT/2 - text_render.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)
    
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
    
    #adding background music
    bgmusic = pygame.mixer.Sound('bgmusic.mp3')
    pygame.mixer.Sound.play(bgmusic, -1)
    
    #main loop
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        global VEL
        global SCORE
        
        #spawn obstacle randomized
        frames+=1
        if frames == random_left:
            spawn_obstacle_left()
            random_left = frames + random.randint(min_time,max_time)
        if frames == random_right:
            spawn_obstacle_right()
            random_right = frames + random.randint(min_time,max_time)
        if frames%200 == 0 and VEL < MAX_VEL:
            if VEL < MAX_VEL:
                VEL+=1
            if max_time > min_time:
                max_time-=10
            
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
        render_obj(car_right, x_right,500)
        render_obj(car_left,x_left,500)
        for obstacle in obstacles:
            obstacle[2]+=VEL
            render_obj(obstacle[0], obstacle[1], obstacle[2])
            if obstacle[2] >= HEIGHT:
                obstacles.remove(obstacle)
                SCORE += 10
                
            if obstacle[2] < 500 and obstacle[2] >= 400:
                if obstacle[1] == x_left or obstacle[1] == x_right:
                    display_text("Game Over!")
                    run = False
            
        highscore_text = pygame.font.SysFont("comicsans", 40).render(f"Score: {SCORE}", SCORE, "black")
        win.blit(highscore_text, (10, HEIGHT - highscore_text.get_height() - 10))
        
        pygame.display.update()
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()