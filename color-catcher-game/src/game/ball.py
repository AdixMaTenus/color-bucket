class Ball:
    def __init__(self, color, screen_width):
        self.color = color
        self.radius = 15
        self.x = random.randint(0, screen_width)
        self.y = 0
        self.speed = random.uniform(1, 3)

    def fall(self):
        self.y += self.speed

    def reset_position(self, screen_width):
        self.x = random.randint(0, screen_width)
        self.y = 0
        self.speed = random.uniform(1, 3)

    def is_caught(self, bucket):
        return (self.y + self.radius >= bucket.y and
                bucket.x <= self.x <= bucket.x + bucket.width)