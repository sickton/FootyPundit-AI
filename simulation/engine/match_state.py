
class MatchState:
    def __init__(self, teamA, teamB):
        self.team_a = teamA
        self.team_b = teamB
        self.score = {self.team_a.name : 0, self.team_b.name : 0}
        self.minute = 0

        self.possession = None
        self.ball = None

        self.events = []

    def add_event(self, event):
        self.events.append(event)

    def __repr__(self):
        return f"<MatchState minute = {self.minute} | score = {self.score}>"