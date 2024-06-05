from src.FileReader import FileReader
from src.DataProcessing import DataProcessing

import src.FileReader
import src.DataProcessing

clients_operations = FileReader.find_files() # получаем список операций клиента

DataProcessing.data_screening(FileReader.read_files())

DataProcessing.print_info()