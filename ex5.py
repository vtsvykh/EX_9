class Game:
    """
    Class of game.
    """

    def __init__(self, team_1, team_2):
        """
        The function sets attributes for an instance of a class.
        """
        self.score = {
            team_1: 0,
            team_2: 0
        }

    def ball_thrown(self, command, points):
        """
        The function allows you to add points to the selected team.
        """
        self.score[command] += points

    def get_score(self):
        """
        The function allows you to find out the current score of the game.
        """
        name_team = list(self.score.keys())
        score_team = list(self.score.values())

        return (f'{name_team[0]}: {score_team[0]}\n'
                f'{name_team[1]}: {score_team[1]}')

    def get_winner(self):
        """
        The function allows you to find out how to win the game.
        """
        score = self.get_score()
        if score[0] > score[1]:
            print(f'Winner: {list(self.score.keys())[0]}')
        elif score[0] < score[1]:
            print(f'Winner: {list(self.score.keys())[1]}')
        else:
            print('Draw!')

    def __str__(self):
        return self.score

    def __repr__(self):
        return self.__str__()
