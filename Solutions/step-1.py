import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reflex Racer")

FPS = 60

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                run = False
                break
    pygame.quit()
    quit()
    
if __name__ == "__main__":
    main()