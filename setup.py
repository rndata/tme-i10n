from setuptools import setup, find_packages


setup(
    name="tme-i10n",
    version="0.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "lz-bot = lz_bot.main:main",
        ],
    },
    python_requires=">=3.8,<3.9",
    install_requires=[
        "toolz ~= 0.9",
        "fire ~= 0.2",
        "aiogram ~= 2.3",
        "attrs ~= 19.3",
    ],
)
