import asyncio
from datetime import datetime

import aiohttp
import more_itertools

from models import SessionDB, UpPeople, migrate


async def get_people(id, session): # функция получения данных
    response = await session.get(f'https://swapi.dev/api/people/{id}/')
    row_data = await response.json()
    data = {}
    data['id'] = id
    data['birth_year'] = row_data['birth_year']
    data['eye_color'] = row_data['eye_color']
    data['films'] = row_data['films']
    data['gender'] = row_data['gender']
    data['hair_color'] = row_data['hair_color']
    data['height'] = row_data['height']
    data['homeworld'] = row_data['homeworld']
    data['mass'] = row_data['mass']
    data['name'] = row_data['name']
    data['skin_color'] = row_data['skin_color']
    data['species'] = row_data['species']
    data['starships'] = row_data['starships']
    data['vehicles'] = row_data['vehicles']
    return data


async def insert_people(people_list): # функция вставки в БД
    async with SessionDB() as session:
        model_list = [UpPeople(**people) for people in people_list]
        session.add_all(model_list)
        await session.commit()


async def main():
    await migrate()
    # async with aiohttp.ClientSession() as session:
    #     coros = [get_people(i, session) for i in range(1, 5)]
    #
    #     for coros_chunk in more_itertools.chunked(coros, 5):
    #         people_list = await asyncio.gather(*coros_chunk)
    #         asyncio.create_task(insert_people(people_list))
    #
    #     tasks = asyncio.all_tasks()
    #     main_task = asyncio.current_task()
    #     tasks.remove(main_task)
    #     await asyncio.gather(*tasks)


if __name__ == '__main__':
    start = datetime.now()
    asyncio.run(main())
    print(datetime.now() - start)
