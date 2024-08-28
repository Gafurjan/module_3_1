calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(my_str):
    count_calls()
    t = (len(my_str), my_str.upper(), my_str.lower())    
    return t
def is_contains(my_string, my_list):
    count_calls()
    for i in my_list:
        if my_string.upper() == i.upper():
            n = True
        else:
            n = False
    return n


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



