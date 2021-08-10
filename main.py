import pygame
import random
from pygame.constants import NOFRAME
pygame.init()
import win32gui, win32con


the_program_to_hide = win32gui.GetForegroundWindow()
win32gui.ShowWindow(the_program_to_hide , win32con.SW_HIDE)

height = 500
width = 500
bg_color = (252,212,228)
bg_color = (2,12,12)
 

def run_img():
    image = pygame.image.load(f'./Dice_new/1.png')
    screen.blit(image, (0, 0))


def initial_window():
    global screen
    screen = pygame.display.set_mode((height, width), NOFRAME)
    icon = pygame.image.load('./Dice_img/5.png')
    pygame.display.set_caption('Dice Rolling...')
    pygame.display.set_icon(icon)
    screen.fill(bg_color)
    image = pygame.image.load('Dice_img.png')
    screen.blit(image, (0, 0))
    pygame.display.update() 

    run = False

    while not run:  

        for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                run = True  
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    run = True
    

                if event.key == pygame.K_r:
                    dice_num = random.randint(1, 6)
                    image = pygame.image.load(f'./Dice_new/{str(dice_num)}.png')
                    screen.blit(image, (0, 0))

        pygame.display.flip() 

initial_window()