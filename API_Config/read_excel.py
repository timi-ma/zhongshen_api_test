import pandas

excel = "./data/API_Zhongshen_TestCases.xlsx"


def read_excel_to_dict(sheet_name):
    try:
        case_datas = pandas.read_excel(excel, sheet_name=sheet_name).to_dict("records")
        print("读取文件成功")
        return case_datas
    except Exception as e:
        print(f"读取文件失败：{e}")
        return []
