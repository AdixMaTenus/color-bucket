class Game:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.is_running = True

    def run(self):
        while self.is_running:
            self.handle_events()
            self.update()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_running = False

    def update(self):
        # Update game state (e.g., score, lives)
        pass

    def render(self):
        # Render game objects on the screen
        pass

    def game_over(self):
        self.is_running = False
        # Handle game over logic (e.g., display score)