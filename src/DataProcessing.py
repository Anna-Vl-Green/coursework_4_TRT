import logging
from config import DATA_COUNT
from datetime import datetime

logging.basicConfig(level=logging.INFO)


class DataProcessing:
    """
    Класс обрабатывает данные из файлов.
    """
    def __init__(self):
        self.executed_operations = []
        self.sorted_operations = []
        self.list_for_public = []
        self.messages_list = []

    def __repr__(self):
        return (f"DataProcessing"
                f"("
                f"executed_operations={self.executed_operations!r}, "
                f"sorted_operations={self.sorted_operations!r}"
                f"list_for_public={self.list_for_public!r}"
                f"messages_list={self.messages_list!r}"
                f")")

    def __str__(self):
        return (f"DataProcessing"
                f"("
                f"executed_operations={self.executed_operations}, "
                f"sorted_operations={self.sorted_operations}"
                f"list_for_public={self.list_for_public}"
                f"messages_list={self.messages_list}"
                f")")

    def data_screening(self, operation_data):
        """
        Метод фильтрует данные из списка операций
        и копирует данные об успешных транзакциях
        в список executed_operations.
        :param operation_data: list[dict]
        """
        for operation in operation_data:
            if operation and operation.get('id') and operation['state'] == 'EXECUTED':
                self.executed_operations.append(operation)
        if len(self.executed_operations) < 1:
            logging.info(f'Информация об успешных операциях отсутствует')

    def data_sort(self):
        """
        Метод сортирует успешные операции из списка executed_operations
        по дате и времени платежа в порядке убывания.
        """
        self.sorted_operations = sorted(self.executed_operations,
                                        key=lambda x: datetime.fromisoformat(x['date']).timestamp(),
                                        reverse=True)
        if len(self.sorted_operations) < 1:
            logging.info(f'Нет данных для сортировки')

    def make_output_list(self):
        """
        Метод создаёт список из последних успешных транзакций клиента согласно требованиям,
        указанным в config.py.
        """
        if len(self.sorted_operations) > DATA_COUNT:
            while len(self.list_for_public) < DATA_COUNT:
                self.list_for_public.append(self.sorted_operations.pop(0))
        else:
            for operation in self.sorted_operations:
                self.list_for_public.append(operation)

    def masking_info(self):
        """
        Метод маскирует данные о платёжных реквизитах клиента.
        """
        space = " "
        for operation in self.list_for_public:
            card_from = operation.get("from", "")
            split_card_from = card_from.split(" ")
            number_from = split_card_from[-1]
            if len(number_from) == 16:
                masked_number_from = number_from[0:6] + "*" * len(number_from[6:-4]) + number_from[-4:]
                operation['from'] = (space.join(split_card_from[:-1]) + space + masked_number_from[:4] + space
                                     + masked_number_from[4:8] + space + masked_number_from[8:12] + space
                                     + masked_number_from[-4:])
            elif len(number_from) == 20:
                operation['from'] = (space.join(split_card_from[:-1]) + " **" + number_from[-4:])
            else:
                operation['from'] = ''
            card_to = operation.get("to", "")
            split_card_to = card_to.split(" ")
            number_to = split_card_to[-1]
            operation['to'] = space.join(split_card_to[:-1]) + " **" + number_to[-4:]

    def create_messages(self):
        """
        Метод создаёт список сообщений с данными об операциях.
        """
        for operation in self.list_for_public:
            date_format = (datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f")).strftime("%d.%m.%Y")
            self.messages_list.append(f'{date_format} {operation["description"]}\n'
                                      f'{operation["from"] + ' ' if operation["from"] else ''}-> {operation["to"]}\n'
                                      f'{operation["operationAmount"]["amount"]} '
                                      f'{operation["operationAmount"]["currency"]["name"]}\n')
