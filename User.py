class User():
    def __init__(self, username):
        self.__id = 0
        self.__username = username
        self.__match_counts = 0
        self.__victories = 0

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_username(self):
        return self.__username

    def get_victories(self):
        return self.__victories

    def get_matchs(self):
        return self.__match_counts

    def plus_match_counts(self):
        self.__match_counts += 1

    def plus_victories(self):
        self.__victories += 1