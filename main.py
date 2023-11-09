# Проверить, что строка является синтаксически корректным номером телефона.

import re

REGEX = re.compile(
    r"^((\+\d{1,4})|(\d{1,4}))(([ -]\d{3})|(\(\d{3}\))|\d{3})(([ -]?\d{3}[ -]\d{2}[ -]\d{2})|([ -]?\d{7})|\d{7})$")


def validatePhoneNumber(Number):
    if re.match(REGEX, Number):
        return True
    else:
        return False


print("Введите номер телефона: ")
phoneNumber = input()

if validatePhoneNumber(phoneNumber):
    print("Телефонный номер является синтаксически корректным номером телефона")
else:
    print("Телефонный номер является синтаксически некорректным номером телефона")
