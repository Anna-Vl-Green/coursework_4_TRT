import pytest
from src.FileReader import FileReader


@pytest.fixture(scope="module")
def file_reader():
    return FileReader("test_data")


def test_find_files(file_reader):
    file_reader.find_files()
    assert len(file_reader.files) > 0, "Файлы найдены"


def test_read_files(file_reader):
    result = file_reader.read_files()
    expected = [
        {
            "id": 482520625,
            "state": "EXECUTED",
            "date": "2019-11-13T17:38:04.800051",
            "operationAmount": {
                "amount": "62814.53",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 38611439522855669794",
            "to": "Счет 46765464282437878125"
        },
        {
            "id": 414894334,
            "state": "EXECUTED",
            "date": "2019-06-30T15:11:53.136004",
            "operationAmount": {
                "amount": "95860.47",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 59956820797131895975",
            "to": "Счет 43475624104328495820"
        },
        {
            "id": 509552992,
            "state": "EXECUTED",
            "date": "2019-04-19T12:02:30.129240",
            "operationAmount": {
                "amount": "81513.74",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Maestro 9171987821259925",
            "to": "МИР 2052809263194182"
        },
        {
            "id": 596914981,
            "state": "EXECUTED",
            "date": "2018-04-16T17:34:19.241289",
            "operationAmount": {
                "amount": "65169.27",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1813166339376336",
            "to": "Счет 97848259954268659635"
        },
    ]
    assert result == expected, f"Ожидалось {expected}, получено {result}"
