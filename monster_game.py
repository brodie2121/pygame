import pygame

def main():
    width = 500
    height = 500
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    
    background_image = pygame.load('images/background.png').convert-alpha)
    # Game initialization

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        # Draw background
        screen.fill(blue_color)
        screen.blit(background_image, [0,0])
        # Game display

        pygame.display.update()
        
    pygame.quit()

if __name__ == '__main__':
    main()
