#%
print("В команде Мастера кода участников: %(team1_num)s!" % {"team1_num": "5"})
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!" %{"team1_num": "5", "team2_num": "6"})
#format
print("Команда Волшебникик данных решила задач: {score2}".format(score2 = "42"))
print("Волшебники данных решили задачи за {team1_time}".format(team1_time = "18015.2"))
#f-строки
team1_num = 5
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
challenge_result = None
tasks_total = score1 + score2
time_avg = int((team1_time / score1 + team2_time / score2) / 2)
if score1 > score2 or score1 == score2 and team1_time < team2_time:
    challenge_result = "Победа команды Мастера кода"
if score2 > score1 or score1 == score2 and team2_time < team1_time:
    challenge_result = "Победа команды Волшебникик данных"
else:
    challenge_result = "Ничья"

print(f"Команды решили {score1} и {score2} задач")
print(f"Результат битвы {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем {time_avg} секунд на задачу")
