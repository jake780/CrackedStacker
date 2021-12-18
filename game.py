import pygame
from block import Block
from scoreboard import Scoreboard

class Game():
    def __init__(self):
        pygame.init()
        pygame.display.init()
        self.width = 400
        self.height = 800
        self.error_margain = 25
        self.difficulty_mult = 1.1
        self.level = 1
        self.bgcolor = ((0,0,20))

        # Create Pygame window
        self.window = pygame.display.set_mode((self.width, self.height))

        # Variables
        self.running = False
        self.blocks = []
        self.effects = []
        self.scoreboard = Scoreboard(self)

        #Set player starting postition
        self.last_block, self.current_block = self.start()

    def restart(self):
        """Restart the game"""
        # Draw
        self.window.fill(self.bgcolor)
        for block in self.blocks:
            block.draw()
        self.scoreboard.old_highscore = self.scoreboard.highscore
        self.scoreboard.update()
        pygame.display.update()
        pygame.time.delay(1000)

        self.blocks = []
        self.scoreboard.score = 0
        self.level = 1
        self.last_block, self.current_block = self.start()

    def end(self):
        """Show end game items and restart"""
        pygame.time.delay(1000)
        self.scoreboard.losing_screen()
        self.scoreboard.compare_scores()
        pygame.display.update()
        pygame.time.delay(3000)
        # dont end the game and restart it instead!
        self.restart()

    def next_level(self):
        """Space was pressed, Attempt to move on to the next level"""

        for block in self.blocks:
            block.frozen = True

        # How far you missed from the center
        # Lose if past half way of the lower block
        missed_margin = abs(self.current_block.x - self.last_block.x)
        if  missed_margin < self.error_margain:
            self.level += 1
            self.scoreboard.score += 1
            new_block = Block(self, self.level)
            self.last_block = self.current_block
            self.current_block = new_block
            new_block.velocity = (self.last_block.velocity * self.difficulty_mult)
            self.blocks.append(new_block)
            self.scoreboard.compare_scores()
        else:
            self.end()

    def start(self):
        """Setup beginning block and freeze it, and setup player block"""
        # Create Immobile start block
        bottom_block = Block(self, 0)
        bottom_block.frozen = True
        bottom_block.x = 200 - (bottom_block.width//2)
        self.last_block = bottom_block
        self.blocks.append(bottom_block)

        # Create first player controlled block
        start_block = Block(self, 1)
        self.blocks.append(start_block)
        return bottom_block, start_block

    def run(self):
        """Run the Game"""
        self.running = True
        #Mainloop
        while self.running:
            self.window.fill((self.bgcolor))
            key = pygame.key.get_pressed()

            # ESC key
            if key[27]:
                self.running = False

            # Close via X
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

            # Space
            if key[32]:
                self.next_level()
                pygame.time.delay(200)

            # Updates
            self.scoreboard.update()

            for e in self.effects:
                e.update()

            for block in self.blocks:
                block.move()
                block.draw()

            pygame.display.update()
            pygame.event.pump()
            pygame.time.delay(10)



