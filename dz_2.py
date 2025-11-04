def get_cats_info(path):
    '''
1. Функція get_cats_info(path) приймає один аргумент - шлях до текстового файлу (path).
2. Файл містить дані про котів, де кожен запис містить унікальний ідентифікатор, ім'я кота та його вік.
3. Функція повертає список словників, де кожен словник містить інформацію про одного кота.
    '''
    koty = []
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                x, z, y = line.strip().split(',')
                koty.append({"id": x, "name": z, "age": y})
        return koty
    except FileNotFoundError:
        print('Файл не знайдено')
        return None
    except ValueError:
        print('Помилка формату даних у файлі')
        return None