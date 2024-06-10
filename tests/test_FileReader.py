import pytest
from tests.test_config import file_reader_str, read_files_expected, file_reader_repr
from src.FileReader import FileReader


@pytest.fixture(scope="module")
def file_reader():
    """
    Инициализирует объект класса FileReader для тестирования функционала модуля.
    :return: FileReader
    """
    return FileReader("test_data")


def test_find_files(file_reader):
    """
    Тестирует функционал метода поиска файлов в указанной директории (find_files).
    :param file_reader:FileReader
    """
    file_reader.find_files()
    assert len(file_reader.files) > 0, "Файлы не найдены"


def test_read_files(file_reader):
    """
    Тестирует функционал метода чтения файлов из списка объекта класса FileReader.
    :param file_reader: FileReader
    """
    file_reader.find_files()
    file_reader.read_files()
    expected = read_files_expected
    assert file_reader.data_list == expected


def test_file_reader__str__(file_reader):
    """
    Тестирует функционал метода распечатки экземпляра класса FileReader.
    :param file_reader: FileReader
    """
    file_reader.find_files()
    file_reader.read_files()
    assert str(file_reader) == file_reader_str


def test_file_reader__repr__(file_reader):
    """
    Тестирует функционал метода формального строкового представления экземпляра класса FileReader.
    :param file_reader: FileReader
    """
    file_reader.find_files()
    file_reader.read_files()
    assert file_reader.__repr__() == file_reader_repr
