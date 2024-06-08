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

    def create_messages(self):
        """
        Метод маскирует данные о платёжных реквизитах клиента
        и список сообщений с данными об операциях.
        :param message_list: list[str]
        """
        space = " "
        for operation in self.list_for_public:



            card_from = operation.get("from", "")
            masked_number_card_from = card_from[0:5] + " " + card_from[4:6] + "*" * 2 + "" + "*" * 4 + card_from[-4:] \
                if card_from else ""
            card_to = operation.get("to", "")
            masked_card_to = "*" * 2 + card_to[-4:] if card_to else ""
            date_format = (datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f")).strftime("%d.%m.%Y")
            self.messages_list.append(f'{date_format} {operation["description"]}\n'
                                      f'{masked_number_card_from} {masked_card_to}\n'
                                      f'{operation["operationAmount"]["amount"]} '
                                      f'{operation["operationAmount"]["currency"]["name"]}\n')
