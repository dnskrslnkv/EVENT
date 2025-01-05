
"""
data_event - словарь с информацией о созданном мероприятии.
Структуру словаря:
data_event = {
                'user_id': {
                            {'event_name': "some_str"},
                            {'date_of_the_event': 'some_str'},
                            {'time_of_the_event': 'some_str'},
                            {'location': 'some_str'},
                            {'payment': 'some_str'},
                            {'count': 'some_str'},
                            'yes': ['some_users_fullname'],
                            'no': ['some_users_fullname'],
                            'doubt': ['some_users_fullname'],
                            'user_id': some_user_id,
                            'username': some_username
                            }
            }
"""

data_event = {}

"""
chat_data - словарь с информацией о пользователе и чате в котором он создает мероприятие.
Структуру словаря:
chat_data = {'user_id': [{chat_id: {
                            'chat_name':some_str,
                            'user_id': some_int
                            'username': some_str} 
                            }]
            } 
                
"""

chat_data = {}


cache = {}