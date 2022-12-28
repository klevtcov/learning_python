def create_record(name, telephone, adress):
    '''create record'''
    record = {
        'name': name,
        'telephone': telephone,
        'adress': adress
    }
    return record


def give_avard(medal, *persons):
    '''give medals to persons'''
    for person in persons:
        print('Tovarisch', person.title(), 'nagrazhdaetsya', medal)


user1 = create_record('Vasya', '+765465546546', 'Tuniss')
user2 = create_record('Petya', '+98765465', 'Manis')

print(user1)
print(user2)

give_avard('Za Berlin', 'Vasya', 'Petya')
give_avard('Za London', 'Alex', 'Petya', 'Andrey')


