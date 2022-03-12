# csv_write用法
'''
import csv
data = [('A',1),('B',2)] or ['A','B','1']
with open('C:/Users/Luogl2000/Desktop/csv_test.csv','w',newline='') as t_file:
    csv_write = csv.writer(t_file, dialect='excel')
    for i in data:
        csv_write.writerow(i)
'''
# pandas to csv用法
'''
import pandas
maxstep = 5
dt = 6
a = [tstep for tstep in range(1, maxstep+1)]
b = [tstep * dt for tstep in range(1, maxstep+1)]
dataframe = pandas.DataFrame({'a':a,'time':b})
dataframe.to_csv('C:/Users/Luogl2000/Desktop/csv_test.csv')
'''
# pandas to excel用法
'''
import pandas
dt = 5
maxstep = 20
a = [tstep for tstep in range(1, maxstep+1)]
b = [tstep * dt for tstep in range(1, maxstep+1)]
dataframe = pandas.DataFrame({'a':a,'time':b})
writer = pandas.ExcelWriter('C:/Users/Luogl2000/Desktop/test2.xlsx')
dataframe.to_excel(writer)
writer.save()
'''
# openpyxl用法
'''
import openpyxl
data = ['T11', 'T21', 'T31', 'T41', 'T51', 'T12', 'T22', 'T32', 'T42','T52', 'T13', 'T23', 'T33', 'T43','T53', 'T14', 'T24', 'T34', 'T44', 'T54','T15', 'T25', 'T35', 'T45', 'T55']
wb = openpyxl.load_workbook('C:/Users/Luogl2000/Desktop/test2.xlsx')
ws = wb['Sheet1']
for i in range(1, len(data) + 1):
    distance = data[i - 1]
    ws.cell(row = 5, column = i + 4).value = distance
wb.save('C:/Users/Luogl2000/Desktop/test2.xlsx')
'''