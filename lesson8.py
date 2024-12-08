import logging


logging.basicConfig(level=logging.INFO)

# logging.info("Программа запущена")
# logging.warning("Это предупреждение")
# logging.error("Это ошибка")
#
# print("Программа запущена")

# 1 zadanie
try:
    a = int(input())
    b = int(input())
    c = a/b
except ZeroDivisionError:
    logging.error("Это ошибка")
else:
    print(c)