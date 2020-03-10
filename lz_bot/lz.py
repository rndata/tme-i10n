import os
import pickle
import re

import attr
from aiogram import Bot, types
from returns.pipeline import is_successful
from returns.result import Failure, Result, Success, safe
import random

import sodeep.nns.gru_ex as gru


@attr.s
class Lz:
    bot: Bot = attr.ib()
    model = attr.ib()
    prob: float = attr.ib(0.1)

    @classmethod
    def build(cls, ckpt, bot, dp):
        lz = cls(bot=bot, model=gru.load_model(ckpt))

        dp.register_message_handler(lz.cmd_prob, commands=["prob"])
        dp.register_message_handler(lz.handler, regexp='.*')
        return lz

    async def handler(self, message: types.Message):
        me = await self.bot.me
        username = me["username"]
        print("got msg")
        if random.random() < self.prob:
            txt = gru.generate_text(self.model, message.text)
            await message.reply(txt)

        if f"@{username}" in message.text:
            print("resolving")
            txt = gru.generate_text(self.model, message.text)
            await message.reply(txt)

    async def cmd_prob(self, message: types.Message):
        args = message.get_args()
        # parts = args.split("=>")

        print("cmd", repr(args))
        prob = safe_float(args)
        if is_successful(prob):
            self.prob = prob.unwrap()
            await message.reply(f"reply prob = {self.prob}")
        else:
            await message.reply(f"failed to parse prob {prob}")


@safe
def safe_int(s: str) -> int:
    return int(s)


@safe
def safe_float(s: str) -> float:
    return float(s)
