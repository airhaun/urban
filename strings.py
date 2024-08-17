team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'
name_team1 = 'Мастера кода'
name_team2 = 'Волшебники данных'

print('В команде Мастера кода учатсников: %s' % team1_num)
print('Итого сегодня в командах участников: %s и %s' % (team1_num, team2_num))
print('Команда волшебники данных решила задач: {} !'.format(score2))
print('Волшебнмкм данных решили задачи за {} c !'.format(team2_time))
print(f'количество решенных задач по командам: {score1} 4 {score2} задач')
print(f'количество задач {tasks_total} и среднее время решений {time_avg}')
if score1 > score2:
    print(f'Победа команды {name_team1}')
elif score2 > score1:
    print(f'Победа команды {name_team2}')
else:
    print('Победила дружба!')
