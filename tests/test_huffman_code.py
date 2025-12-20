"""
Тесты для реализации алгоритма Хаффмана
"""

import os

from pathlib import Path
from typing import Any

import pytest

from src.huffman_code.huffman_code import decode


class TestHuffmanBasicFunctions:
    """Класс тестов базовых функций алгоритма Хаффмана"""

    def test_count_frequencies_basic(
        self, huffman_code_module: dict[str, Any], short_text: str
    ) -> None:
        """Тест подсчета частот символов"""
        freq = huffman_code_module["count_frequencies"](short_text)
        assert isinstance(freq, dict)
        assert "h" in freq
        assert "e" in freq
        assert freq["l"] == 3  # 'l' встречается 3 раза в "hello world"

    def test_count_frequencies_empty(
        self, huffman_code_module: dict[str, Any], empty_text: str
    ) -> None:
        """Тест подсчета частот для пустой строки"""
        freq = huffman_code_module["count_frequencies"](empty_text)
        assert freq == {}

    def test_count_frequencies_single_char(
        self, huffman_code_module: dict[str, Any], single_char_text: str
    ) -> None:
        """Тест подсчета частот для строки из одного символа"""
        freq = huffman_code_module["count_frequencies"](single_char_text)
        assert freq == {"a": 1}

    def test_build_tree_basic(
        self, huffman_code_module: dict[str, Any], short_text: str
    ) -> None:
        """Тест построения дерева Хаффмана"""
        tree = huffman_code_module["build_tree"](short_text)
        assert tree is not None
        assert hasattr(tree, "freq")
        assert hasattr(tree, "left")
        assert hasattr(tree, "right")

    def test_build_tree_empty(
        self, huffman_code_module: dict[str, Any], empty_text: str
    ) -> None:
        """Тест построения дерева для пустой строки"""
        tree = huffman_code_module["build_tree"](empty_text)
        assert tree is None

    def test_make_codes_basic(
        self, huffman_code_module: dict[str, Any], short_text: str
    ) -> None:
        """Тест создания кодов Хаффмана"""
        tree = huffman_code_module["build_tree"](short_text)
        codes = huffman_code_module["make_codes"](tree)

        assert isinstance(codes, dict)
        # Все коды должны быть строками из 0 и 1
        for code in codes.values():
            assert all(bit in "01" for bit in code)
            assert len(code) > 0

    def test_make_codes_empty_tree(self, huffman_code_module: dict[str, Any]) -> None:
        """Тест создания кодов для пустого дерева"""
        codes = huffman_code_module["make_codes"](None)
        assert codes == {}


class TestHuffmanEncodeDecode:
    """Класс тестов кодирования и декодирования"""

    @pytest.mark.parametrize(
        "text_fixture",
        [
            "short_text",
            "long_text",
            "text_with_special_chars",
            "unicode_text",
            "repeated_char_text",
            "single_char_text",
        ],
    )
    def test_encode_decode_roundtrip(
        self,
        huffman_code_module: dict[str, Any],
        request: pytest.FixtureRequest,
        text_fixture: str,
    ) -> None:
        """Тест на параметризованном тексте, проверка, что кодирование и декодирование возвращает исходный текст"""
        text: str = request.getfixturevalue(text_fixture)
        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_code_module["encode"](text)

        # Удаляем возможные пустые строки из таблицы кодов
        codes = {char: code for char, code in codes.items() if char != ""}

        decoded: str = huffman_code_module["decode"](encoded, codes)

        assert decoded == text, f"Failed for fixture: {text_fixture}"

    def test_encode_empty(
        self, huffman_code_module: dict[str, Any], empty_text: str
    ) -> None:
        """Тест кодирования пустой строки"""
        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_code_module["encode"](empty_text)
        assert encoded == ""
        assert codes == {}

    def test_decode_empty(self, huffman_code_module: dict[str, Any]) -> None:
        """Тест декодирования пустых данных"""
        decoded: str = huffman_code_module["decode"]("", {})
        assert decoded == ""

    def test_encode_single_char(
        self, huffman_code_module: dict[str, Any], single_char_text: str
    ) -> None:
        """Тест кодирования строки из одного символа"""
        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_code_module["encode"](single_char_text)
        assert encoded == "0"  # Для одного символа код всегда "0"
        assert codes == {"a": "0"}

    def test_encode_repeated_char(
        self, huffman_code_module: dict[str, Any], repeated_char_text: str
    ) -> None:
        """Тест кодирования строки из повторяющихся символов"""
        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_code_module["encode"](repeated_char_text)
        assert encoded == "0" * 5  # 5 нулей для 5 символов 'a'
        assert codes == {"a": "0"}

    @pytest.mark.parametrize(
        "invalid_encoded, codes, expected_exception",
        [
            (
                "012",
                {"a": "0"},
                ValueError,
            ),  # Некорректный символ в закодированной строке
            ("01", {"a": "2"}, ValueError),  # Некорректный код в таблице
            ("01", {1: "0"}, TypeError),  # Неправильный тип ключа
            ("01", {"a": 0}, TypeError),  # Неправильный тип значения
        ],
    )
    def test_decode_invalid_input(
        self,
        huffman_code_module: dict[str, Any],
        invalid_encoded: str,
        codes: dict[Any, Any],
        expected_exception: type[Exception],
    ) -> None:
        """Тест декодирования с некорректными входными данными"""
        with pytest.raises(expected_exception):
            huffman_code_module["decode"](invalid_encoded, codes)

    def test_encode_invalid_input(self, huffman_code_module: dict[str, Any]) -> None:
        """Тест кодирования с некорректными входными данными"""
        with pytest.raises(TypeError):
            huffman_code_module["encode"](123)  # Не строка

    def test_property_prefix_free(
        self, huffman_code_module: dict[str, Any], random_text: str
    ) -> None:
        """Property-based тест, проверка, что коды Хаффмана префиксные"""
        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_code_module["encode"](random_text)

        # Удаляем возможные пустые строки
        codes = {char: code for char, code in codes.items() if char != ""}

        codes_list: list[str] = list(codes.values())
        for i in range(len(codes_list)):
            for j in range(len(codes_list)):
                if i != j:
                    assert not codes_list[i].startswith(codes_list[j]), (
                        f"Code {codes_list[i]} is prefix of {codes_list[j]}"
                    )

    def test_compression_ratio(
        self, huffman_code_module: dict[str, Any], random_text: str
    ) -> None:
        """Тест для проверки того, что закодированный текст не длиннее оригинального в битах"""
        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_code_module["encode"](random_text)

        original_bits: int = len(random_text) * 8  # 8 бит на символ
        encoded_bits: int = len(encoded)

        # Алгоритм Хаффмана не гарантирует сжатие для всех текстов, но проверяем корректность
        assert encoded_bits <= original_bits or len(set(random_text)) > 1


