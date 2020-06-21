import pandas as pd

csv_data = pd.read_csv(r'C:\Users\guine\Downloads\OD_2017.csv', sep=',')
csv_data2 = csv_data.loc[:,['ID_PESS','ZONA', 'CO_DOM_X', 'CO_DOM_Y',
                        'ZONA_ESC', 'CO_ESC_X',	'CO_ESC_Y',
                        'ZONATRA1', 'CO_TR1_X',	'CO_TR1_Y',
                        'ZONATRA2', 'CO_TR2_X',	'CO_TR2_Y',
                        'ZONA_O', 'CO_O_X', 'CO_O_Y',
                        'ZONA_D', 'CO_D_X', 'CO_D_Y',
                        'ZONA_T1', 'CO_T1_X', 'CO_T1_Y',
                        'ZONA_T2', 'CO_T2_X', 'CO_T2_Y',
                        'ZONA_T3', 'CO_T3_X', 'CO_T3_Y']]


cols1 = ['CO_DOM_X','CO_DOM_Y']
cols2 = ['CO_ESC_X','CO_ESC_Y']
cols3 = ['CO_TR1_X','CO_TR1_Y']
cols4 = ['CO_TR2_X','CO_TR2_Y']
cols5 = ['CO_O_X','CO_O_Y']
cols6 = ['CO_D_X','CO_D_Y']
cols7 = ['CO_T1_X','CO_T1_Y']
cols8 = ['CO_T2_X','CO_T2_Y']
cols9 = ['CO_T3_X','CO_T3_Y']

csv_data2 = csv_data2.drop_duplicates(subset='ID_PESS', keep="first")

csv_data2['CO_DOM'] = csv_data2[cols1].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
csv_data2['CO_ESC'] = csv_data2[cols2].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
csv_data2['CO_TR1'] = csv_data2[cols3].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
csv_data2['CO_TR2'] = csv_data2[cols4].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
csv_data2['CO_O'] = csv_data2[cols5].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
csv_data2['CO_D'] = csv_data2[cols6].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
csv_data2['CO_T1'] = csv_data2[cols7].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
csv_data2['CO_T2'] = csv_data2[cols8].apply(lambda row: ','.join(row.values.astype(str)), axis=1)
csv_data2['CO_T3'] = csv_data2[cols9].apply(lambda row: ','.join(row.values.astype(str)), axis=1)



csv_cont1 = csv_data2.groupby('CO_DOM').count()
csv_cont2 = csv_data2.groupby('CO_ESC').count()
csv_cont3 = csv_data2.groupby('CO_TR1').count()
csv_cont4 = csv_data2.groupby('CO_TR2').count()
csv_cont5 = csv_data2.groupby('CO_O').count()
csv_cont6 = csv_data2.groupby('CO_D').count()
csv_cont7 = csv_data2.groupby('CO_T1').count()
csv_cont8 = csv_data2.groupby('CO_T2').count()
csv_cont9 = csv_data2.groupby('CO_T3').count()

csv_total = pd.concat([csv_cont1, csv_cont2,csv_cont3,csv_cont4,csv_cont5,csv_cont6,csv_cont7,csv_cont8,csv_cont9], axis = 1, join = 'outer')
csv_total['totalid'] = csv_total['ID_PESS'] .sum(axis=1)
csv_total2 = csv_total.loc[:,['totalid']]

csv_total2.to_csv(r'C:\Users\guine\Downloads\ContCoords.csv', index = True)