def decorator_logs(path_to_log):
    def _decorator_logs(old_function):
        def new_function(*args):
            print(f"Вызвана функция {old_function} с аргументами {args}")
            result = old_function(*args)
            print(result)
            with open(path_to_log, "a") as file:
                file.write(f"Вызвана функция {old_function} с аргументами {args}\n{result}\n")
            return result

        return new_function

    return _decorator_logs
