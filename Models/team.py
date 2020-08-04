class Team:
    def __init__(self, team_id, team_name):
        self.team_id = team_id
        self.team_name = team_name

    def get_team_dict(self):
        team_dict = {"team_id": self.team_id, "team_name": self.team_name}
        return team_dict
