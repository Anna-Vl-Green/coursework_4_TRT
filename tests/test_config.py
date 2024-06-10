file_reader_str = ("FileReader(directory=test_data, files=['test_operations.json'], "
                   "data_list=["
                   "{'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051', "
                   "'operationAmount': "
                   "{'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, "
                   "'description': 'Перевод со счета на счет', "
                   "'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'}, "
                   "{'id': 414894334, 'state': 'EXECUTED', 'date': '2019-06-30T15:11:53.136004', "
                   "'operationAmount': "
                   "{'amount': '95860.47', 'currency': {'name': 'руб.', 'code': 'RUB'}}, "
                   "'description': 'Перевод со счета на счет', "
                   "'from': 'Счет 59956820797131895975', 'to': 'Счет 43475624104328495820'}, "
                   "{}, "
                   "{'id': 509552992, 'state': 'EXECUTED', 'date': '2019-04-19T12:02:30.129240', "
                   "'operationAmount': "
                   "{'amount': '81513.74', 'currency': {'name': 'руб.', 'code': 'RUB'}}, "
                   "'description': 'Перевод с карты на карту', "
                   "'from': 'Maestro 9171987821259925', 'to': 'МИР 2052809263194182'}, "
                   "{'id': 596914981, 'state': 'EXECUTED', 'date': '2018-04-16T17:34:19.241289', "
                   "'operationAmount': "
                   "{'amount': '65169.27', 'currency': {'name': 'USD', 'code': 'USD'}}, "
                   "'description': 'Перевод организации', "
                   "'from': 'Visa Platinum 1813166339376336', 'to': 'Счет 97848259954268659635'}, "
                   "{'id': 200634844, 'state': 'CANCELED', 'date': '2018-02-13T04:43:11.374324', "
                   "'operationAmount': "
                   "{'amount': '42210.20', 'currency': {'name': 'руб.', 'code': 'RUB'}}, "
                   "'description': 'Перевод организации', "
                   "'from': 'Счет 33355011456314142963', 'to': 'Счет 45735917297559088682'}"
                   "])")

file_reader_repr = ("FileReader(directory='test_data', files=['test_operations.json'], "
                    "data_list=["
                    "{'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051', "
                    "'operationAmount': "
                    "{'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, "
                    "'description': 'Перевод со счета на счет', "
                    "'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'}, "
                    "{'id': 414894334, 'state': 'EXECUTED', 'date': '2019-06-30T15:11:53.136004', "
                    "'operationAmount': "
                    "{'amount': '95860.47', 'currency': {'name': 'руб.', 'code': 'RUB'}}, "
                    "'description': 'Перевод со счета на счет', "
                    "'from': 'Счет 59956820797131895975', 'to': 'Счет 43475624104328495820'}, "
                    "{}, "
                    "{'id': 509552992, 'state': 'EXECUTED', 'date': '2019-04-19T12:02:30.129240', "
                    "'operationAmount': "
                    "{'amount': '81513.74', 'currency': {'name': 'руб.', 'code': 'RUB'}}, "
                    "'description': 'Перевод с карты на карту', "
                    "'from': 'Maestro 9171987821259925', 'to': 'МИР 2052809263194182'}, "
                    "{'id': 596914981, 'state': 'EXECUTED', 'date': '2018-04-16T17:34:19.241289', "
                    "'operationAmount': {'amount': '65169.27', 'currency': {'name': 'USD', 'code': 'USD'}}, "
                    "'description': 'Перевод организации', "
                    "'from': 'Visa Platinum 1813166339376336', 'to': 'Счет 97848259954268659635'}, "
                    "{'id': 200634844, 'state': 'CANCELED', 'date': '2018-02-13T04:43:11.374324', "
                    "'operationAmount': "
                    "{'amount': '42210.20', 'currency': {'name': 'руб.', 'code': 'RUB'}}, "
                    "'description': 'Перевод организации', "
                    "'from': 'Счет 33355011456314142963', 'to': 'Счет 45735917297559088682'}])")

