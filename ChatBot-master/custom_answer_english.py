import random

repeat_list = ['Repeat the action', 'Try again!', 'Try one more time', "It's not working, try again"]

joke_potato_list = ['That was just a joke, bro...', 'Joke bro, ist douk :)']

else_list = ["I don't know what that is... \n Try /start", "This command does not exist, start over with /start"]

aim_rofl_list = ["Why are you pointing at me? I'll point at you now 🤬"]

ban_symbols = [',']

available_symbols_age = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

def random_repeat_list():
    return random.choice(repeat_list)

def too_long():
    return "Too much text!"

def random_joke_first():
    return random.choice(joke_potato_list)

def random_else_list():
    return random.choice(else_list)