import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO)


class DataProcessing:
    def __init__(self):
        self.executed_operations = []
        self.sorted_operations = []
        self.list_for_public = []

    def data_screening(self, operation_data):
        for operation in operation_data:
            if operation and operation.get('id') and operation['state'] == 'EXECUTED':
                self.executed_operations.append(operation)

    def data_sort(self):
        self.sorted_operations = sorted(self.executed_operations,
                                        key=lambda x: datetime.fromisoformat(x['date']).timestamp(),
                                        reverse=True)

    def make_output_list(self):
        if len(self.sorted_operations) > 5:
            while len(self.list_for_public) < 5:
                self.list_for_public.append(self.sorted_operations.pop(0))
        else:
            for operation in self.sorted_operations:
                self.list_for_public.append(operation)

    def print_info(self):
        for operation in self.list_for_public:
            card_from = operation.get("from", "")
            masked_number_card_from = card_from[0:5] + " " + card_from[4:6] + "*" * 2 + "" + "*" * 4 + card_from[-4:] \
                if card_from else ""
            card_to = operation.get("to", "")
            masked_card_to = "*" * 2 + card_to[-4:] if card_to else ""
            date_format = (datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f")).strftime("%d.%m.%Y")
            print(f'{date_format} {operation["description"]}\n'
                  f'{masked_number_card_from} {masked_card_to}\n'
                  f'{operation["operationAmount"]["amount"]} {operation["operationAmount"]["currency"]["name"]}\n')
