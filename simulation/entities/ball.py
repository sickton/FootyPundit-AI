class Ball:
    def __init__(self):
        self.position = (0,0)
        self.state = "free"
        self.last_touch = None

    def __repr__(self):
        return f"<Ball Status = {self.state} | Last touch - {self.last_touch}>"