import asyncio
from datetime import datetime

import aiohttp
import more_itertools

from models import SessionDB, UpPeople, migrate


async def get_people(id_people, session):
    response = await session.get(f'https://swapi.dev/api/people/{id_people}/')
    data = await response.json()
    data['id'] = id_people

    if data:
        films = []
        for film_url in data.get('films', []):
            resp = await session.get(film_url)
            film = await resp.json()
            films.append(film.get('title'))
        data['films'] = ', '.join(films)

        species = []
        for specie_url in data.get('species', []):
            resp = await session.get(specie_url)
            specie = await resp.json()
            species.append(specie.get('name'))
        data['species'] = ', '.join(species)

        starships = []
        for starship_url in data.get('starships', []):
            resp = await session.get(starship_url)
            starship = await resp.json()
            starships.append(starship.get('name'))
        data['starships'] = ', '.join(starships)

        vehicles = []
        for vehicle_url in data.get('vehicles', []):
            resp = await session.get(vehicle_url)
            vehicle = await resp.json()
            vehicles.append(vehicle.get('name'))
        data['vehicles'] = ', '.join(vehicles)

    return data


async def insert_people(people_list):
    async with SessionDB() as session:
        model_list = [
            UpPeople(
                id=people_dict.get('id'),
                birth_year=people_dict.get('birth_year'),
                eye_color=people_dict.get('eye_color'),
                films=people_dict.get('films'),
                gender=people_dict.get('gender'),
                hair_color=people_dict.get('hair_color'),
                height=people_dict.get('height'),
                homeworld=people_dict.get('homeworld'),
                mass=people_dict.get('mass'),
                name=people_dict.get('name'),
                skin_color=people_dict.get('skin_color'),
                species=people_dict.get('species'),
                starships=people_dict.get('starships'),
                vehicles=people_dict.get('vehicles')
            ) for people_dict in people_list
        ]

        session.add_all(model_list)
        await session.commit()


async def main():
    await migrate()

    async with aiohttp.ClientSession() as session:

        coros = [get_people(i, session) for i in range(1, 85)]

        for coros_chunk in more_itertools.chunked(coros, 5):
            people_list = await asyncio.gather(*coros_chunk)
            asyncio.create_task(insert_people(people_list))

        tasks = asyncio.all_tasks()
        main_task = asyncio.current_task()
        tasks.remove(main_task)
        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = datetime.now()
    asyncio.run(main())
    stop = datetime.now()
    print(stop - start)
