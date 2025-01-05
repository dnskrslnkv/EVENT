from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from .states import Event
from data_files import data_event, chat_data, cache
from getter import getting_chat_id, getting_number_chat
from keyboards.inline_keyboards.info_keyboard import create_event_kb


from templates_text import start_create_event_message

router = Router(name=__name__)


@router.message(Command('event', prefix="!/"))
async def handle_start_event(message: types.Message):

    cache[f'{message.from_user.id}'] = f'{message.chat.id}'
    if str(message.from_user.id) not in chat_data:
        chat_data[f'{message.from_user.id}'] = []
        chat_data[f'{message.from_user.id}'].append({f'{message.chat.id}': {'chat_name': message.chat.full_name,
                                                                            'username': message.from_user.full_name,
                                                                            'user_id': message.from_user.id},
                                                     })
        data_event[f'{message.from_user.id}'] = []
        cache[f'{message.from_user.id}'] = f'{message.chat.id}'
        await message.bot.send_message(chat_id=message.from_user.id,
                                       text=start_create_event_message(message.from_user.full_name))

    else:
        list_chat = getting_chat_id(message.from_user.id, chat_data)
        if cache[f'{message.from_user.id}'] in list_chat:
            await message.answer(
                text=f'{message.from_user.full_name}, пользователь может создавать один действующий опрос в чате! '
                     f'Завершите предыдущий опрос, чтобы создать новый!', show_alert=True)
        else:
            chat_data[f'{message.from_user.id}'].append({f'{message.chat.id}': {'chat_name': message.chat.full_name,
                                                                                'username': message.from_user.full_name,
                                                                                'user_id': message.from_user.id},
                                                         })

            cache[f'{message.from_user.id}'] = f'{message.chat.id}'

            await message.bot.send_message(chat_id=message.from_user.id,
                                           text=start_create_event_message(message.from_user.full_name))


@router.message(Command('cancel', prefix="/"))
async def handle_cancel_event(message: types.Message):

    temp = getting_number_chat(chat_data, cache[f'{message.from_user.id}'], str(message.from_user.id))
    del chat_data[f'{message.from_user.id}'][temp]
    if len(data_event[f'{message.from_user.id}']) > 0:
        del data_event[f'{message.from_user.id}'][temp]
    del cache[f'{message.from_user.id}']
    await message.answer(
        text=f'{message.from_user.full_name}, процесс создания мероприятия приостановлен!', show_alert=True)





@router.message(Command('create', prefix="!/"))
async def handle_create_event(message: types.Message, state: FSMContext):

        data_event[f'{message.from_user.id}'].append({f'{cache[f"{message.from_user.id}"]}':
                                                              {'1': {},
                                                               '2': {},
                                                               '3': {},
                                                               '4': {},
                                                               '5': {},
                                                               '6': {},
                                                               'yes': [],
                                                               'no': [],
                                                               'doubt': [],
                                                               'user_id': message.from_user.id,
                                                               'username': message.from_user.full_name

                                                               },
                 })


        await state.set_state(Event.event_name)
        await message.answer(text='<b> Введите название мероприятия: </b>')




@router.message(Event.event_name, F.text)
async def handle_event_name(message: types.Message, state: FSMContext):
    temp = getting_number_chat(data_event, cache[f'{message.from_user.id}'], str(message.from_user.id))
    data_event[f'{message.from_user.id}'][temp][f"{cache[f'{message.from_user.id}']}"]['1'] = await state.update_data(event_name=message.text)
    await state.clear()
    await state.set_state(Event.date_of_the_event)
    await message.answer(text=f'<b> Введите дату мероприятия: </b>')

@router.message(Event.date_of_the_event, F.text)
async def handle_date_of_the_event(message: types.Message, state: FSMContext):
    temp = getting_number_chat(data_event, cache[f'{message.from_user.id}'], str(message.from_user.id))
    data_event[f'{message.from_user.id}'][temp][f"{cache[f'{message.from_user.id}']}"]['2'] = await state.update_data(date_of_the_event=message.text)
    await state.clear()
    await state.set_state(Event.time_of_the_event)
    await message.answer(text=f'<b> Введите время проведения мероприятия: </b>')

@router.message(Event.time_of_the_event, F.text)
async def handle_time_of_the_event(message: types.Message, state: FSMContext):
    temp = getting_number_chat(data_event, cache[f'{message.from_user.id}'], str(message.from_user.id))
    data_event[f'{message.from_user.id}'][temp][f"{cache[f'{message.from_user.id}']}"]['3'] = await state.update_data(time_of_the_event=message.text)
    await state.clear()
    await state.set_state(Event.location)
    await message.answer(text=f'<b> Введите место проведения мероприятия: </b>')

@router.message(Event.location, F.text)
async def handle_location(message: types.Message, state: FSMContext):
    temp = getting_number_chat(data_event, cache[f'{message.from_user.id}'], str(message.from_user.id))
    data_event[f'{message.from_user.id}'][temp][f"{cache[f'{message.from_user.id}']}"]['4'] = await state.update_data(location=message.text)
    await state.clear()
    await state.set_state(Event.payment)
    await message.answer(text=f'<b> Введите взнос для участия в мероприятии: </b>')

@router.message(Event.payment, F.text)
async def handle_payment(message: types.Message, state: FSMContext):
    temp = getting_number_chat(data_event, cache[f'{message.from_user.id}'], str(message.from_user.id))
    data_event[f'{message.from_user.id}'][temp][f"{cache[f'{message.from_user.id}']}"]['5'] = await state.update_data(payment=message.text)
    await state.clear()
    await state.set_state(Event.count)
    await message.answer(text=f'<b> Введите максимальное количество участников: </b>')

@router.message(Event.count, F.text)
async def handle_count(message: types.Message, state: FSMContext):
    temp = getting_number_chat(data_event, cache[f'{message.from_user.id}'], str(message.from_user.id))
    data_event[f'{message.from_user.id}'][temp][f"{cache[f'{message.from_user.id}']}"]['6'] = await state.update_data(count=message.text)

    await state.clear()
    await message.answer(text=f'<b> Создать мероприятие? </b>',
                             reply_markup=create_event_kb())