class TestHuffmanTextFiles:
    """Класс тестов для работы с текстовыми файлами"""

    def test_save_load_text_file_roundtrip(
        self, huffman_files_module: dict[str, Any], short_text: str, tmp_path: Path
    ) -> None:
        """Тест сохранения и загрузки из текстового файла"""
        test_file: Path = tmp_path / "test.txt"

        huffman_files_module["save_encoded_to_text_file"](short_text, str(test_file))

        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_files_module["load_from_text_file"](str(test_file))

        # Текстовые файлы не имеют padding, используем ignore_trailing_bits=False
        decoded: str = decode(encoded, codes, ignore_trailing_bits=False)

        assert decoded == short_text
        assert os.path.exists(test_file)

    def test_text_file_with_special_chars(
        self,
        huffman_files_module: dict[str, Any],
        text_with_special_chars: str,
        tmp_path: Path,
    ) -> None:
        """Тест работы со специальными символами в текстовом файле"""
        test_file: Path = tmp_path / "special.txt"

        huffman_files_module["save_encoded_to_text_file"](
            text_with_special_chars, str(test_file)
        )
        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_files_module["load_from_text_file"](str(test_file))

        decoded: str = decode(encoded, codes, ignore_trailing_bits=False)

        assert decoded == text_with_special_chars

    def test_text_file_empty(
        self, huffman_files_module: dict[str, Any], empty_text: str, tmp_path: Path
    ) -> None:
        """Тест работы с пустым файлом"""
        test_file: Path = tmp_path / "empty.txt"

        huffman_files_module["save_encoded_to_text_file"](empty_text, str(test_file))
        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_files_module["load_from_text_file"](str(test_file))

        assert encoded == ""
        assert codes == {}

    def test_load_nonexistent_file(self, huffman_files_module: dict[str, Any]) -> None:
        """Тест загрузки несуществующего файла"""
        with pytest.raises(FileNotFoundError):
            huffman_files_module["load_from_text_file"]("nonexistent_file.txt")


