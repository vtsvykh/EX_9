class Game:
    """
    Class of game.

    Attributes:
        team_1 (str): name of the first team
        team_2 (srt): name of the second team
    """

    def __init__(self, team_1, team_2):
        """
        The function sets attributes for an instance of a class.
        :param team_1: name of the first team
        :param team_2: name of the second team
        """
        self.score = {
            team_1: 0,
            team_2: 0
        }

    def ball_thrown(self, command, points):
        """
        The function allows you to add points to the selected team.
        :param command: team number
        :param points:  number of points
        :return: new game score
        """
        self.score[command] += points

    def get_score(self):
        """
        The function allows you to find out the current score of the game.
        :return: game score
        """
        name_team = list(self.score.keys())
        score_team = list(self.score.values())

        return (f'{name_team[0]}: {score_team[0]}\n'
                f'{name_team[1]}: {score_team[1]}')

    def get_winner(self):
        """
        The function allows you to find out how to win the game.
        :return: the winning team
        """
        score = self.get_score()
        if score[0] > score[1]:
            print(f'Winner: {list(self.score.keys())[0]}')
        elif score[0] < score[1]:
            print(f'Winner: {list(self.score.keys())[1]}')
        else:
            print('Draw!')

    def __str__(self):
        """
        Outputs a string in a readable format.
        """
        return self.score

    def __repr__(self):
        """
        Creates a string representation of an object.
        """
        return self.__str__()
