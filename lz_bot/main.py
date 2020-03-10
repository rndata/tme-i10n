import os
import sys
import logging

import fire
from aiogram import Bot, Dispatcher, types, executor

import w2v.tfidf as w
from .lz import Lz

logging.basicConfig(level=logging.INFO)


def launch_bot(ckpt_file):
    token = os.getenv("TME_API_TOKEN")
    if token is None:
        print("TME_API_TOKEN is empty, token required")
        sys.exit(1)

    bot = Bot(token=token)
    dp = Dispatcher(bot)

    lz_bot = Lz.build(ckpt=ckpt_file, bot=bot, dp=dp)

    executor.start_polling(dp, skip_updates=True)


def main():
    fire.Fire({
        "run": launch_bot,
    })