read_files_expected = [
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
    {},
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
    {
        "id": 200634844,
        "state": "CANCELED",
        "date": "2018-02-13T04:43:11.374324",
        "operationAmount": {
            "amount": "42210.20",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 33355011456314142963",
        "to": "Счет 45735917297559088682"
    }
]

test_data = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
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
    {},
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
    {
        "id": 200634844,
        "state": "CANCELED",
        "date": "2018-02-13T04:43:11.374324",
        "operationAmount": {
            "amount": "42210.20",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 33355011456314142963",
        "to": "Счет 45735917297559088682"
    },
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
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    }
]

correct_data = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
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
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
    }
]

correct_data_sort = [
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
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
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
    }
]

correct_output_list = [
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
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {
            "amount": "31957.58",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589"
    },
    {
        "id": 667307132,
        "state": "EXECUTED",
        "date": "2019-07-13T18:51:29.313309",
        "operationAmount": {
            "amount": "97853.86",
            "currency": {
                "name": "руб.",
                "code": "RUB"
            }
        },
        "description": "Перевод с карты на счет",
        "from": "Maestro 1308795367077170",
        "to": "Счет 96527012349577388612"
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
    }
]

correct_mask_list = [{'date': '2019-11-13T17:38:04.800051',
                      'description': 'Перевод со счета на счет',
                      'from': 'Счет **9794',
                      'id': 482520625,
                      'operationAmount': {'amount': '62814.53',
                                          'currency': {'code': 'RUB', 'name': 'руб.'}},
                      'state': 'EXECUTED',
                      'to': 'Счет **8125'},
                     {'date': '2019-08-26T10:50:58.294041',
                      'description': 'Перевод организации',
                      'from': 'Maestro 1596 83** **** 5199',
                      'id': 441945886,
                      'operationAmount': {'amount': '31957.58',
                                          'currency': {'code': 'RUB', 'name': 'руб.'}},
                      'state': 'EXECUTED',
                      'to': 'Счет **9589'},
                     {'date': '2019-07-13T18:51:29.313309',
                      'description': 'Перевод с карты на счет',
                      'from': 'Maestro 1308 79** **** 7170',
                      'id': 667307132,
                      'operationAmount': {'amount': '97853.86',
                                          'currency': {'code': 'RUB', 'name': 'руб.'}},
                      'state': 'EXECUTED',
                      'to': 'Счет **8612'},
                     {'date': '2019-06-30T15:11:53.136004',
                      'description': 'Перевод со счета на счет',
                      'from': 'Счет **5975',
                      'id': 414894334,
                      'operationAmount': {'amount': '95860.47',
                                          'currency': {'code': 'RUB', 'name': 'руб.'}},
                      'state': 'EXECUTED',
                      'to': 'Счет **5820'},
                     {'date': '2019-04-19T12:02:30.129240',
                      'description': 'Перевод с карты на карту',
                      'from': 'Maestro 9171 98** **** 9925',
                      'id': 509552992,
                      'operationAmount': {'amount': '81513.74',
                                          'currency': {'code': 'RUB', 'name': 'руб.'}},
                      'state': 'EXECUTED',
                      'to': 'МИР **4182'}]

correct_messages_list = ['13.11.2019 Перевод со счета на счет\n'
                         'Счет **9794 -> Счет **8125\n'
                         '62814.53 руб.\n',
                         '26.08.2019 Перевод организации\n'
                         'Maestro 1596 83** **** 5199 -> Счет **9589\n'
                         '31957.58 руб.\n',
                         '13.07.2019 Перевод с карты на счет\n'
                         'Maestro 1308 79** **** 7170 -> Счет **8612\n'
                         '97853.86 руб.\n',
                         '30.06.2019 Перевод со счета на счет\n'
                         'Счет **5975 -> Счет **5820\n'
                         '95860.47 руб.\n',
                         '19.04.2019 Перевод с карты на карту\n'
                         'Maestro 9171 98** **** 9925 -> МИР **4182\n'
                         '81513.74 руб.\n']

