import random

class Game:
    def __init__(self):
        self.player = None
        self.enemies = []
        self.score = 0

    def setup_game(self):
        self.player = Player()
        for _ in range(5):
            enemy = Enemy()
            self.enemies.append(enemy)

    def update_game(self):
        self.player.update()
        for enemy in self.enemies:
            enemy.update()
            if self.player.collides_with(enemy):
                self.game_over()
        self.score += 1

    def game_over(self):
        print("Game Over!")
        print("Score:", self.score)
        exit()

class GameObject:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size

    def update(self):
        pass

    def collides_with(self, other_object):
        if self.x < other_object.x + other_object.size and self.x + self.size > other_object.x:
            if self.y < other_object.y + other_object.size and self.y + self.size > other_object.y:
                return True
        return False

class Player(GameObject):
    def __init__(self):
        super().__init__(10, 10, 10)

    def update(self):
        self.move()

    def move(self):
        # AI logic for player movement
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

class Enemy(GameObject):
    def __init__(self):
        x = random.randint(0, 20)
        y = random.randint(0, 20)
        super().__init__(x, y, 10)

    def update(self):
        self.move()

    def move(self):
        # AI logic for enemy movement
        self.x += random.randint(-1, 1)
        self.y += random.randint(-1, 1)

def main():
    game = Game()
    game.setup_game()
    while True:
        game.update_game()

if __name__ == "__main__":
    main()