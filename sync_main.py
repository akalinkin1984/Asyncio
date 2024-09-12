import requests
from datetime import datetime

from sync_models import SessionDB, UpPeople, create_tables, engine


def get_data(url):
    response = requests.get(url)
    return response.json()


def insert_data():
    for i in range(1, 85):
        url = f'https://swapi.dev/api/people/{i}/'
        data = get_data(url)

        if data:
            films = []
            for film_url in data.get('films', []):
                film = get_data(film_url).get('title')
                films.append(film)
            films = ', '.join(films)

            species = []
            for specie_url in data.get('species', []):
                specie = get_data(specie_url).get('name')
                species.append(specie)
            species = ', '.join(species)

            starships = []
            for starship_url in data.get('starships', []):
                starship = get_data(starship_url).get('name')
                starships.append(starship)
            starships = ', '.join(starships)

            vehicles = []
            for vehicle_url in data.get('vehicles', []):
                vehicle = get_data(vehicle_url).get('name')
                vehicles.append(vehicle)
            vehicles = ', '.join(vehicles)

        with SessionDB() as session:
            people = UpPeople(id=i,
                              birth_year=data.get('birth_year'),
                              eye_color = data.get('eye_color'),
                              films = films,
                              gender = data.get('gender'),
                              hair_color = data.get('hair_color'),
                              height = data.get('height'),
                              homeworld = data.get('homeworld'),
                              mass = data.get('mass'),
                              name = data.get('name'),
                              skin_color = data.get('skin_color'),
                              species = species,
                              starships = starships,
                              vehicles = vehicles,
            )
            session.add(people)
            session.commit()


create_tables(engine)

start = datetime.now()
insert_data()
print(datetime.now() - start)
