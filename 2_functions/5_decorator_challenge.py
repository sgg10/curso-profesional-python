"""Decorators Challenge"""

# Multiprocess and threads
import logging
import multiprocessing
import threading

# Utils
from datetime import datetime, timedelta
from random import randint
from time import sleep
from typing import Union

import requests

logging.basicConfig(level=logging.DEBUG, format="%(message)s")

RUN_TYPE = Union[float, int]


def thread_worker(name: str, run_every: RUN_TYPE = 0, daemon=False):
    logging.debug(f"Registered {name} worker.")

    def with_worker(function):
        def wrapper(*args, **kwargs):
            def process(*args, **kwargs):
                while True:
                    initial_time = datetime.now()
                    function(*args, **kwargs)
                    tf = datetime.now() - initial_time
                    logging.debug(f"{name} finished in {tf.total_seconds()}s")
                    sleep(run_every)

            threading.Thread(
                target=process,
                name=function.__name__,
                args=args,
                kwargs=kwargs,
                daemon=daemon,
            ).start()

        return wrapper

    return with_worker


def process_worker(name: str, run_every: RUN_TYPE = 0, daemon=False):
    logging.debug(f"Registered {name} worker.")

    def with_worker(function):
        def wrapper(*args, **kwargs):
            def process(*args, **kwargs):
                while True:
                    initial_time = datetime.now()
                    function(*args, **kwargs)
                    tf = datetime.now() - initial_time
                    logging.debug(f"{name} finished in {tf.total_seconds()}s")
                    sleep(run_every)

            multiprocessing.Process(
                target=process,
                name=function.__name__,
                args=args,
                kwargs=kwargs,
                daemon=daemon,
            ).start()

        return wrapper

    return with_worker


def worker(name: str, run_every: RUN_TYPE = 0):
    logging.debug(f"Registered {name} worker.")

    def with_worker(function):
        def wrapper(*args, **kwargs):
            while True:
                initial_time = datetime.now()
                function(*args, **kwargs)
                tf = datetime.now() - initial_time
                logging.debug(f"{name} finished in {tf.total_seconds()}s")
                sleep(run_every)

        return wrapper

    return with_worker


@thread_worker(name="say_hi", run_every=3, daemon=True)
def say_hi(name):
    logging.info(f"Hi, {name}!")


@process_worker(name="random_character", run_every=5, daemon=False)
def get_character():
    id = randint(1, 671)
    res = requests.get(f"https://rickandmortyapi.com/api/character/{id}")
    if res.status_code == 200:
        name = res.json().get("name")
        logging.info(name)


@worker(name="Pokemons", run_every=timedelta(seconds=2).total_seconds())
def get_pokemon(limit: int):
    if limit >= 1118:
        limit = 1118
    id = randint(1, limit)
    res = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")
    if res.status_code == 200:
        result = res.json()
        name = result.get("forms")[0].get("name")
        logging.info(name)


if __name__ == "__main__":
    say_hi("Sebastian")  # Run worker as a thread automaticity
    get_character()  # Run worker as a process automaticity

    """
    With worker decorator we need to create manually a process
    or thread to execute. Or only run a function
    but that function block the main process and main thread,
    for this reason is better create a new procees or thread.
    """
    process = multiprocessing.Process(target=get_pokemon, args=(151,))
    process.start()
