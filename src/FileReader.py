import os
import json
import logging

logging.basicConfig(level=logging.INFO)


class FileReader:

    def __init__(self, directory="data"):
        self.files = []
        self.data_list = []
        self.directory = directory

    def find_files(self):
        """

        :return:
        """
        self.files = os.listdir(self.directory)

    def read_files(self):
        """

        :return:
        """
        if len(self.files) > 0:
            for file in self.files:
                with open(os.path.join(self.directory, file), "r") as f:
                    self.data_list[file] = json.loads(file)
        else:
            logging.info(f'Выполненные операции отсутствуют')
