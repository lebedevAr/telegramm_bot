import random
import scripts

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ContentType, ParseMode, ChatActions

from replics import Replic
from keyboard import *

bot_token = scripts.get_api_token()

bot = Bot(token=bot_token)
dp = Dispatcher(bot)

rep = Replic()

user_dict = {"in_game": False, "attempts": 0, "number": 0}


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(text=rep.get_helping(), reply_markup=comm_kb)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    if user_dict["in_game"]:
        await message.answer(f"Я хотел поиграть...")
    elif not user_dict["in_game"]:
        first_name = message.from_user.first_name
        await message.reply(rep.get_starting(first_name))


# @dp.message_handler(commands=['keyboard'])
# async def process_start_command(message: types.Message):
#     await message.answer(f"Привет, такая получилась клавиатура!", reply_markup=game_keyboard)


# @dp.message_handler(commands=['file'])
# async def process_file_command(message: types.Message):
#     user_id = message.from_user.id
#     await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
#     file = r"C:\Users\artyo\Desktop\кур.docx"
#     await asyncio.sleep(1)
#     await bot.send_document(user_id, open(file, 'rb'), caption='Этот файл')


@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    if user_dict["in_game"]:
        await message.answer(f"Мы играем, не отвлекайся!")
    else:
        user_id = message.from_user.id
        await bot.send_chat_action(user_id, ChatActions.UPLOAD_PHOTO)
        file = scripts.get_cat_picture()
        capt = "Ура коты!!!"
        first_name = message.from_user.first_name
        if first_name == "spetan":
            file = scripts.get_bear_picture()
            captions = ["дааа, медведи", "ну такие нормальные ребята",
                        "еще есть пиздючело 1,5 метра,\nну там такой, отдыхающий, но с припиздоном",
                        "ебать гризли самый быстрый 56км в час", "сука имбалансные существа",
                        "Они не умерли!\nТам просто только серые фотки..."]
            capt = captions[random.randint(0, 5)]
        await bot.send_photo(user_id, file, reply_to_message_id=message.message_id, caption=capt)


@dp.message_handler(commands=['game'])
async def process_start_command(message: types.Message):
    if user_dict["in_game"]:
        await message.answer(f"Мы уже играем, разве нет?")
    else:
        first_name = message.from_user.first_name
        if not user_dict["in_game"]:
            user_dict["in_game"] = True
            user_dict["number"] = scripts.get_random_num()
            await message.reply(text=rep.get_gaming(first_name), reply_markup=game_kb)


@dp.message_handler(commands=['cancel'])
async def process_start_command(message: types.Message):
    if not user_dict["in_game"]:
        await message.reply(rep.get_cancelling(user_dict["in_game"]))
    elif user_dict["in_game"]:
        user_dict["in_game"] = False
        await message.reply(rep.get_cancelling(user_dict["in_game"]))


@dp.message_handler()
async def echo(message: types.Message):
    if not user_dict["in_game"]:
        await message.answer("К сожалению, я не знаю такой команды.\nНапишите, пожалуйста /help !")
    elif user_dict["in_game"] == True and user_dict["attempts"] == 0:
        if int(message.text) <= 10:
            user_dict["attempts"] = int(message.text)
            await message.answer(f"Хорошо, у тебя {message.text} попыток.\nНачнем!")
        else:
            await message.answer(f"Я же просил не больше 10!\nПодумай еще")
    elif user_dict["in_game"] == True and user_dict["attempts"] != 0:
        if int(message.text) == user_dict["number"]:
            user_dict["attempts"] = 0
            user_dict["number"] = 0
            user_dict["in_game"] = False
            await message.answer(f"Красавееееец!\nСыграем еще? /game")
        elif int(message.text) > user_dict["number"]:
            user_dict["attempts"] = user_dict["attempts"] - 1
            attempts = user_dict["attempts"]
            if attempts == 0:
                user_dict["in_game"] = False
                await message.answer(f"Попытки кончились, может повезет в другой раз? /game")
            else:
                await message.answer(f"Не угадал) Мое число меньше! (осталось {attempts} попыток)")
        else:
            user_dict["attempts"] = user_dict["attempts"] - 1
            attempts = user_dict["attempts"]
            if attempts == 0:
                user_dict["in_game"] = False
                await message.answer(f"Попытки кончились, может повезет в другой раз? /game")
            else:
                await message.answer(f"Не угадал) Мое число больше! (осталось {attempts} попыток)")


@dp.message_handler(content_types=ContentType.STICKER)
async def unknown_message(msg: types.Message):
    if user_dict["in_game"]:
        await msg.answer(f"Мы играем, не отвлекайся!")
    else:
        message_text = 'Классный стикер, но я не знаю, что с ним делать 🥲.\nНапишите, пожалуйста /help !'
        await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    if user_dict["in_game"]:
        await msg.answer(f"Мы играем, не отвлекайся!")
    else:
        message_text = 'Не знаю, что это.\nНапишите, пожалуйста /help !'
        await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