data_process_str = ("DataProcessing(executed_operations=[{'id': 441945886, 'state': 'EXECUTED', "
                    "'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': "
                    "'31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': "
                    "'Перевод организации', 'from': 'Maestro 1596 83** **** 5199', 'to': 'Счет "
                    "**9589'}, {'id': 414894334, 'state': 'EXECUTED', 'date': "
                    "'2019-06-30T15:11:53.136004', 'operationAmount': {'amount': '95860.47', "
                    "'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со "
                    "счета на счет', 'from': 'Счет **5975', 'to': 'Счет **5820'}, {'id': "
                    "509552992, 'state': 'EXECUTED', 'date': '2019-04-19T12:02:30.129240', "
                    "'operationAmount': {'amount': '81513.74', 'currency': {'name': 'руб.', "
                    "'code': 'RUB'}}, 'description': 'Перевод с карты на карту', 'from': 'Maestro "
                    "9171 98** **** 9925', 'to': 'МИР **4182'}, {'id': 596914981, 'state': "
                    "'EXECUTED', 'date': '2018-04-16T17:34:19.241289', 'operationAmount': "
                    "{'amount': '65169.27', 'currency': {'name': 'USD', 'code': 'USD'}}, "
                    "'description': 'Перевод организации', 'from': 'Visa Platinum "
                    "1813166339376336', 'to': 'Счет 97848259954268659635'}, {'id': 482520625, "
                    "'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051', "
                    "'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', "
                    "'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет "
                    "**9794', 'to': 'Счет **8125'}, {'id': 667307132, 'state': 'EXECUTED', "
                    "'date': '2019-07-13T18:51:29.313309', 'operationAmount': {'amount': "
                    "'97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': "
                    "'Перевод с карты на счет', 'from': 'Maestro 1308 79** **** 7170', 'to': "
                    "'Счет **8612'}], sorted_operations=[{'id': 596914981, 'state': 'EXECUTED', "
                    "'date': '2018-04-16T17:34:19.241289', 'operationAmount': {'amount': "
                    "'65169.27', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': "
                    "'Перевод организации', 'from': 'Visa Platinum 1813166339376336', 'to': 'Счет "
                    "97848259954268659635'}]list_for_public=[{'id': 482520625, 'state': "
                    "'EXECUTED', 'date': '2019-11-13T17:38:04.800051', 'operationAmount': "
                    "{'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, "
                    "'description': 'Перевод со счета на счет', 'from': 'Счет **9794', 'to': "
                    "'Счет **8125'}, {'id': 441945886, 'state': 'EXECUTED', 'date': "
                    "'2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', "
                    "'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод "
                    "организации', 'from': 'Maestro 1596 83** **** 5199', 'to': 'Счет **9589'}, "
                    "{'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309', "
                    "'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', "
                    "'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Maestro "
                    "1308 79** **** 7170', 'to': 'Счет **8612'}, {'id': 414894334, 'state': "
                    "'EXECUTED', 'date': '2019-06-30T15:11:53.136004', 'operationAmount': "
                    "{'amount': '95860.47', 'currency': {'name': 'руб.', 'code': 'RUB'}}, "
                    "'description': 'Перевод со счета на счет', 'from': 'Счет **5975', 'to': "
                    "'Счет **5820'}, {'id': 509552992, 'state': 'EXECUTED', 'date': "
                    "'2019-04-19T12:02:30.129240', 'operationAmount': {'amount': '81513.74', "
                    "'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с "
                    "карты на карту', 'from': 'Maestro 9171 98** **** 9925', 'to': 'МИР "
                    "**4182'}]messages_list=['13.11.2019 Перевод со счета на счет\\nСчет **9794 "
                    "-> Счет **8125\\n62814.53 руб.\\n', '26.08.2019 Перевод "
                    'организации\\nMaestro 1596 83** **** 5199 -> Счет **9589\\n31957.58 '
                    "руб.\\n', '13.07.2019 Перевод с карты на счет\\nMaestro 1308 79** **** 7170 "
                    "-> Счет **8612\\n97853.86 руб.\\n', '30.06.2019 Перевод со счета на "
                    "счет\\nСчет **5975 -> Счет **5820\\n95860.47 руб.\\n', '19.04.2019 Перевод с "
                    'карты на карту\\nMaestro 9171 98** **** 9925 -> МИР **4182\\n81513.74 '
                    "руб.\\n'])")

