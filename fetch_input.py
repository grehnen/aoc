import os
import requests
from datetime import datetime
from typing import List
from dotenv import load_dotenv

load_dotenv()


def fetch_input(day: int):
    filename = f"input/d{day}.txt"
    if os.path.exists(filename):
        print(f"{filename} already exists. Skipping fetch.")
        return get_file_content(filename)

    cookie = {"session": os.getenv("SESSION_COOKIE")}

    url = f"https://adventofcode.com/2024/day/{day}/input"

    response = requests.get(url, cookies=cookie)
    response.raise_for_status()

    with open(filename, "w") as file:
        file.write(response.text)

    print(f"Content fetched and saved to {filename}")
    return get_file_content(filename)


def get_file_content(filename: str) -> List[str]:
    with open(filename, "r") as file:
        return file.read().splitlines()


if __name__ == "__main__":
    today = datetime.today().day
    fetch_input(today)
