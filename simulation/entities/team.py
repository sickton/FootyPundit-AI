class Team:
    def __init__(self, name, squad: list, formation: str):
        self.name = name
        self.squad = squad
        self.formation = formation

        self.goalkeepers = []
        self.defenders = []
        self.midfielders = []
        self.attackers = []

        self.assign_player_positions()

    def assign_player_positions(self):
        for player in self.squad:
            position = player.position.upper()

            if position == "GK":
                self.goalkeepers.append(player)
            elif position in ["CB", "RB", "LB", "LWB", "RWB", "DEF"]:
                self.defenders.append(player)
            elif position in ["CM", "RM", "LM", "CAM", "CDM", "MF"]:
                self.midfielders.append(player)
            elif position in ["CF", "ST", "LW", "RW", "RF", "FW", "LF"]:
                self.attackers.append(player)

    def get_goalkeepers(self):
        return self.goalkeepers

    def get_defenders(self):
        return self.defenders

    def get_midfielders(self):
        return self.midfielders

    def get_attackers(self):
        return self.attackers

    def get_player_by_name(self, name: str):
        for player in self.squad:
            if player.name.upper() == name.upper():
                return player

        return None

    def __repr__(self):
        return f"<Team - {self.name} | Formation - {self.formation} | Squad size - {len(self.squad)}>"