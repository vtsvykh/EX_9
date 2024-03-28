class Game:
    """

    """

    def __init__(self, team_1, team_2):
        self.score = {
            team_1: 0,
            team_2: 0
        }

    def __str__(self):
        return self.score

    def __repr__(self):
        return self.__str__()

    def ball_thrown(self, command, points):
        self.score[command] += points

    def get_score(self):
        name_team = list(self.score.keys())
        score_team = list(self.score.values())

        return (f'{name_team[0]}: {score_team[0]}\n'
                f'{name_team[1]}: {score_team[1]}')

    def get_winner(self):
        score = self.get_score()
        if score[0] > score[1]:
            print(f'Winner: {list(self.score.keys())[0]}')
        elif score[0] < score[1]:
            print(f'Winner: {list(self.score.keys())[1]}')
        else:
            print('Draw!')
