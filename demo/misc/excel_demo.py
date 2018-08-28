import xlrd

workbook=xlrd.open_workbook('test.xlsx')
sheet=workbook.sheets()[0]
#sheet=workbook.sheet_by_index(0)
#sheet=workbook.sheet_by_name('sheet_name')
#获取行、列的数组值
sheet.row_value(i)
sheet.clo_value(i)
#
row_num=sheet.nrows
col_num=sheet.ncols

cell_A1=sheet.cell(0,0).value
cell_A1=sheet.row(0)[0].value

