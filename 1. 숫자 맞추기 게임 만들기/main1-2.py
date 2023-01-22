import random

random_number = random.randint(1,100)

game_count = 1

while True:
	my_number = int(input("1~100 사이의 숫자를 입력하세요"))

	if my_number > random_number:
		print("down")
	elif my_number < random_number:
		print("up")

	elif my_number == random_number:
		print(f"{game_count}회 만에 맞추었습니다")
		break

	game_count = game_count + 1