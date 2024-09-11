import requests

from sync_models import SessionDB, UpPeople, create_tables, engine


def get_data(url):
    response = requests.get(url)
    return response.json()


def insert_data():
    url = 'https://swapi.dev/api/people/'
    for i in range(1, 85):
        data = get_data(url + f'{str(i)}/')
        with SessionDB() as session:
            people = UpPeople(id=i,
                              birth_year=data.get('birth_year'),
                              eye_color = data.get('eye_color'),
                              films = data.get('films'),
                              gender = data.get('gender'),
                              hair_color = data.get('hair_color'),
                              height = data.get('height'),
                              homeworld = data.get('homeworld'),
                              mass = data.get('mass'),
                              name = data.get('name'),
                              skin_color = data.get('skin_color'),
                              species = data.get('species'),
                              starships = data.get('starships'),
                              vehicles = data.get('vehicles'),
            )
            session.add(people)
            session.commit()


create_tables(engine)
insert_data()