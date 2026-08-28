# Importing a library is a "game library", a set of tools that help programmers create games
import pygame
#import randint from random to place coins in random places
from random import randint

# This is the command that runs pygame
pygame.init()

# Width and height of the game window
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# The program window that is created when we set its size in the settings
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# The name of window
pygame.display.set_caption("You have 30 seconds to collect as much hats as you can")
# Icon of game 1) name 2) set it
icon = pygame.image.load("game_icon.png")
pygame.display.set_icon(icon)

# initialize clock
clock =pygame.time.Clock()
FPS =30
#the size of hero
hero_width=144
hero_height=74
#coordinates of hero +speed
hero_x = 10
hero_y = 10
hero_speed = 10
# The color
beige=(241,232,200)
white = (255, 255, 255)
black = (0, 0, 0)
#score of game
score = 0
#time count
timecount = 30000
time_start = pygame.time.get_ticks()
# text font (name of font, size)
text_font = pygame.font.SysFont("Arial", 30)  




# A function that fills the screen with the selected color
def fill_background():
    screen.fill(beige)
# hero image on display function
def hero_image_display(hero_x,hero_y):
    #add hero image to hero_image
    hero_image=pygame.image.load("hero.png")
    #hero add to display + coordinates
    screen.blit(hero_image,(hero_x,hero_y))
# hero  movement function
def hero_movement_display(hero_x,hero_y, keys):
    # Initialize new_x and new_y to the current position
    new_hero_x, new_hero_y = hero_x, hero_y

    # if press button, then happens movement; i use if not elif because of that way hero can move diagonally; 'and' means that hero doesnt dissapear behind the 
    if keys[pygame.K_RIGHT] and hero_x+hero_width<SCREEN_WIDTH :
        new_hero_x += hero_speed
    if keys[pygame.K_LEFT] and hero_x>0 :
        new_hero_x -= hero_speed
    if keys[pygame.K_DOWN] and hero_y+hero_height<SCREEN_HEIGHT :
        new_hero_y += hero_speed
    if keys[pygame.K_UP] and hero_y>0 :
        new_hero_y -= hero_speed

    return new_hero_x, new_hero_y
# function time
def fps_time():
    clock.tick(FPS)

#coin is image
coin_image=pygame.image.load("coin.png")
# function that makes coins in random place
def coin_display():
    coin_x = randint(0, SCREEN_WIDTH - 50)
    coin_y = randint(0, SCREEN_HEIGHT - 50)
    return coin_x, coin_y
#list of coins
coins = [coin_display()]


# function of text display  
def text_display(text, font, text_col, x,y):
    # img is text with font and color
    img = font.render(text, True, text_col)
    # show that text (img) on position xy
    screen.blit(img, (x,y))

input_text=""
input_text_font = pygame.font.SysFont("Arial", 30) 
def input_text_display(text, font, text_col, x,y):
    # img is text with font and color
    input_text_img = font.render(text, True, text_col)
    # show that text (img) on position xy
    screen.blit(input_text_img, (x,y))
#function that reads score form text file
def read_score():
    try:
        #if we have txt file score , then we read it and get int that is score
        with open('score.txt', 'r') as file:
            score = int(file.read())
            # if we cannot find the file
    except FileNotFoundError:
        # If the file doesn't exist, return a score of 0
        score = 0
    return score
#function that writes score in text file
def write_score(score):
    with open('score.txt', 'w') as file:
        file.write(str(score))



# game on
running = True
# The game cycle, controlled by the running variable. If you need to end the game, you just need to change the value of running to False. As a result, the cycle will end.
while running:
    
    # view each event in turn from the list of all events
    for event in pygame.event.get():
        #text input by user
        if event.type == pygame.TEXTINPUT:
            input_text+=event.text

        # Check window closure -->if event is quit, then close
        # pygame.QUIT is an event that starts after clicking the cross and passes the value False to the running variable, as a result of which the game cycle ends.
        if event.type == pygame.QUIT:
            running = False

    #keys is press on button on keyboard
    keys = pygame.key.get_pressed()
    hero_x, hero_y=hero_movement_display(hero_x, hero_y,keys)

    # Fill in the background color when the game is on
    fill_background()
    # Function about adding hero
    hero_image_display(hero_x, hero_y)
    # allows user to put name and there is output by criteria ( what he inputs, font, color, location)
    input_text_display("Username: "+input_text, input_text_font,(0,0,0), 1000,10)
    # The display of text (Score, score to string, font, color, x,y)# current score reads from file in the loop to be updated
    current_score = read_score()
    text_display("Score: " + str(score), text_font, (0, 0, 0), 10, 10)

    # helo_rect is similar to colliderbox 
    hero_rect =pygame.Rect(hero_x, hero_y, hero_width, hero_height)
    #each coin in coins
    for coin in coins:
        coin_x, coin_y = coin
        # to have no error in colliderrect
        coin_rect = pygame.Rect(coin_x, coin_y, 72, 60)
        # new coin appears
        screen.blit(coin_image,(coin_x, coin_y))

        #if player colide the coin it dissapers from the list of coins
        if coin_rect.colliderect(hero_rect):
            #coin dissapears if we touch it
            coins.remove(coin)
            # score -> +coin = +score
            score+=1
            current_score += 1
            #new coin in list to show up new coin
            coins.append(coin_display())

     # Write the updated score to the file before exiting
    write_score(current_score)   
    
    fps_time()

        # How much time goes on
    time_current = pygame.time.get_ticks()
    elapsed_time = time_current - time_start
    # How much time we have
    remaining_time = max(timecount - elapsed_time, 0)
    time_text = text_font.render(f"Time: {remaining_time // 1000}", True, (0, 0, 0))    
    screen.blit(time_text, (500, 10))
        # If time is ended than gameover
    if remaining_time == 0:
         running= False

    # Upadtes the display
    pygame.display.flip()

gameover= not running
# in that case after running game the user can check his score, not ending the game in 3 seconds, and close the game itself   
while gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = False

    fill_background()
    text_display("Your Score: " + str(score), text_font, (0, 0, 0), 500, 350)
    pygame.display.flip()

# pygame.quit() is a function that checks that when the game cycle is completed, the game window closes
pygame.quit()