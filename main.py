from src.FileReader import FileReader
from src.DataProcessing import DataProcessing


if __name__ == '__main__':
    files_data = FileReader()
    files_data.find_files()
    files_data.read_files()

    operations_data = DataProcessing()
    operations_data.data_screening(files_data.data_list)
    operations_data.data_sort()
    operations_data.make_output_list()
    operations_data.print_info()
