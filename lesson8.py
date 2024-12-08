import logging


# logging.info("Программа запущена")
# logging.warning("Это предупреждение")
# logging.error("Это ошибка")
#
# print("Программа запущена")

# 1 zadanie
# try:
#     a = int(input())
#     b = int(input())
#     c = a/b
# except ZeroDivisionError:
#     logging.error("Это ошибка")
# except ValueError:
#     logging.error("Ошибка конвертации")
# else:
#     logging.info("с")
#     print(c)

logging.basicConfig(filename='example.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

try:
    a=int(input("Первое "))
    b=int(input("Втоое "))
    c = a/b
    logging.info("Идет деление")
except ZeroDivisionError:
    logging.error("Деление на ноль")
except ValueError:
    logging.error("Ошибка конвертации")
else:
    logging.info("Успешное деление")
    print(c)