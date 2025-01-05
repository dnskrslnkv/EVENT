"""
Хранения функций, которые возвращают текст на то или иное обрабатываемое событие.
"""


"""
Функция create_template_event_message создает сообщение о мероприятии. 
На вход принимает словарь с данными о мероприятии, user_id  и username(fullname) пользователя, создавшего мероприятие.
"""
def create_template_event_message(data_event: dict,
                                  user_id: str,
                                  username: str,
                                  chat_id: str,
                                  index: int) -> str:

    newline_char_yes = '\n ✅'
    newline_char_no = '\n ❌'
    newline_char_doubt = '\n 💭'

    text = f'<b>-----------------------------</b>\n\n' \
           f'⚡️<b>Название меропрития:</b>     {data_event[user_id][index][chat_id]["1"]["event_name"]}\n' \
           f'🗓   <b>Дата проведения:</b>     {data_event[user_id][index][chat_id]["2"]["date_of_the_event"]}\n' \
           f'⏰   <b>Время проведения:</b>     {data_event[user_id][index][chat_id]["3"]["time_of_the_event"]}\n' \
           f'🗾   <b>Место проведения:</b> {data_event[user_id][index][chat_id]["4"]["location"]}\n' \
           f'💵   <b>Взнос:</b>  {data_event[user_id][index][chat_id]["5"]["payment"]}\n' \
           f'👤   <b>Количество участников:</b>    {data_event[user_id][index][chat_id]["6"]["count"]}\n\n' \
           '<b>-----------------------------</b>\n\n' \
           'Идут:\n' \
           f'✅{newline_char_yes.join(data_event[user_id][index][chat_id]["yes"])}\n' \
           '<b>-----------------------------</b>\n\n' \
           'Не идут:\n' \
           f'❌{newline_char_no.join(data_event[user_id][index][chat_id]["no"])}\n' \
           '<b>-----------------------------</b>\n\n' \
           'Сомневаются:\n' \
           f'💭{newline_char_doubt.join(data_event[user_id][index][chat_id]["doubt"])}\n' \
           '<b>-----------------------------</b>\n\n' \
           'Статистика:\n' \
           f'✅: <b>{len(data_event[user_id][index][chat_id]["yes"])}</b>\n' \
           f'❌: <b>{len(data_event[user_id][index][chat_id]["no"])}</b>\n' \
           f'💭: <b>{len(data_event[user_id][index][chat_id]["doubt"])}</b>\n' \
           f'Всего: <b>{len(data_event[user_id][index][chat_id]["yes"])+len(data_event[user_id][index][chat_id]["no"])+len(data_event[user_id][index][chat_id]["doubt"])}</b>\n' \
           '<b>-----------------------------</b>\n\n' \
           f'Мероприятие создал: <b>{username}</b>\n' \
           f'ID: <b>{user_id}</b>\n' \
           '<b>-----------------------------</b>\n\n' \

    return text



"""
Функция error_chat_for_create_event_message создает сообщение о смене чата при использовании команды /event. 
На вход принимает username пользователя.
"""
def error_chat_for_create_event_message(username: str) -> str:
       text = f'<b>{username}</b>,\n\n' \
              f'1️⃣  В чате <b>группы</b> воспользуйтесь командой <b>/event</b>\n'

       return text


"""
Функция start_create_message создает сообщение о режиме создания мероприятия. 
На вход принимает username пользователя.
"""
def start_create_event_message(username: str) -> str:
       text = f'<b> {username} </b>,\n' \
              f'Добро пожаловать в режим создания мероприятия!\n\n\n' \
              f'Для создания мероприятия воспользуйтесь командой - /create\n' \
              f'Для отмены создания мероприятия воспользуйтесь командой - /cancel\n' \
              f'Для получения информации о моих возможностях воспользуйтесь командой - /help\n'

       return text


"""
Функция delete_event_message создает сообщение об удалении мероприятия. 
На вход принимает username пользователя.
"""
def delete_event_message(username: str) -> str:
       text = f'<b> {username} </b>,\n' \
              f'Мероприятие удалено\n\n\n' \
              f'Для получения информации о моих возможностях воспользуйтесь командой - /help\n'

       return text


"""
Функция hello_message создает сообщение "приветствие". 
На вход принимает username пользователя.
"""
def hello_message(username: str) -> str:
       text = f"Привет, <b>{username}</b>!\n" \
              f"Я бот который помогает создать опрос о походе на мероприятие!</b>\n\n" \
              f"Для получения информации о моих возможностях воспользуйтесь командой - /help\n" \

       return text


"""
Функция help_message создает сообщение о правильном использовании бота". 
"""
def help_message() -> str:
       text = '<b>Для корректного функционирования используйте следующий алгоритм</b>:\n\n' \
              '1️⃣ Добавьте меня в <b>группу</b>, в которой хотите создать опрос\n' \
              '2️⃣ В чате <b>группы</b> воспользуйтесь командой <b>/event</b>\n'

       return text