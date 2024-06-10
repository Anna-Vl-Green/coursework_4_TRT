from src.FileReader import FileReader
from src.DataProcessing import DataProcessing


def print_messages(messages_list: list):
    """
    Функция выводит на печать сообщения из списка сообщений.
    :param messages_list: list[str]
    """
    for message in messages_list:
        print(message)


if __name__ == '__main__':
    files_data = FileReader()
    files_data.find_files()
    files_data.read_files()

    operations_data = DataProcessing()
    operations_data.data_screening(files_data.data_list)
    operations_data.data_sort()
    operations_data.make_output_list()
    operations_data.masking_info()
    operations_data.create_messages()
    print_messages(operations_data.messages_list)
