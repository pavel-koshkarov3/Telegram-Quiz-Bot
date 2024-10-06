from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder
from questions import quiz_data
from db import get_quiz_index, update_quiz_index, save_score, get_score
from aiogram import F
from aiogram import Dispatcher
from aiogram.filters import Command


def generate_options_keyboard(answer_options, right_answer):
    builder = InlineKeyboardBuilder()
    for option in answer_options:
        builder.add(types.InlineKeyboardButton(
            text=option,
            callback_data="right_answer" if option == right_answer else "wrong_answer")
        )
    builder.adjust(1)
    return builder.as_markup()


async def get_question(message: types.Message, user_id):
    current_question_index = await get_quiz_index(user_id)
    if current_question_index < len(quiz_data):
        correct_index = quiz_data[current_question_index]['correct_option']
        opts = quiz_data[current_question_index]['options']
        kb = generate_options_keyboard(opts, opts[correct_index])
        await message.answer(f"{quiz_data[current_question_index]['question']}", reply_markup=kb)
    else:
        score = await get_score(user_id)
        await message.answer(f"Это был последний вопрос. Ваш результат: {score} из {len(quiz_data)}.")
        await save_score(user_id, score)  # Save score


async def right_answer(callback: types.CallbackQuery):
    await callback.message.answer("Верно!")
    current_question_index = await get_quiz_index(callback.from_user.id)
    await save_score(callback.from_user.id, await get_score(callback.from_user.id) + 1)  # Increase score
    await update_quiz_index(callback.from_user.id, current_question_index + 1)
    await get_question(callback.message, callback.from_user.id)


async def wrong_answer(callback: types.CallbackQuery):
    current_question_index = await get_quiz_index(callback.from_user.id)
    correct_option = quiz_data[current_question_index]['correct_option']
    await callback.message.answer(f"Неправильно. Правильный ответ: {quiz_data[current_question_index]['options'][correct_option]}")
    await update_quiz_index(callback.from_user.id, current_question_index + 1)
    await get_question(callback.message, callback.from_user.id)


async def cmd_start(message: types.Message):
    builder = ReplyKeyboardBuilder()
    builder.add(types.KeyboardButton(text="Начать игру"))
    await message.answer("Добро пожаловать в квиз!", reply_markup=builder.as_markup(resize_keyboard=True))


async def cmd_quiz(message: types.Message):
    await message.answer("Давайте начнем квиз!")
    await update_quiz_index(message.from_user.id, 0)
    await get_question(message, message.from_user.id)


def setup_handlers(dp: Dispatcher):
    dp.message.register(cmd_start, Command("start"))
    dp.message.register(cmd_quiz, F.text == "Начать игру")
    dp.callback_query.register(right_answer, F.data == "right_answer")
    dp.callback_query.register(wrong_answer, F.data == "wrong_answer")