data_process_repr = ("DataProcessing(executed_operations=[{'id': 441945886, 'state': 'EXECUTED', "
                     "'date': '2019-08-26T10:50:58.294041', 'operationAmount': {'amount': "
                     "'31957.58', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': "
                     "'Перевод организации', 'from': 'Maestro 1596 83** **** 5199', 'to': 'Счет "
                     "**9589'}, {'id': 414894334, 'state': 'EXECUTED', 'date': "
                     "'2019-06-30T15:11:53.136004', 'operationAmount': {'amount': '95860.47', "
                     "'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со "
                     "счета на счет', 'from': 'Счет **5975', 'to': 'Счет **5820'}, {'id': "
                     "509552992, 'state': 'EXECUTED', 'date': '2019-04-19T12:02:30.129240', "
                     "'operationAmount': {'amount': '81513.74', 'currency': {'name': 'руб.', "
                     "'code': 'RUB'}}, 'description': 'Перевод с карты на карту', 'from': 'Maestro "
                     "9171 98** **** 9925', 'to': 'МИР **4182'}, {'id': 596914981, 'state': "
                     "'EXECUTED', 'date': '2018-04-16T17:34:19.241289', 'operationAmount': "
                     "{'amount': '65169.27', 'currency': {'name': 'USD', 'code': 'USD'}}, "
                     "'description': 'Перевод организации', 'from': 'Visa Platinum "
                     "1813166339376336', 'to': 'Счет 97848259954268659635'}, {'id': 482520625, "
                     "'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051', "
                     "'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', "
                     "'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет "
                     "**9794', 'to': 'Счет **8125'}, {'id': 667307132, 'state': 'EXECUTED', "
                     "'date': '2019-07-13T18:51:29.313309', 'operationAmount': {'amount': "
                     "'97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': "
                     "'Перевод с карты на счет', 'from': 'Maestro 1308 79** **** 7170', 'to': "
                     "'Счет **8612'}], sorted_operations=[{'id': 596914981, 'state': 'EXECUTED', "
                     "'date': '2018-04-16T17:34:19.241289', 'operationAmount': {'amount': "
                     "'65169.27', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': "
                     "'Перевод организации', 'from': 'Visa Platinum 1813166339376336', 'to': 'Счет "
                     "97848259954268659635'}]list_for_public=[{'id': 482520625, 'state': "
                     "'EXECUTED', 'date': '2019-11-13T17:38:04.800051', 'operationAmount': "
                     "{'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, "
                     "'description': 'Перевод со счета на счет', 'from': 'Счет **9794', 'to': "
                     "'Счет **8125'}, {'id': 441945886, 'state': 'EXECUTED', 'date': "
                     "'2019-08-26T10:50:58.294041', 'operationAmount': {'amount': '31957.58', "
                     "'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод "
                     "организации', 'from': 'Maestro 1596 83** **** 5199', 'to': 'Счет **9589'}, "
                     "{'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309', "
                     "'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', "
                     "'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Maestro "
                     "1308 79** **** 7170', 'to': 'Счет **8612'}, {'id': 414894334, 'state': "
                     "'EXECUTED', 'date': '2019-06-30T15:11:53.136004', 'operationAmount': "
                     "{'amount': '95860.47', 'currency': {'name': 'руб.', 'code': 'RUB'}}, "
                     "'description': 'Перевод со счета на счет', 'from': 'Счет **5975', 'to': "
                     "'Счет **5820'}, {'id': 509552992, 'state': 'EXECUTED', 'date': "
                     "'2019-04-19T12:02:30.129240', 'operationAmount': {'amount': '81513.74', "
                     "'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с "
                     "карты на карту', 'from': 'Maestro 9171 98** **** 9925', 'to': 'МИР "
                     "**4182'}]messages_list=['13.11.2019 Перевод со счета на счет\\nСчет **9794 "
                     "-> Счет **8125\\n62814.53 руб.\\n', '26.08.2019 Перевод "
                     'организации\\nMaestro 1596 83** **** 5199 -> Счет **9589\\n31957.58 '
                     "руб.\\n', '13.07.2019 Перевод с карты на счет\\nMaestro 1308 79** **** 7170 "
                     "-> Счет **8612\\n97853.86 руб.\\n', '30.06.2019 Перевод со счета на "
                     "счет\\nСчет **5975 -> Счет **5820\\n95860.47 руб.\\n', '19.04.2019 Перевод с "
                     'карты на карту\\nMaestro 9171 98** **** 9925 -> МИР **4182\\n81513.74 '
                     "руб.\\n'])")
