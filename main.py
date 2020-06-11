from utils import csv_handler

def main():
    data = csv_handler.read_csv()
    csv_handler.construct_arrays(data)


main()  
