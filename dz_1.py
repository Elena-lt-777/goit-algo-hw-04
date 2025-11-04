def total_salary(path):
    '''
1. Функція total_salary(path) приймає один аргумент - шлях до текстового файлу (path).
2. Файл містить дані про заробітні плати розробників, розділені комами. 
Кожен рядок вказує на одного розробника.
3. Функція аналізує файл, обчислює загальну та середню суму заробітної плати.
4. Результатом роботи функції є кортеж із двох чисел: 
загальної суми зарплат і середньої заробітної плати.

    '''

    num_devolop = 0
    sum_zp = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                y, z = line.strip().split(',')
                num_devolop += 1
                sum_zp += int(z)
            sred_zp = round(sum_zp / num_devolop)
            return sum_zp, sred_zp
    except FileNotFoundError:
        print('Файл не знайдено')
        return None, None
    except ValueError:
        print('Помилка формату даних у файлі')
        return None, None