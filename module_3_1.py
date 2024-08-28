calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info(my_string):
    count_calls()
    m = (len(my_string), my_string.upper(), my_string.lower())
    return m

print(string_info("Urban"))

def is_contains(my_str, my_list):
    count_calls()
    n = my_str in my_list
    return n

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)



