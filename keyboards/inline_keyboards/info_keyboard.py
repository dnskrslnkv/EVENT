from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

"""
Хранения функций, которые возвращают Inline клавиатуры.
"""


def create_event_kb() -> InlineKeyboardMarkup:
    """
    Функция create_event_kb создает клавиатуру с функционалом создания мероприятия в чате группы (да/нет).
    """

    button_1 = InlineKeyboardButton(text='✅ Да',
                                    callback_data='create_event')
    button_2 = InlineKeyboardButton(text='❌ Нет',
                                    callback_data='dont_create_event')
    row = [button_1, button_2]
    rows = [row]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup


def vote_event_kb() -> InlineKeyboardMarkup:
    """
    Функция vote_event_kb создает клавиатуру  с функционалом опроса
    об участии в мероприятии (Иду/Не иду/Сомневаюсь/Изменить выбор/Завершить опрос)
    """

    button_1 = InlineKeyboardButton(text='✅ Иду',
                                    callback_data='going')
    button_2 = InlineKeyboardButton(text='❌ Не иду',
                                    callback_data='dont_going')
    button_3 = InlineKeyboardButton(text='💭 Пока думаю',
                                    callback_data='doubt')
    button_4 = InlineKeyboardButton(text='  Изменить выбор',
                                    callback_data='change')
    button_5 = InlineKeyboardButton(text='  Завершить опрос',
                                    callback_data='close')

    row_1 = [button_1, button_2, button_3]
    row_2 = [button_4, button_5]
    rows = [row_1, row_2]
    markup = InlineKeyboardMarkup(inline_keyboard=rows)
    return markup



