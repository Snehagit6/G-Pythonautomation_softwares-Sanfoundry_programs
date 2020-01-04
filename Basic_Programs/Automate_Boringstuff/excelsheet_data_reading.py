from Basic_Programs.Automate_Boringstuff.excel_sheet_openpyxl import Spec

spec=Spec("G://Pythonexceldata.xlsx")
@spec.data
def read_data(param,**kwargs):
    print(param['ID'])
read_data(6)

