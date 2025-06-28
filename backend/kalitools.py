import requests  # Импортируем библиотеку для выполнения HTTP-запросов
from pyfiglet import Figlet  # Импортируем библиотеку для отображения текста в стиле ASCII
import folium  # Импортируем библиотеку для создания интерактивных карт
import time  # Импортируем модуль для работы с задержками и временем


# Функция получения информации по IP-адресу
def get_info_by_ip(ip="127.0.0.1"):
    try:
        # Выполняем GET-запрос к API для получения данных по IP и преобразуем ответ в JSON
        response = requests.get(url=f"http://ip-api.com/json/{ip}").json()

        # Создаем словарь с нужными данными, полученными из ответа API
        data = {
            "[IP]": response.get("query"),  # IP-адрес
            "[Int prov]": response.get("isp"),  # Интернет-провайдер (ISP)
            "[Org]": response.get("org"),  # Организация
            "[Country]": response.get("country"),  # Страна
            "[Region Name]": response.get("regionName"),  # Регион/область
            "[City]": response.get("city"),  # Город
            "[ZIP]": response.get("zip"),  # Почтовый индекс
            "[Lat]": response.get("lat"),  # Широта
            "[Lon]": response.get("lon"),  # Долгота
            "[Status]": response.get("status"),  # Статус запроса (успех/ошибка)
            "[Timezone]": response.get("timezone"),  # Часовой пояс
            "[AS]": response.get("as"),  # Autonomous System (AS)
        }

        # Выводим полученные данные по каждому ключу и значению
        for k, v in data.items():
            print(f" {k} : {v}")

        # Создаем карту с помощью folium, центрируя ее на координатах IP-адреса
        area = folium.Map(
            location=[response.get("lat"), response.get("lon")],  # Центр карты — координаты IP
            tiles="Stamen Terrain",  # Тип карты (тропический стиль)
            attr="Map data &copy; OpenStreetMap contributors, CC-BY-SA, Imagery © Stamen Design",  # Атрибуция картографических данных
        )
        tooltip = "Click me!"  # Текст подсказки при наведении на маркер

        # Добавляем маркер на карту по координатам IP с всплывающей подсказкой
        folium.Marker(
            [response.get("lat"), response.get("lon")], popup="<i>Mt. Hood Meadows</i>", tooltip=tooltip
        ).add_to(area)

        # Сохраняем карту в HTML-файл с именем, основанным на IP и городе
        area.save(f"{response.get('query')}_{response.get('city')}.html")
    except requests.exceptions.ConnectionError:
        print("[!] Please check your connection!")  # Сообщение об ошибке при отсутствии соединения

# Функция отображения текста с рамкой в стиле ASCII-art
def print_with_border(text, border_char='_'):
    f = Figlet(font='slant')  # Создаем объект Figlet с выбранным шрифтом 'slant'
    ascii_art = f.renderText(text)  # Генерируем ASCII-арт из текста

    lines = ascii_art.split('\n')  # Разбиваем ASCII-арт на строки для обработки по отдельности
    max_length = max(len(line) for line in lines)  # Находим длину самой длинной строки

    print(border_char * (max_length + 2))  # Верхняя граница рамки

    for line in lines:
        print(border_char + line.ljust(max_length) + border_char)  
        # Выводим каждую строку с рамкой по бокам, дополняя пробелами до максимальной длины

    print(border_char * (max_length + 2))  # Нижняя граница рамки

# Основная функция меню выбора действия пользователя
def probiv():
    print_with_border('\nДобро пожаловать в Бета-версию приложения Kali tools')  
    print('                                 Авторы: MRX, Jorh')
    print("\n1) Пробив во ФИО🙎 (В разработке)")   # В разработке: поиск по ФИО
    print("2) Пробив по телефону📱 (В разработке)")   # В разработке: поиск по телефону
    print("3) Пробив по ВК💠  (В разработке)")   # В разработке: поиск по ВК
    print("4) Пробив по Email📧 (В разработке)")   # В разработке: поиск по Email
    print("5) Пробив по ip (доступно)")   # Доступная функция — поиск информации по IP

    a = int(input('\nВведите цифру способа пробива(1🙎, 2📱, 3💠, 4📧,5): '))  
    # Пользователь вводит номер выбранного способа поиска

    if a == 5:
        print("\nВведите ip адрес")
        ip_address = input("IP адрес: ")  
        get_info_by_ip(ip=ip_address)  
        # Вызов функции получения информации по IP

    elif a == 2:
        print()
        print("Введи номер. Пример:+7XXXXXXXXXX,7XXXXXXXXXX")  
        # Пока что тут только сообщение о необходимости ввести номер телефона (функция не реализована)

    

    elif a ==4:
        print()
        print("Введи почту. Пример:123456789@gmail.com")  
        # Аналогично — предполагается обработка email, но функция не реализована

    elif a ==1:
        print()
        print("Введите ФИО. Пример ИВАНОВ ИВАН ИВАНОВИЧ")
        
        # Определяем функцию поиска ФИО в базе данных файла "database.txt"
        def найти_в_базе(фио, файл_базы):
            with open("database.txt", 'r', encoding='utf-8') as база:
                for строка in база:
                    if фио in строка:
                        return строка.strip().split('\t')  
                        # Предполагается разделение данных табуляцией и возврат списка данных
        
            return None
        
        # Основная функция поиска и вывода информации о человеке из базы данных
        def main():
            файл_базы = 'database.txt'
            фио = input('Введите ФИО: ')
            print('Ищем обидчика🔎')
            time.sleep(2)
            результат = найти_в_базе(фио, файл_базы)

            if результат:
                print(f'\nДанные по ФИО "{фио}":')
                print(f'ФИО: {результат[0]}')
                print(f'Дата рождения держателя: {результат[1]}')
                print(f'Паспорт: {результат[2]}')
                print(f'Номер карты: {результат[3]}')
                print(f'Срок действия карты: {результат[4]}')
                print(f'Адрес работы: {результат[11]}')
                print(f'Место работы: {результат[13]}')
                print(f'Почтовый индекс: {результат[14]}')
                print(f'Регион: {результат[15]}')
                print(f'Город: {результат[17]}')
                print(f'Район: {результат[16]}')
                print(f'Улица: {результат[19]}')
                print(f'Номер дома: {результат[20]}')
                # Выводим найденные данные из базы (предполагается структура файла)
            else:
                print(f'ФИО "{фио}" не найдено в базе данных.')
        
        if __name__ == '__main__':
            main()   # Запускаем функцию поиска при запуске этого блока
        
    else:
        print('\nНе верная команда')   # Обработка некорректного ввода
    
# Стартовое окно — проверка пароля перед входом в программу
password = input('Введите пароль: ')
if password == '1234':
    probiv()   # Если пароль правильный — запускаем меню поиска/пробива 
else:
    print('Доступ отказан (Неверный пароль)')   # Неверный пароль — отказ в доступе