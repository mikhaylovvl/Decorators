def decorator_logger(old_function):
    def new_function(*args):
        print(f"Вызвана функция {old_function} с аргументами {args}")
        result = old_function(*args)
        print(result)
        with open("logs.txt", "a", encoding="utf-8") as file:
            file.write(f"Вызвана функция {old_function} с аргументами {args} \n{result}\n")
        return result

    return new_function


