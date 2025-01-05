from aiogram import Router, F
from aiogram.types import CallbackQuery

from data_files import data_event, chat_data, cache
from keyboards.inline_keyboards.info_keyboard import vote_event_kb

from templates_text import create_template_event_message, delete_event_message

from getter import getting_user_id, getting_number_chat


router = Router(name=__name__)





@router.callback_query(F.data == 'create_event')
async def callback_create_event_yes(callback_query: CallbackQuery):
    """
    Функция callback_create_event_yes обрабатывает нажатие на кнопку "Да" при создании мероприятия.
    """
    temp = getting_number_chat(data_event, cache[f'{callback_query.from_user.id}'], str(callback_query.from_user.id))

    await callback_query.message.bot.send_message(chat_id=cache[f'{callback_query.from_user.id}'],
        text= create_template_event_message(data_event = data_event,
                                            user_id=str(callback_query.from_user.id),
                                            username=callback_query.from_user.full_name,
                                            chat_id=cache[f'{callback_query.from_user.id}'],
                                            index = temp),
        reply_markup=vote_event_kb())
    await callback_query.message.answer(text="Мероприятие успешно создано!")



@router.callback_query(F.data == 'dont_create_event')
async def callback_create_event_no(callback_query: CallbackQuery):
    """
    Функция callback_create_event_no обрабатывает нажатие на кнопку "Нет" при создании мероприятия.
    """
    temp = getting_number_chat(data_event, cache[f'{callback_query.from_user.id}'], str(callback_query.from_user.id))
    key = str(callback_query.from_user.id)
    try:
        del data_event[f'{key}'][temp]
        del chat_data[f'{key}'][temp]
        await callback_query.message.answer(text=delete_event_message(callback_query.from_user.full_name))

    except Exception:
        await callback_query.message.answer(text="Упс... Возникла ошибка попробуйте заново!")


@router.callback_query(F.data == 'going')
async def callback_vote_going(callback_query: CallbackQuery):
    """
    Функция callback_vote_going обрабатывает нажатие на кнопку "Иду" при создании мероприятия.
    """
    key = getting_user_id(callback_query.message.text)
    chat_id = str(callback_query.message.chat.id)
    temp = getting_number_chat(data_event, chat_id, key)


    if callback_query.from_user.full_name in (data_event[f'{key}'][temp][chat_id]['yes']):
        await callback_query.answer(text=f'{callback_query.from_user.full_name}, твой голос уже есть!', show_alert=True)
    elif callback_query.from_user.full_name in (data_event[f'{key}'][temp][chat_id]['no']):
        await callback_query.answer(text=f'{callback_query.from_user.full_name}, твой голос уже есть!', show_alert=True)
    elif callback_query.from_user.full_name in (data_event[f'{key}'][temp][chat_id]['doubt']):
        await callback_query.answer(text=f'{callback_query.from_user.full_name}, твой голос уже есть!', show_alert=True)
    else:
        data_event[key][temp][chat_id]['yes'].append(f'{callback_query.from_user.full_name}')

        await callback_query.message.edit_text(
            text=create_template_event_message(data_event=data_event,
                                               user_id=key,
                                               username=data_event[key][temp][chat_id]['username'],
                                               chat_id=chat_id,
                                               index=temp,
                                               ),
            reply_markup=vote_event_kb())


@router.callback_query(F.data == 'dont_going')
async def callback_vote_dont_going(callback_query: CallbackQuery):
    """
        Функция callback_vote_dont_going обрабатывает нажатие на кнопку "Не иду" при создании мероприятия.
    """
    key = getting_user_id(callback_query.message.text)
    chat_id = str(callback_query.message.chat.id)
    temp = getting_number_chat(data_event, chat_id, key)

    if callback_query.from_user.full_name in (data_event[f'{key}'][temp][chat_id]['yes']):
        await callback_query.answer(text=f'{callback_query.from_user.full_name}, твой голос уже есть!', show_alert=True)
    elif callback_query.from_user.full_name in (data_event[f'{key}'][temp][chat_id]['no']):
        await callback_query.answer(text=f'{callback_query.from_user.full_name}, твой голос уже есть!', show_alert=True)
    elif callback_query.from_user.full_name in (data_event[f'{key}'][temp][chat_id]['doubt']):
        await callback_query.answer(text=f'{callback_query.from_user.full_name}, твой голос уже есть!', show_alert=True)
    else:
        data_event[key][temp][chat_id]['no'].append(f'{callback_query.from_user.full_name}')

        await callback_query.message.edit_text(
            text=create_template_event_message(data_event=data_event,
                                               user_id=key,
                                               username=data_event[key][temp][chat_id]['username'],
                                               chat_id=chat_id,
                                               index=temp,
                                               ),
            reply_markup=vote_event_kb())


