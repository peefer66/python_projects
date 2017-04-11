# THIS SCRIPT EXTRACTS THE VALUES FORM THE SYNTHOMER COMPOUND XLS Files
# CREATES A CSV FILE USING PANDAS

import os
import xlrd
import csv
import pandas as pd

def create_row_list(worksheet, row):
    # This function takes the row and column and appends the value to row list
    row_list = []
    # APPEND THE VALUES FOR COMPOUND NUMBER, CUSTOMER & USE AND COVER TO UPPERCASE
    # BEFORE append
    row_list.append(worksheet.cell_value(row, 8).upper())
    row_list.append(worksheet.cell_value(row, 1).upper())
    # strip the 'USE :' from the start and then lstrip to remove any remaining leading blanks
    row_list.append(worksheet.cell_value(row,3)[6:len( worksheet.cell_value(row,3).upper())].lstrip(' '))
    row_list.append(worksheet.cell_value(row + 3, 1))
    return row_list

if __name__ == ('__main__'):
    # Itterate through the directory and sub dirs and print ot the file name
    spath = 'H:/Project_Munich_Technology/New_name_ MIs/'
    sheet_list = []
    for  root, dirs, files in os.walk(spath):
        for file in files:
            pathname = os.path.join(root, file)
            # CONVER \ TO / IN THE PATH
            pathname = '/'.join(pathname.split('\\'))
            #print(pathname)
            workbook = xlrd.open_workbook(pathname)
            worksheet = workbook.sheet_by_index(0)
            for col in range(40,55):
                if worksheet.cell_value(col,6) == 'COMPOUND : ':
                    my_list = create_row_list(worksheet, col)
            sheet_list.append(my_list)

    # for item in sheet_list:
    #     print(item)

    # uSE PANDAS TO CREAT A DATAFRAME FROM  THE SHEET_LIST AND CONVERE TO A CSV FILE.
    my_df = pd.DataFrame(sheet_list)
    my_df.to_csv('output.csv', index=False, header=False)
