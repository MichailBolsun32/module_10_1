# Необходимо создать функцию write_words(word_count, file_name),
# где word_count - количество записываемых слов, file_name - название файла, куда будут записываться слова.
# Функция должна вести запись слов "Какое-то слово № <номер слова по порядку>" в соответствующий файл
# с прерыванием после записи каждого на 0.1 секунду.
# Сделать паузу можно при помощи функции sleep из модуля time,
# предварительно импортировав её: from time import sleep.
# В конце работы функции вывести строку "Завершилась запись в файл <название файла>".
import time
from time import sleep
from datetime import datetime
from threading import Thread # Для мультипоточной работы


def write_words(word_count, file_name):
    with open(str(file_name), 'w', encoding='UTF-8') as file:
        for num in range(word_count):
            file.write(f'Какое-то слово № {num + 1}\n')
            time.sleep(0.1)
    print('Завершилась запись в файл', file_name)

time_start = datetime.now()

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

time_end = datetime.now()
time_res = time_end - time_start
print('Работа потоков', time_res)

time_start = datetime.now()

# инициализация потоков
thr_first = Thread(target=write_words, args=(10, 'example5.txt'))
thr_second = Thread(target=write_words, args=(30, 'example6.txt'))
thr_third = Thread(target=write_words, args=(200, 'example7.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example8.txt'))

# запуск потоков
thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

# ожидаем завершения потоков
thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()

time_end = datetime.now()
time_res = time_end - time_start
print('Работа потоков', time_res)