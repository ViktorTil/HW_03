from datetime import datetime, timedelta

first = datetime(year=1990, month=6, day=10).date()
second = datetime(year=1996, month=2, day=29).date()
third = datetime(year=1998, month=7, day=12).date()
fourth = datetime(year= 2001, month=3, day=7).date()
fifth = datetime(year=1992, month=6, day=13).date()
sixth = datetime(year=1978, month=6, day=16).date()
seventh = datetime(year=1980, month=6, day=14).date()
eighth = datetime(year=2000, month=6, day=11).date()
users = [{"name": "vasya", "birthday": first}, {"name": "nata",
                                                "birthday": second}, {"name": "oleg", "birthday": third} ,{"name": "marta", "birthday": fourth}]

users.extend([{"name": "galja", "birthday": fifth}, {"name": "anja",
                                                "birthday": sixth}, {"name": "olga", "birthday": seventh}, {"name": "marik", "birthday": eighth}])




current_datetime = datetime.now()
saturday = current_datetime + timedelta(5 - current_datetime.weekday())
friday = current_datetime + timedelta(12 - current_datetime.weekday())


def add(users):
    
    future_week={"Monday" : [], "Tuesday" : [], "Wednesday" : [],"Thursday" : [], "Friday" : [] }
    
    for fb in users:
        
        if fb["birthday"] >= saturday.date() and fb["birthday"] <= friday.date():
             
            if fb["birthday"].weekday() >= 5:
                day = "Monday"
            else:
                day = fb["birthday"].strftime("%A")

            future_week[day].append(fb['name'])

    return future_week   
 
    
def get_birthdays_per_week(users):
    for day, name in users.items():
         if name != []:
            print(f'{day} : {", ".join(map(str,name))}')



def next_birthday(users):
    users_next = []
    for user in users:
        temp_birth = user['birthday']
        
        try:
            user_data = temp_birth.replace(year=current_datetime.year)

            if user_data < current_datetime.date():
                user_data = temp_birth.replace(year=current_datetime.year+1)

            users_next.append({'name': user['name'], 'birthday': user_data})
            
        except ValueError:
            user_data = temp_birth.replace(year=current_datetime.year, day=28)

            if user_data < current_datetime.date():
                
                try:
                    user_data = temp_birth.replace(year=current_datetime.year+1)

                except ValueError:
                    user_data = temp_birth.replace(year=current_datetime.year+1, day=28)


            users_next.append({'name': user['name'], 'birthday': user_data})
    
    return users_next


def main():

    future_birth = next_birthday(users) # следующие дни рождения от сегодняшней даты

    future_week = add(future_birth) # выборка ДР на след неделе

    get_birthdays_per_week(future_week) # печать именинников на след неделю

if __name__ == '__main__':
    main()

