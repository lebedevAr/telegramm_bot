from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

__all__ = ["game_kb", "comm_kb"]


class __Keyboard:
    def __init__(self, buttons_num: int, text_list: list[str]):
        self._buttons_num = buttons_num
        self._text_list = text_list
        self._auto_resizing = True

    def _create_buttons(self):
        buttons_list = []
        for i in range(self._buttons_num):
            button: KeyboardButton = KeyboardButton(self._text_list[i])
            buttons_list.append(button)
        return buttons_list

    def create_keyboard(self):
        buttons_list = self._create_buttons()
        keyboard_name: ReplyKeyboardMarkup = ReplyKeyboardMarkup(keyboard=[buttons_list],
                                                                 resize_keyboard=self._auto_resizing,
                                                                 one_time_keyboard=True)
        return keyboard_name


kb_1 = __Keyboard(2, ["Играем!", "Не хочу("])
kb_2 = __Keyboard(5, ["/help", "/start", "/photo", "/game", "/cancel"])
game_kb = kb_1.create_keyboard()
comm_kb = kb_2.create_keyboard()
