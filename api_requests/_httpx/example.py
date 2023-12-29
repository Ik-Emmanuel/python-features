from typing import Any
import time
import httpx
import asyncio

BASE_URL = "https://httpbin.org"

# def fetch_get() -> Any:
#     response = httpx.get(f"{BASE_URL}/get")
#     return response.json()

def fetch_get(client: httpx.Client) -> Any:
    response = client.get(f"{BASE_URL}/get")
    return response.json()

async def aysnc_fetch_get(client: httpx.AsyncClient) -> Any:
    response = await client.get(f"{BASE_URL}/get")
    return response.json()

# ---

# def fetch_post() -> Any:
#     data_to_post = {"key": "value"}
#     response = httpx.post(f"{BASE_URL}/post", json=data_to_post)
#     return response.json()

def fetch_post(client: httpx.Client) -> Any:
    data_to_post = {"key": "value"}
    response = client.post(f"{BASE_URL}/post", json=data_to_post)
    return response.json()


async def async_fetch_post(client: httpx.AsyncClient):
    data_to_post = {"key": "value"}
    response = await client.post(f"{BASE_URL}/post", json=data_to_post)
    return response.json()

# ---

# def fetch_put() -> Any:
#     data_to_put = {"key": "updated_value"}
#     response = httpx.put(f"{BASE_URL}/put", json=data_to_put)
#     return response.json()

def fetch_put(client: httpx.Client) -> Any:
    data_to_put = {"key": "updated_value"}
    response = client.put(f"{BASE_URL}/put", json=data_to_put)
    return response.json()


async def async_fetch_put(client: httpx.AsyncClient):
    data_to_put = {"key": "updated_value"}
    response = await client.put(f"{BASE_URL}/put", json=data_to_put)
    return response.json()

# ---

# def fetch_delete() -> Any:
#     response = httpx.delete(f"{BASE_URL}/delete")
#     return response.json()

def fetch_delete(client: httpx.Client) -> Any:
    response = client.delete(f"{BASE_URL}/delete")
    return response.json()


async def async_fetch_delete(client: httpx.AsyncClient):
    response = await client.delete(f"{BASE_URL}/delete")
    return response.json()

def main_sync() -> None:

    start = time.perf_counter()
    # print("GET:", fetch_get())
    # print("POST:", fetch_post())
    # print("PUT:", fetch_put())
    # print("DELETE:", fetch_delete())

    with httpx.Client() as client:
        print("GET:", fetch_get(client))
        print("POST:", fetch_post(client))
        print("PUT:", fetch_put(client))
        print("DELETE:", fetch_delete(client))

    end = time.perf_counter()
    print(f"Time taken: {end - start:.2f} seconds.")

async def main_async():
    # record the starting time
    start = time.perf_counter()

    async with httpx.AsyncClient() as client:
        tasks = [
            aysnc_fetch_get(client),
            async_fetch_post(client),
            async_fetch_put(client),
            async_fetch_delete(client),
        ]
        results = await asyncio.gather(*tasks)

    for result in results:
        print(result)

    # record the ending time
    end = time.perf_counter()
    print(f"Time taken: {end - start:.2f} seconds.")



if __name__ == "__main__":
    main_sync()
    # or 
    # asyncio.run(main_async())