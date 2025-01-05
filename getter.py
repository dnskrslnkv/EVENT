def getting_user_id(some_str:str)-> str:
    some_lst = some_str.splitlines()[-2]
    return some_lst.split()[1]

def getting_chat_id(user_id:int, data: dict)->list:
    id = []
    for el in data[f'{user_id}']:
        for i,j in el.items():
            id.append(f'{i}')
    return id


def getting_number_chat(test_data: dict, chat_id:str, user_id: str)->int:
    for i in range(len(test_data[user_id])):
        for k, v in test_data[user_id][i].items():
            if k == chat_id:
                return i