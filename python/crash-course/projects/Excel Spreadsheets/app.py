import openpyxl as xl

wb = xl.load_workbook("transactions.xlsx")
sheet = wb["Sheet1"]
cell = sheet.cell(1, 1)         # It is equal to: `cell = sheet.cell(1,1)`
print(cell.value)