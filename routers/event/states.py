from aiogram.fsm.state import  StatesGroup, State

class Event(StatesGroup):
    event_name = State()
    date_of_the_event = State()
    time_of_the_event = State()
    location= State()
    payment = State()
    count = State()
