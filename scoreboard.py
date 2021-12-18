import pygame
from effects import Burst

class Scoreboard():
    def __init__(self, game):
        self.game = game
        pygame.font.init()
        self.font = pygame.font.SysFont(None, 54)

        self.x = 50
        self.y = 0
        self.score = 0
        self.highscore = self.load_highscore()
        self.old_highscore = self.highscore

    def load_highscore(self):
        with open("highscore.txt", "r") as hs:
            return hs.read()

    def write_highscore(self):
        with open("highscore.txt", "wt") as hs:
            hs.write(str(self.highscore))

    def compare_scores(self):
        """Check if you beat the highscore"""
        if self.score > int(self.highscore):
            self.highscore = self.score
            self.write_highscore()
            print(f"You beat the highscore! The new highscore is: {self.score}")
            # Burst effect on Highscore
            self.game.effects.append(Burst(self.game, self.game.current_block.x+(self.game.current_block.width//2), self.game.current_block.y+(self.game.current_block.height//2), 50))
        # If at max score aka win
        if self.score > self.game.max_score:
            self.game.win()

    def draw_background(self):
        # Draw banner
        pygame.draw.rect(self.game.window, (150,150,150), (0,0,self.game.width, 40))
        #Draw Score text
        image = self.font.render("Score:", True, "cyan")
        self.game.window.blit(image, (0, 0, 100, 100))
        #Draw HighScore text
        image2 = self.font.render("HS:", True, "cyan")
        self.game.window.blit(image2, (200, 0, 100, 100))

    def display_score(self, x=125, y=2, color="red"):
        # Display score integer
        image = self.font.render(f"{self.score}", True, color)
        self.game.window.blit(image, (x, y))

    def display_highscore(self, x=300, y=2, color="red"):
        # Draw highscore height banner
        pygame.draw.rect(self.game.window, "cyan", (0, self.game.height-((int(self.old_highscore))*20)-20, self.game.width, 20))

        # Draw highscore number
        image = self.font.render(f"{self.highscore}", True, color)
        self.game.window.blit(image, (x, y))

    def display_screen(self, screen_type):
        """Display different screens such as win or lose"""
        font = pygame.font.SysFont(None, 54)
        # Losing Text
        if screen_type == "lose":
            text_color = "red"
            image = font.render("YOU LOSE!", True, text_color)
        # Winning Text
        elif screen_type == "win":
            text_color = "green"
            image = font.render("YOU WIN!", True, text_color)
        else:
            return ValueError("Bad screen_type argument!")

        self.game.window.blit(image, ((self.game.width//2)-100, 200, 100, 100))
        #Display Final Score text
        image2 = self.font.render("Final Score:", True, text_color)
        self.game.window.blit(image2, ((self.game.width//2)-120, self.game.height//2+47, 100, 100))
        #Display Final score Integer
        self.display_score(x=(self.game.width//2)+120, y=(self.game.height//2)+50, color=text_color)
    
    def draw(self):
        # Draw Scoreboard background
        self.draw_background()
        self.display_score()
        self.display_highscore()

    def update(self):
        """Updates all elements of the Scoreboard"""
        self.draw()
        