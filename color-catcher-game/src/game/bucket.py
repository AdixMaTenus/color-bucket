class Bucket:
    def __init__(self, x, y, width, height, colors):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colors = colors
        self.current_color_index = 0

    def move_left(self, amount):
        self.x -= amount

    def move_right(self, amount):
        self.x += amount

    def cycle_color(self):
        self.current_color_index = (self.current_color_index + 1) % len(self.colors)

    def check_collision(self, ball):
        return (self.x < ball.x < self.x + self.width) and (self.y < ball.y < self.y + self.height)