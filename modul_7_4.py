

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = (team1_time*team1_num + team2_time*team2_num)/tasks_total

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = f'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = f'Победа команды Волшебники Данных!'
else:
    result = f'Ничья!'
challenge_result = result

#Использование %:
print('В команде Мастера кода участников: %s ! ' % team1_num)
print('Итого сегодня в командах участников: %s и %s !' %(team1_num, team2_num))
#Использование format():
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Волшебники данных решили задачи за {} !'.format(round(team1_time, 1)))
#Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {round(time_avg,1)} секунды на задачу!.')
