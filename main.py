import pygame
import random

pygame.init()

WIDTH, HEIGHT = 600, 400
FPS = 30
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FONT_SIZE = 36

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(("Rock", "Paper", "Scissors"))

font = pygame.font.Font(None. FONT_SIZE)

choices = ["Rock", "Paper", "Scissors"]

def get_winner(player, computer):
    if player == computer:
        return "It's a draw/tie!"
    elif (player == "Rock" and computer == "Scissors") or \
            (player == "Paper" and computer == "Rock") or \
            (player == "Scissors" and computer == "Paper"):
            return "You Win!"
    else:
            return "You Lose"
    
def main():
      running = True
      player_choice = None
      computer_choice = None
      result = ""

      while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        player_choice = "Rock"
                    elif event.key == pygame.K_p:
                        player_choice = "Paper"
                    elif event.key == pygame.K_s:
                        player_choice = "Scissors"

 

 
