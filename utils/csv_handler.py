import pandas as pd
import re

class Person:
  def __init__(self, coords, id_pess):
    self.coords = coords
    self.id_pess = id_pess

#   def myfunc(self):
#     print("Hello my name is " + self.name)

def read_csv():
    
    # with open("OD_2017.csv") as file:
    #     # data = [",".split(line) for line in file]

    # print (data[1:10])

    # data = pd.read_csv('OD_2017_1.csv')
    # data.head()

    cols_list = ["ZONA", "CO_DOM_X", "CO_DOM_Y", "ID_PESS", ]
    print(cols_list)
    csv_data = pd.read_csv("C:/Users/Igor/Documents/GitHub/ep1-aed2/utils/OD_2017.csv", sep=',', usecols=cols_list)
    print(csv_data['ZONA'])
    return csv_data


def construct_arrays(columns):
    #Ler CSV
    #open

    #Pega coluna ID_PESS e passa pro array ids[]
    # ids = []

    # Pego colunas com a palavra CO_*_X e pegar a coluna seguinte para montar o array,  e passo pro array de arrays coords[[]] 
    # usando Regex
    coords = [[]]

    ids = columns.ID_PESS.tolist()

    ids = ids.drop_duplicates(keep=First)

    for item in columns:
        
    #     #Ve se a coluna é alguma da constante
        coord_regex = re.search('^CO_*_X$', )
        if column == (coord_regex):
            coords[[item]].append()

    ids = remove_duplicates(ids, 'array')
    coord = remove_duplicates(coords, 'array of arrays')


def remove_duplicates(array, type):
    if type == 'array':
        no_dupes = []
    else:
        no_dupes = [[]]

    for item in array:
        if item not in array:
            no_dupes.append(item)
    no_dupes.sort()

    return no_dupes

def check_connections(csv, ids, coords):

    pass 