from datetime import date

dthj = date.today()
day = 1 #dthj.weekday()

dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
if day == 0:   #Segunda
    print("Hoje é", dias[day])
elif day == 1: #Terca
    print("Hoje é", dias[day])
elif day == 2: #Quarta
    print("Hoje é", dias[day])
elif day == 3: #Quinta
    print("Hoje é", dias[day])
elif day == 4: #Sexta
    print("Hoje é", dias[day])
elif day == 5: #Sabado
    print("Hoje é", dias[day])
elif day == 6: #Domingo
    print("Hoje é", dias[day])

print(day)
