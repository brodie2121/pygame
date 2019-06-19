import pygame
import random
import time
# Create Vehicle Class
class Vehicle(pygame.sprite.Sprite):
    def __init__(self, image, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image).convert_alpha()
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.center = [self.x, self.y] 

"""class Crash(object):
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.width = 500
        self.height = 50
        self.button_color = 191, 146, 177
        self.text_color = 255, 255, 255
        self.font = pygame.font.Font(None, 75)
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center 
    
    def crash_message(self):
        self.image_message = self.font.render("You Crashed" , True, self.text_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.image_message, self.image_message_rect)"""



"""def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

    def message_display(text):
        larget4xt = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects(text, largeText) 
        TextRect.center  = ((display_width/2),(display_height/2))
        gameDisplay.blit(TextSurfd, TextRect)
        
        pygame.display.update()
        
        time.sleep(2)

        game_loop()

    def crash():
        message_display('you crashed')"""

# Create Player Class that inherits from Car Class
class Player(Vehicle):
    def motion(self):
        self.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
        self.vx = 10
        self.vy = 10

        key = pygame.key.get_pressed()

        for i in range(2):
            if key[self.move[i]]:
                self.rect.x += self.vx * [-1, 1][i]

        for i in range(2):
            if key[self.move[2:4][i]]:
                self.rect.y += self.vy * [-1, 1][i]

# define Comp class
class Comp(Vehicle):
    def motion(self):
        self.x += -self.speed
        self.rect.x += -self.speed
        if self.x < 0:
            self.kill()

def main():
    
    # Initialize game window
    width = 1200
    height = 600
    blue_color = (97, 159, 182)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')

    background_image = pygame.image.load('images/background_image.png').convert_alpha()

    # Game initialization
    stop_game = False
    
    # initialize player and add direction button controls
    player = Player('images/player_image.png', 40, 50, 0)
    
    # Add event for creating new comp_vehicles
    ADDCOMP = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDCOMP, 2000)

    # Create group to contain comp_vehicles
    comps = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player)

    while not stop_game:
        for event in pygame.event.get():
            
            # Event handling
            if event.type == pygame.QUIT:
                stop_game = True
            elif event.type == ADDCOMP:
                comp_y = 0
                lane = random.randint(0, 3)
                if lane == 0:
                    comp_y = 100
                elif lane == 1:
                    comp_y = 225
                elif lane == 2:
                    comp_y = 360
                elif lane == 3:
                    comp_y = 485
                new_comp = Comp('images/player_image.png', 1400, comp_y, 5)
                comps.add(new_comp)
                all_sprites.add(new_comp)

        # Game logic
        player.motion()
        

        for comp in comps:
            comp.motion()

        hit = pygame.sprite.spritecollide(player, comps, True)

        if hit:
            #if collision is detected end game
            
            stop_game = True

        # Draw background
        screen.fill(blue_color)
        screen.blit(background_image, [0, 0])

        # Draw player, enemy, and other vehicles
        player_group = pygame.sprite.Group()
        player_group.add(player)
        player_group.draw(screen)

        comps.draw(screen)

        # Game display
        pygame.display.update()

    pygame.quit()

if __name__ == '__main__':
    main()