class Player:
    #default constructor
    def __init__(self, name, position, team, attributes: dict, overall: int):
        self.name = name
        self.position = position
        self.team = team
        self.pace = attributes["pace"]
        self.shooting = attributes["shooting"]
        self.passing = attributes["passing"]
        self.dribbling = attributes["dribbling"]
        self.defending = attributes["defending"]
        self.physicality = attributes["physicality"]
        self.attacking_positioning = attributes["attacking_positioning"]
        self.defensive_positioning = attributes["defensive_positioning"]
        self.diving = attributes.get("diving", 0)
        self.handling = attributes.get("handling", 0)
        self.kicking = attributes.get("kicking", 0)
        self.reflexes = attributes.get("reflexes", 0)
        self.goalkeeper_positioning = attributes.get("goalkeeper_positioning", 0)
        self.overall = overall

        self.stamina = 100
        self.has_ball = False
