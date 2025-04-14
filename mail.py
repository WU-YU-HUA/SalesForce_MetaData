# from simple_salesforce import Salesforce
from simple_salesforce import Salesforce
import pandas as pd
# dev
sf = Salesforce(username="",
                password="", 
                security_token="", 
                domain="")
# 要查詢的 Salesforce Object 名稱
object_list = ['RFQ_form__c', 'RFQ_Form_Line_Item__c', 'MFG_Cost__c', 'Cost_BOM_RM_Item__c', 'Tooling_Cost__c', 'Vendor_Source__c']

for object_name in object_list:
    # 取得 describe 結果（欄位 metadata）
    describe = sf.__getattr__(object_name).describe()

    # 提取欄位資料
    fields_info = []
    for field in describe['fields']:
        fields_info.append({
            'Label': field['label'],
            'API Name': field['name'],
            'Data Type': field['type'],
            'Is Formula': field['calculated']
        })

    # 轉成 DataFrame 顯示（可匯出 Excel）
    df = pd.DataFrame(fields_info)
    df = df.sort_values('Label')
    print(df)

    df.to_excel(f'./metaData/{object_name}_fields_metadata.xlsx', index=False)