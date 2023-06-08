def get_val(collection, key, default='git'):
    """
    Функция возвращает значение из словаря по переданному ключу,
    если ключ существует.
    В ином случае возвращается значение default
    :param collection: исходный словарь.
    :param key: переданный ключ.
    :param default: значение по-умолчанию.
    :return: значение по ключу или значение по-умолчанию.
    """
    if key in collection:
        return collection[key]
    else:
        return default
