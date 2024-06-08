import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)


class DataProcessing:
    """
    TODO
    """
    def __init__(self):
        self.executed_operations = []
        self.sorted_operations = []
        self.list_for_public = []
        self.messages_list = []

    def __repr__(self):
        return "Объект обрабатывает данные из файлов"

    def data_screening(self, operation_data):
        """
        Метод фильтрует данные из списка операций
        и копирует данные об успешных транзакциях
        в список executed_operations.
        :param operation_data: list
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
        Метод создаёт список из 5 последних успешных транзакций клиента.
        """
        if len(self.sorted_operations) > 5:
            while len(self.list_for_public) < 5:
                self.list_for_public.append(self.sorted_operations.pop(0))
        else:
            for operation in self.sorted_operations:
                self.list_for_public.append(operation)

    def masking_info(self):
        """
        Метод маскирует данные о платёжных реквизитах клиента
        и список сообщений с данными об операциях.
        :param message_list: list[str]
        """
        space = " "
        for operation in self.list_for_public:
            card_from = operation.get("from", "")
            split_card_from = card_from.split(" ")
            number_from = split_card_from[-1]
            if len(number_from) == 16:
                masked_number_from = number_from[0:6] + "*" * len(number_from[6:12]) + number_from[12:]
                operation['from'] = (space.join(split_card_from[:-1]) + space + masked_number_from[:4] + space
                                     + masked_number_from[4:8] + space + masked_number_from[8:12] + space
                                     + masked_number_from[12:])
            elif len(number_from) == 20:
                masked_number_from = number_from[0:7] + "*" * len(number_from[7:17]) + number_from[17:]
                operation['from'] = (space.join(split_card_from[:-1]) + space + masked_number_from[:5] + space
                                     + masked_number_from[5:9] + space + masked_number_from[9:13] + space +
                                     masked_number_from[13:17] + space + masked_number_from[17:])
            else:
                logging.info(f'Некорректный номер источника платежа')
                operation['from'] = ''
            card_to = operation.get("to", "")
            split_card_to = card_to.split(" ")
            number_to = split_card_to[-1]
            operation['to'] = space.join(split_card_to[:-1]) + " **" + number_to[-4:]

    def create_messages(self):
        for operation in self.list_for_public:
            pass
