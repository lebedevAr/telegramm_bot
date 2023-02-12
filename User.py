class User:
    def __init__(self, username):
        self.__id = 1
        self.__username = username
        self.__game_status = False
        self.__attempts = 0
        self.__victories = 0
        self.__match_counts = 0

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def get_username(self):
        return self.__username

    def get_victories(self):
        return self.__victories

    def get_matchs(self):
        return self.__match_counts

    def get_attempts(self):
        return self.__attempts

    def get_game_status(self):
        return self.__game_status

    def plus_match_counts(self):
        self.__match_counts += 1

    def plus_victories(self):
        self.__victories += 1

    def plus_attempt(self):
        self.__attempts += 1

    def change_game_status(self, status: bool):
        self.__game_status = status
