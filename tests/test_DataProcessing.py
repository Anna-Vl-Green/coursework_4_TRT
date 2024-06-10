import pytest
from tests.test_config import (
                               test_data,
                               correct_data,
                               correct_data_sort,
                               correct_output_list,
                               correct_mask_list,
                               correct_messages_list,
                               data_process_str,
                               data_process_repr
                               )
from src.DataProcessing import DataProcessing


@pytest.fixture(scope="module")
def data_process():
    """
    Инициализирует объект класса DataProcessing для тестирования функционала модуля.
    :return:
    """
    return DataProcessing()


def test_data_screening_empty(data_process):
    """
    Тестирует функционал вывода системного сообщения об отсутствии успешных операций.
    """
    data_process.data_screening([])
    assert data_process.executed_operations == []


def test_data_sort_empty(data_process):
    """
    Тестирует функционал вывода системного сообщения об отсутствии данных для сортировки.
    """
    data_process.data_screening([])
    data_process.data_sort()
    assert data_process.sorted_operations == []


def test_data_screening(data_process):
    """
    Тестирует функционал метода фильтрации данных об операциях (data_screening).
    :param file_reader.data_list: list[dict]
    """
    data_process.data_screening(test_data)
    assert data_process.executed_operations == correct_data


def test_data_sort(data_process):
    """
    Тестирует функционал метода сортировки данных об операциях (data_sort).
    """
    data_process.data_screening(test_data)
    data_process.data_sort()
    assert data_process.sorted_operations == correct_data_sort


def test_make_output_list(data_process):
    """
    Тестирует функционал метода создания списка из 5
    последних успешных операций клиента (make_output_list).
    """
    data_process.data_screening(test_data)
    data_process.data_sort()
    data_process.make_output_list()
    assert data_process.list_for_public == correct_output_list


def test_masking_info(data_process):
    """
    Тестирует функционал метода маскирования данных об операциях (masking_info).
    """
    data_process.data_screening(test_data)
    data_process.data_sort()
    data_process.make_output_list()
    data_process.masking_info()
    assert data_process.list_for_public == correct_mask_list


def test_create_message(data_process):
    """
    Тестирует функционал метода создания списка сообщений с данными об операциях (create_messages).
    """
    data_process.data_screening(test_data)
    data_process.data_sort()
    data_process.make_output_list()
    data_process.masking_info()
    data_process.create_messages()
    assert data_process.messages_list == correct_messages_list


def test_data_processing__str__(data_process):
    """
    Тестирует функционал метода распечатки экземпляра класса DataProcessing.
    :param data_process: DataProcessing
    """
    data_process.data_screening(test_data)
    data_process.data_sort()
    data_process.make_output_list()
    data_process.masking_info()
    data_process.create_messages()
    assert str(data_process) == data_process_str


def test_data_processing__repr__(data_process):
    """
    Тестирует функционал метода формального строкового представления экземпляра класса DataProcessing.
    :param data_process: DataProcessing
    """
    data_process.data_screening(test_data)
    data_process.data_sort()
    data_process.make_output_list()
    data_process.masking_info()
    data_process.create_messages()
    assert data_process.__repr__() == data_process_repr
