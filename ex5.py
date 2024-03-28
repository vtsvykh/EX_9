class Game:
    """

    """

    def __init__(self, score):
        self.score = score

    def __str__(self):
        return self.scoreE

    def __repr__(self):
        return self.__str__()

    def ball_thrown(self, command, points):
        self.score[command] += points

    def get_score(self):
        name_team = list(self.score.keys())
        score_team = list(self.score.values())
        for _ in range(len(name_team)):
            print(f'{name_team[_]}: {score_team[_]}')

        return list(self.score.values())

    def get_winner(self):
        score = self.get_score()
        if score[0] > score[1]:
            print(f'Winner: {list(self.score.keys())[0]}')
        elif score[0] < score[1]:
            print(f'Winner: {list(self.score.keys())[1]}')
        else:
            print('Draw!')
