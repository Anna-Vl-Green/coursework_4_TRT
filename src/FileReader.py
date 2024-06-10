import os
import json
import logging
import config

logging.basicConfig(level=config.LOG_LEVEL)


class FileReader:
    """
    Объект находит файлы и прочитывает их.
    """

    def __init__(self, directory="data"):
        self.directory = directory
        self.files = []
        self.data_list = []

    def __repr__(self):
        return (f"FileReader"
                f"("
                f"directory={self.directory!r}, "
                f"files={self.files!r}, "
                f"data_list={self.data_list!r}"
                f")")

    def __str__(self):
        return (f"FileReader"
                f"("
                f"directory={self.directory}, "
                f"files={self.files}, "
                f"data_list={self.data_list}"
                f")")

    def find_files(self):
        """
        Метод находит файлы в директории (по умолчанию - "data")
        и создаёт список с их названиями.
        """
        self.files = os.listdir(self.directory)
        if len(self.files) < 1:
            logging.info(f'Информация об операциях отсутствует')

    def read_files(self):
        """
        Метод читает файлы из списка файлов объекта
        и преобразовывает содержимое файлов
        в единый список операций.
        """
        if len(self.files) > 0:
            for file in self.files:
                with open(os.path.join(self.directory, file), "r", encoding='UTF-8') as f:
                    self.data_list.extend(json.loads(f.read()))
        else:
            logging.info(f'Выполненные операции отсутствуют')
