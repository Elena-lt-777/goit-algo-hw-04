def parse_input(user_input):
    '''
функція parse_input() розбирає введений користувачем рядок на команду та її аргументи. 
Команди та аргументи мають бути розпізнані незалежно від регістру введення.
    '''
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    '''
    За цією командою бот зберігає у пам'яті новий контакт. 
    Користувач вводить ім'я username та номер телефону phone, обов'язково через пробіл.
    '''
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_username_phone(args, contacts):
    '''
    За цією командою бот зберігає в пам'яті новий номер телефону phone для контакту username,
     що вже існує в записнику.
    '''
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact non updated."

def show_phone(args, contacts):
    '''
    За цією командою бот виводить у консоль номер телефону для зазначеного контакту username.
    '''
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return "Ім'я не знайдено."
    
def show_all(contacts):
    '''
    За цією командою бот виводить всі збереженні контакти з номерами телефонів у консоль.
    '''
    if not contacts:
        return "Список пуст."
    else:
        return contacts

def main():
    '''
Бот завершує свою роботу, якщо зустрічає слова: "close" або "exit".
Бот не чутливий до регістру введених команд.
Бот приймає команди:
"hello", та відповідає у консоль повідомленням "How can I help you?"
    '''
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_username_phone(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
