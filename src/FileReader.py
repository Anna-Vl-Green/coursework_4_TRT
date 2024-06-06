import os
import json
import logging
import config

logging.basicConfig(level=config.LOG_LEVEL)


class FileReader:

    def __init__(self, directory="data"):
        self.files = []
        self.data_list = []
        self.directory = directory

    def find_files(self):
        """
        Метод находит файлы в папке (по умолчанию - "data" и создаёт список с их названиями.
        """
        self.files = os.listdir(self.directory)

    def read_files(self):
        """
        Метод читает файлы из списка объекта.
        """
        if len(self.files) > 0:
            for file in self.files:
                with open(os.path.join(self.directory, file), "r", encoding='UTF-8') as f:
                    self.data_list.extend(json.loads(f.read()))
        else:
            logging.info(f'Выполненные операции отсутствуют')
