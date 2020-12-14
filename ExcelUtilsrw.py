import xlrd

class ExcelUtils:

    @classmethod
    def read(cls,filename="",sheetname="0"):
        try:
            list=[]
            file=xlrd.open_workbook(filename)
            if sheetname.isdigit():
                sheet=file.sheet_by_index(int(sheetname))
                rows=sheet.nrows
                for i in range(rows):
                    list.append(sheet.row_values(i))
                return list
            else:
                sheet=file.sheet_by_name(sheetname)
                rows=sheet.nrows
                for i in range(rows):
                    list.append(sheet.row_values(i))
                return list
        except Exception as error:
            print(error)
s=ExcelUtils.read("C:\\Users\\123\\PycharmProjects\\day16\\testcaserw\\bankuser.xlsx", "0")
# print(s)
