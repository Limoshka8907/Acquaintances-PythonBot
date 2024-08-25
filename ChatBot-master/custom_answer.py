import random


repeat_list = ['Повторите действие','Повторите ещё раз!','Попробуйте снова','Это не работает,попробуй ещё раз']

joke_potato_list = ['Это шутка...\n\nМы все знаем что есть только 2 гендера - 1 и 0)','Jokes)']

else_list = ['Я не знаю что это... \n Попробуй /start','Данной команды не существует, начни заново /start']

aim_rofl_list = ['Чево?']

ban_symvols = [',']

available_symvols_age = ['1','2','3','4','5','6','7','8','9','0']

def random_reapeat_list():
	return random.choice(repeat_list)
def too_long():
	return 'Слишком много текста!'
def joke_first():
	return random.choice(joke_potato_list)
def else_list():
	return random.choice(else_list)