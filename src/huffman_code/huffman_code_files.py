"""
Функции для работы с файлами в алгоритме Хаффмана.
Поддерживает два формата: текстовый и бинарный
"""

from .huffman_code import decode, encode


def save_encoded_to_text_file(text: str, filename: str) -> None:
    """Кодирование текста и сохранение в текстовый файл"""
    if not isinstance(text, str):
        raise TypeError(f"Ожидается строка для text, получен {type(text).__name__}")

    if not filename:
        raise ValueError("Имя файла не может быть пустым")

    encoded, codes = encode(text)

    # Фильтруем таблицу кодов перед сохранением
    filtered_codes = {char: code for char, code in codes.items() if char != ""}

    with open(filename, "w", encoding="utf-8") as f:
        codes_parts: list[str] = []
        for char, code in filtered_codes.items():
            # Кодируем символ в hex, чтобы избежать проблем с ":" и ","
            char_hex = char.encode("utf-8").hex()
            codes_parts.append(f"{char_hex}:{code}")

        codes_str = ",".join(codes_parts)
        f.write(codes_str + "\n")
        f.write(encoded)


def load_from_text_file(filename: str):
    """Загрузка закодированных данных из текстового файла"""
    if not filename:
        raise ValueError("Имя файла не может быть пустым")

    try:
        with open(filename, encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{filename}' не найден")
    except UnicodeDecodeError:
        raise ValueError(f"Файл '{filename}' не в формате UTF-8")

    if len(lines) < 2:
        return "", {}

    codes_line = lines[0].strip()
    codes = {}

    if codes_line:
        pairs = codes_line.split(",")
        for pair in pairs:
            if ":" in pair:
                char_hex, code = pair.split(":", 1)

                try:
                    char_bytes = bytes.fromhex(char_hex)
                    char = char_bytes.decode("utf-8")

                    if char:
                        codes[char] = code
                except (ValueError, UnicodeDecodeError):
                    # Пропускаем некорректные записи
                    continue

    encoded = lines[1].strip()
    return encoded, codes


def save_encoded_to_binary_file(text: str, filename: str) -> None:
    """Кодирование текста и сохранение в бинарный файл"""
    if not isinstance(text, str):
        raise TypeError(f"Ожидается строка для text, получен {type(text).__name__}")

    if not filename:
        raise ValueError("Имя файла не может быть пустым")

    encoded, codes = encode(text)

    # Фильтруем таблицу кодов перед сохранением
    filtered_codes = {char: code for char, code in codes.items() if char != ""}

    with open(filename, "wb") as f:
        # Кодируем таблицу кодов
        codes_parts: list[str] = []
        for char, code in filtered_codes.items():
            char_code = ord(char)
            codes_parts.append(f"{char_code}:{code}")

        codes_str = ",".join(codes_parts)
        codes_bytes = codes_str.encode("utf-8")

        f.write(len(codes_bytes).to_bytes(4, "big"))
        f.write(codes_bytes)

        encoded_length = len(encoded)
        f.write(encoded_length.to_bytes(4, "big"))

        bits = encoded
        padding = (8 - len(bits) % 8) % 8
        bits += "0" * padding

        byte_values: list[int] = []
        for i in range(0, len(bits), 8):
            byte_bits = bits[i : i + 8]
            byte_value = int(byte_bits, 2)
            byte_values.append(byte_value)

        f.write(bytes(byte_values))
        f.write(padding.to_bytes(1, "big"))


def load_from_binary_file(filename: str) -> tuple[str, dict[str, str]]:
    """Загрузка закодированных данных из бинарного файла"""
    if not filename:
        raise ValueError("Имя файла не может быть пустым")

    try:
        with open(filename, "rb") as f:
            codes_size = int.from_bytes(f.read(4), "big")

            codes_bytes = f.read(codes_size)
            if len(codes_bytes) != codes_size:
                raise ValueError("Неверный размер таблицы кодов в файле")

            codes_str = codes_bytes.decode("utf-8")

            codes: dict[str, str] = {}
            if codes_str:
                pairs = codes_str.split(",")
                for pair in pairs:
                    if pair and ":" in pair:
                        char_code_str, code = pair.split(":", 1)

                        try:
                            char_code = int(char_code_str)
                            char = chr(char_code)

                            if char:
                                codes[char] = code
                        except (ValueError, OverflowError):
                            continue

            encoded_length = int.from_bytes(f.read(4), "big")

            all_data = f.read()
            if len(all_data) < 1:
                raise ValueError("Файл поврежден: отсутствуют данные")

            padding = all_data[-1]
            data_bytes = all_data[:-1]

            bits_parts: list[str] = []
            for byte in data_bytes:
                bits_parts.append(f"{byte:08b}")

            bits = "".join(bits_parts)

            if padding > 0:
                bits = bits[:-padding]

            encoded = bits[:encoded_length]

            return encoded, codes
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{filename}' не найден")


def encode_file(input_file: str, output_file: str, binary_mode: bool = True) -> None:
    """Кодирует содержимое текстового файла"""
    if not input_file or not output_file:
        raise ValueError("Имена файлов не могут быть пустыми")

    try:
        with open(input_file, encoding="utf-8") as f:
            text = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"Входной файл '{input_file}' не найден")
    except UnicodeDecodeError:
        raise ValueError(f"Файл '{input_file}' не в формате UTF-8")

    if binary_mode:
        save_encoded_to_binary_file(text, output_file)
        print(f"Файл '{input_file}' закодирован в бинарный файл '{output_file}'")
    else:
        save_encoded_to_text_file(text, output_file)
        print(f"Файл '{input_file}' закодирован в текстовый файл '{output_file}'")


def decode_file(input_file: str, output_file: str, binary_mode: bool = True) -> None:
    """Декодирует файл, созданный encode_file"""
    if not input_file or not output_file:
        raise ValueError("Имена файлов не могут быть пустыми")

    try:
        if binary_mode:
            encoded, codes = load_from_binary_file(input_file)
        else:
            encoded, codes = load_from_text_file(input_file)
    except FileNotFoundError:
        raise FileNotFoundError(f"Файл '{input_file}' не найден")
    except Exception as e:
        raise ValueError(f"Ошибка при загрузке файла: {e}")

    # Для бинарных файлов игнорируем padding, для текстовых - нет
    text = decode(encoded, codes, ignore_trailing_bits=binary_mode)

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(text)

    print(f"Файл '{input_file}' декодирован в '{output_file}'")
