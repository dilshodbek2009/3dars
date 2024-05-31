from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="User"))
    return rkm


def next_menu():
    rkm = ReplyKeyboardMarkup(resize_keyboard=True)
    rkm.row(KeyboardButton(text="Product"), KeyboardButton(text="View users"))
    return rkm