@router.callback_query(F.data == 'doubt')
async def callback_vote_doubt(callback_query: CallbackQuery):
    """
            Функция callback_vote_doubt обрабатывает нажатие на кнопку "Сомневаюсь" при создании мероприятия.
    """
    key = getting_user_id(callback_query.message.text)
    chat_id = str(callback_query.message.chat.id)
    temp = getting_number_chat(data_event, chat_id, key)

    if callback_query.from_user.full_name in (data_event[f'{key}'][temp][chat_id]['yes']):
        await callback_query.answer(text=f'{callback_query.from_user.full_name}, твой голос уже есть!', show_alert=True)
    elif callback_query.from_user.full_name in (data_event[f'{key}'][temp][chat_id]['no']):
        await callback_query.answer(text=f'{callback_query.from_user.full_name}, твой голос уже есть!', show_alert=True)
    elif callback_query.from_user.full_name in (data_event[f'{key}'][temp][chat_id]['doubt']):
        await callback_query.answer(text=f'{callback_query.from_user.full_name}, твой голос уже есть!', show_alert=True)
    else:
        data_event[key][temp][chat_id]['doubt'].append(f'{callback_query.from_user.full_name}')

        await callback_query.message.edit_text(
            text=create_template_event_message(data_event=data_event,
                                               user_id=key,
                                               username=data_event[key][temp][chat_id]['username'],
                                               chat_id=chat_id,
                                               index=temp,
                                               ),
            reply_markup=vote_event_kb())


@router.callback_query(F.data == 'change')
async def callback_vote_change(callback_query: CallbackQuery):
    """
            Функция callback_vote_change обрабатывает нажатие на кнопку "Изменить выбор" при создании мероприятия.
    """
    key = getting_user_id(callback_query.message.text)
    chat_id = str(callback_query.message.chat.id)
    temp = getting_number_chat(data_event, chat_id, key)
    if callback_query.from_user.full_name in data_event[f'{key}'][temp][chat_id]['yes']:
        data_event[f'{key}'][temp][chat_id]['yes'].remove(callback_query.from_user.full_name)
    elif callback_query.from_user.full_name in data_event[f'{key}'][temp][chat_id]['no']:
        data_event[f'{key}'][temp][chat_id]['no'].remove(callback_query.from_user.full_name)
    elif callback_query.from_user.full_name in data_event[f'{key}'][temp][chat_id]['doubt']:
        data_event[f'{key}'][temp][chat_id]['doubt'].remove(callback_query.from_user.full_name)
    else:
        await callback_query.answer(
            text=f'{callback_query.from_user.full_name}, вы еще не голосовали! Самое время сделать выбор!',
            show_alert=True)
    await callback_query.message.edit_text(
        text=create_template_event_message(data_event=data_event,
                                           user_id=key,
                                           username=data_event[key][temp][chat_id]['username'],
                                           chat_id=chat_id,
                                           index=temp,
                                           ),
        reply_markup=vote_event_kb())


@router.callback_query(F.data == 'close')
async def callback_vote_close(callback_query: CallbackQuery):
    """
         Функция callback_vote_close обрабатывает нажатие на кнопку "Завершить опрос" при создании мероприятия.
    """
    key = getting_user_id(callback_query.message.text)
    chat_id = str(callback_query.message.chat.id)
    temp = getting_number_chat(data_event, chat_id, key)
    print(key, type(key))
    print(chat_id, type(chat_id))
    print(temp, type(temp))
    print(data_event)

    if data_event[f'{key}'][temp][chat_id]['username'] == callback_query.from_user.full_name:
        await callback_query.message.edit_text(
            text=create_template_event_message(data_event=data_event,
                                               user_id=key,
                                               username=data_event[key][temp][chat_id]['username'],
                                               chat_id=chat_id,
                                               index=temp,
                                               ))
        del data_event[f'{key}'][temp]
        del chat_data[f'{key}'][temp]

    else:
        await callback_query.answer(
            text=f'{callback_query.from_user.full_name}, удалять опрос может только тот кто его создал!',
            show_alert=True)
