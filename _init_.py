calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return(len(string)), string.upper(), string.lower()

def is_contains(string, list_to_search):
    count_calls()
    for i in list_to_search:
        if string.lower() == i.lower():
            return True
    return False
string_info('Urban')
string_info('Python')
is_contains('Urban', ['urban', 'city', 'town'])
is_contains('Python', ['java', 'c++', 'python'])

print(f'Количество вызово функций: {calls}')