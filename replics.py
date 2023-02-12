class Replic:
    __commands_list = ["/help - информация о всех командах", "/start - перезапуск бота",
                       "/photo - отправка рандомного кота",
                       "/game - начать игру", "/cancel - закончить игру"]

    def _get_commands_string(self):
        srting = ""
        for e in self.__commands_list:
            srting += f"{e}\n"
        return srting

    def get_helping(self):
        return f"Сейчас есть следующие команды:\n{self._get_commands_string()}Также вы можете " \
               f"воспользоваться клавиатурой!"

    def get_starting(self, username):
        return f"Привет, {username}! Это тестовый бот.\n{self.get_helping()}"

    @staticmethod
    def get_gaming(username):
        return f"Ну что, {username}, готов сыграть в игру?\n" \
               f"Правила просты: я загадываю число от 1 до 100 и у тебя есть сколько-то попыток его угадать " \
               f"(напиши сколько хочешь, но не больше 10! 🥰). Если устанешь играть, то просто напиши /cancel\n" \
               f"Или воспользуйся клавиатурой! "

    @staticmethod
    def get_cancelling(in_game_status: bool):
        return f"Мы вроде и не играли сейчас 😁" if not in_game_status else f"Поиграем в другой раз 😢"
