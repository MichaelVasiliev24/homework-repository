import random
import string

import pytest


@pytest.fixture
def random_text():
    """Случайный текст разной длины"""
    length = random.randint(10, 100)
    return "".join(
        random.choices(string.ascii_letters + string.digits + " \n\t", k=length)
    )


@pytest.fixture
def empty_text():
    """Пустой текст"""
    return ""


@pytest.fixture
def single_char_text():
    """Текст из одного символа"""
    return "a"


@pytest.fixture
def repeated_char_text():
    """Текст из одного повторяющегося символа"""
    return "aaaaa"


@pytest.fixture
def short_text():
    """Короткий текст"""
    return "hello world"


@pytest.fixture
def long_text():
    """Длинный текст"""
    return """Алгоритм сжатия Хаффмана широко применяется в современных технологиях.
    Этот метод позволяет эффективно уменьшить размер данных без потери информации.
    Принцип работы основан на использовании переменной длины кодов для символов:
    чем чаще символ встречается, тем короче его код."""


@pytest.fixture
def text_with_special_chars():
    """Текст со специальными символами"""
    return "Hello\nWorld\tTab\r\nSpecial\\Characters"


@pytest.fixture
def unicode_text():
    """Текст с Unicode символами"""
    return "Привет мир! Hello 世界"


@pytest.fixture
def random_binary_string():
    """Случайная бинарная строка (для тестов декодирования)"""
    length = random.randint(20, 100)
    return "".join(random.choices("01", k=length))


@pytest.fixture
def sample_huffman_codes():
    """Пример таблицы кодов Хаффмана"""
    return {"a": "0", "b": "10", "c": "11"}


@pytest.fixture
def sample_encoded_text():
    """Пример закодированного текста"""
    return "010011"


@pytest.fixture
def huffman_code_module():
    """Импорт модуля с алгоритмом Хаффмана"""

    from src.huffman_code.huffman_code import (
        build_tree,
        count_frequencies,
        decode,
        encode,
        make_codes,
    )

    return {
        "encode": encode,
        "decode": decode,
        "count_frequencies": count_frequencies,
        "build_tree": build_tree,
        "make_codes": make_codes,
    }


@pytest.fixture
def huffman_files_module():
    """Импорт модуля для работы с файлами"""

    from src.huffman_code.huffman_code_files import (
        decode_file,
        encode_file,
        load_from_binary_file,
        load_from_text_file,
        save_encoded_to_binary_file,
        save_encoded_to_text_file,
    )

    return {
        "save_encoded_to_text_file": save_encoded_to_text_file,
        "load_from_text_file": load_from_text_file,
        "save_encoded_to_binary_file": save_encoded_to_binary_file,
        "load_from_binary_file": load_from_binary_file,
        "encode_file": encode_file,
        "decode_file": decode_file,
    }
