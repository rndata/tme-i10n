import os
import re
import pickle

import attr
from aiogram import Bot, types


@attr.s
class Lz:
    path: str = attr.ib()
    bot: Bot = attr.ib()
    state = attr.ib()

    @classmethod
    def build(cls, path, bot, dp):
        if os.path.isfile(path):
            state = cls.read_state(path)
        else:
            state = dict()
        lz = cls(path=path, bot=bot, state=state)
        lz.save_state()

        dp.register_message_handler(lz.command, commands=["add"])
        dp.register_message_handler(lz.handler, regexp='.*')
        return lz

    @classmethod
    def read_state(cls, path):
        with open(path, 'rb') as f:
            return pickle.load(f)

    @classmethod
    def write_state(cls, data, path):
        with open(path, 'wb') as f:
            return pickle.dump(data, f)

    def load_state(self):
        self.state = Lz.read_state(self.path)

    def save_state(self):
        Lz.write_state(self.state, self.path)

    def resolve_reply(self, txt):
        for k, v in self.state.items():
            if k.match(txt):
                return v

    async def handler(self, message: types.Message):
        me = await self.bot.me
        username = me["username"]
        if f"@{username}" in message.text:
            print("resolving")
            reply = self.resolve_reply(message.text)

            if reply:
                await message.reply(reply)

    async def command(self, message: types.Message):
        args = message.get_args()
        parts = args.split("=>")
        if len(parts) < 2:
            await message.reply("2 args need")
        else:
            regex, val, *_ = parts
            r = re.compile(regex)
            self.state[r] = val
            self.save_state()
            await message.reply(f"Added {r} => {val}")