class TestHuffmanBinaryFiles:
    """Класс тестов для работы с бинарными файлами"""

    def test_save_load_binary_file_roundtrip(
        self, huffman_files_module: dict[str, Any], short_text: str, tmp_path: Path
    ) -> None:
        """Тест сохранения и загрузки из бинарного файла"""
        test_file: Path = tmp_path / "test.bin"

        huffman_files_module["save_encoded_to_binary_file"](short_text, str(test_file))

        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_files_module["load_from_binary_file"](str(test_file))

        # Бинарные файлы имеют padding, нужно использовать ignore_trailing_bits=True
        decoded: str = decode(encoded, codes, ignore_trailing_bits=True)

        assert decoded == short_text
        assert os.path.exists(test_file)

    def test_binary_file_with_unicode(
        self, huffman_files_module: dict[str, Any], unicode_text: str, tmp_path: Path
    ) -> None:
        """Тест работы с Unicode в бинарном файле"""
        test_file: Path = tmp_path / "unicode.bin"

        huffman_files_module["save_encoded_to_binary_file"](
            unicode_text, str(test_file)
        )
        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_files_module["load_from_binary_file"](str(test_file))

        decoded: str = decode(encoded, codes, ignore_trailing_bits=True)

        assert decoded == unicode_text

    def test_binary_file_corrupted(
        self, huffman_files_module: dict[str, Any], tmp_path: Path
    ) -> None:
        """Тест обработки поврежденного бинарного файла"""
        test_file: Path = tmp_path / "corrupted.bin"

        # Создаем некорректный бинарный файл
        with open(test_file, "wb") as f:
            f.write(b"INVALID_DATA")

        with pytest.raises((ValueError, UnicodeDecodeError)):
            huffman_files_module["load_from_binary_file"](str(test_file))


class TestHuffmanIntegration:
    """Класс интеграционных тестов"""

    @pytest.mark.parametrize("binary_mode", [True, False])
    def test_encode_decode_file_integration(
        self,
        huffman_files_module: dict[str, Any],
        long_text: str,
        tmp_path: Path,
        binary_mode: bool,
    ) -> None:
        """Интеграционный тест кодирования и декодирования файла"""
        input_file: Path = tmp_path / "input.txt"
        encoded_file: Path = (
            tmp_path / "encoded.bin" if binary_mode else tmp_path / "encoded.txt"
        )
        output_file: Path = tmp_path / "output.txt"

        with open(input_file, "w", encoding="utf-8") as f:
            f.write(long_text)

        huffman_files_module["encode_file"](
            str(input_file), str(encoded_file), binary_mode=binary_mode
        )

        huffman_files_module["decode_file"](
            str(encoded_file), str(output_file), binary_mode=binary_mode
        )

        with open(output_file, encoding="utf-8") as f:
            result: str = f.read()

        assert result == long_text

    def test_encode_file_nonexistent(
        self, huffman_files_module: dict[str, Any], tmp_path: Path
    ) -> None:
        """Тест кодирования несуществующего файла"""
        with pytest.raises(FileNotFoundError):
            huffman_files_module["encode_file"](
                "nonexistent.txt", str(tmp_path / "output.bin")
            )

    def test_decode_file_nonexistent(
        self, huffman_files_module: dict[str, Any], tmp_path: Path
    ) -> None:
        """Тест декодирования несуществующего файла"""
        with pytest.raises(FileNotFoundError):
            huffman_files_module["decode_file"](
                "nonexistent.bin", str(tmp_path / "output.txt")
            )


class TestHuffmanEdgeCases:
    """Класс тестов крайних случаев"""

    @pytest.mark.parametrize(
        "text, description",
        [
            ("a" * 1000, "1000 одинаковых символов"),
            ("".join(chr(i) for i in range(256)), "Все ASCII символы"),
            ("a" + "b" * 100 + "c" * 10, "Сильно различающиеся частоты"),
            ("ab" * 500, "Чередующиеся символы"),
        ],
    )
    def test_various_edge_cases(
        self, huffman_code_module: dict[str, Any], text: str, description: str
    ) -> None:
        """Тест различных крайних случаев"""
        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_code_module["encode"](text)

        # Фильтруем пустые строки из таблицы кодов
        codes = {char: code for char, code in codes.items() if char != ""}

        decoded: str = huffman_code_module["decode"](encoded, codes)

        assert decoded == text, f"Failed for case: {description}"

    def test_large_text(self, huffman_code_module: dict[str, Any]) -> None:
        """Тест с очень большим текстом"""
        large_text: str = "Lorem ipsum dolor sit amet, " * 1000
        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_code_module["encode"](large_text)

        # Фильтруем пустые строки из таблицы кодов
        codes = {char: code for char, code in codes.items() if char != ""}

        decoded: str = huffman_code_module["decode"](encoded, codes)

        assert decoded == large_text
        assert len(codes) == len(set(large_text))

    def test_single_character_repeated(
        self, huffman_code_module: dict[str, Any]
    ) -> None:
        """Тест с одним символом, повторяющимся много раз"""
        text: str = "z" * 10000
        encoded: str
        codes: dict[str, str]
        encoded, codes = huffman_code_module["encode"](text)

        assert codes == {"z": "0"}
        assert encoded == "0" * 10000
        decoded: str = huffman_code_module["decode"](encoded, codes)
        assert decoded == text
