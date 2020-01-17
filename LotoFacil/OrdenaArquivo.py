import win32com.client

excel = win32com.client.Dispatch("Excel.Application")

wb = excel.Workbooks.Open('loto.xlsx')
ws = wb.Worksheets('Sheet1')

ws.Range('A8:A1888').Sort(Key1=ws.Range('A1'), Order1=1, Orientation=1)

wb.Save()
excel.Application.Quit()