import time
import requests

CAT_URL = "https://cataas.com/cat"


def fetch(url: str) -> bytes:
    return requests.get(url).content


def save_file(data: bytes, path: str) -> None:
    with open(path, "wb") as f:
        f.write(data)


def main(count: int) -> None:
    start_time = time.perf_counter()
    for i in range(count):
        save_file(fetch(CAT_URL), f"{i}.png")
    print(f"Finished in {time.perf_counter() - start_time:.2f} seconds!")


if __name__ == '__main__':
    main(5)