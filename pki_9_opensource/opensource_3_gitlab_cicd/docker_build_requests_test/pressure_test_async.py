import requests
import asyncio

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


async def pressure_test(host, id):
    # print(f'ID: {id} Started')
    result = await loop.run_in_executor(None, requests.get, host)
    # print(f'ID: {id} Stopped')
    return result.status_code


def pressure_test_main(conns, url):
    tasks = []

    for i in range(conns):
        task = loop.create_task(pressure_test(url, i))
        tasks.append(task)

    loop.run_until_complete(asyncio.wait(tasks))

    result_list = []
    for i in tasks:
        result_list.append(i.result())

    return result_list


if __name__ == '__main__':
    print(pressure_test_main(10, 'https://nginix.dcloud.cisco.com.com'))
