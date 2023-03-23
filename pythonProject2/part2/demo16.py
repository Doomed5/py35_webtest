class Game():
    top_scorce = 0

    def __init__(self, player_name):
        self.player_name = player_name

    def start_game(self):
        print('开始游戏')

    @classmethod
    def show_top_scorce(cls):
        print(cls.top_scorce)

    @staticmethod
    def show_help():
        print('帮助信息')
