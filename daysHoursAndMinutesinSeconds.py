timeDay = int(input('digite a quantidade de dias: '))
timeHours = int(input('digite a quantidade de horas: '))
timeMin = int(input('digite a quantidade de minutos: '))
timeDay = timeDay * 86400
timeHours = timeHours * 3600
timeMin = timeMin * 60
totalTime = timeDay + timeHours + timeMin
print(f'{totalTime} SEGUNDOS')
