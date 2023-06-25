import pandas as pd
import requests
import json

# case 1 กรณีข้อมูลเยอะมาก ๆ
# ใช้ postman เรียกใช้ api แล้ว save เป็น json ก่อนเพราะบาง api ใช้โค้ดดึงตรงไม่ได้ข้อมูลเยอะเกินไป ram เต็ม
def json_to_csv(json_path: str):
    f = open(json_path, mode='r', encoding='utf-8')
    json_data = json.load(f)
    data = pd.DataFrame(json_data)  # ใช้ข้อมูลเฉพาะที่อยู่ใน tag ที่ชื่อว่า rows
    # data = pd.DataFrame(json_data['rows'])  # ใช้ข้อมูลเฉพาะที่อยู่ใน tag ที่ชื่อว่า rows
    data.to_csv(json_path.replace('.json', '.csv'), index=False, encoding='cp874')  # เดิม path เป็น .json แต่ export เป็น csv
    f.close()

json_to_csv(r'E:\_BigData\disaster_promptdev\json\1.json')



# case 2 กรณี api เป็นแบบดึงทีละจังหวัด
def api_to_csv(api_url: str):
    path = 'C:/coop_project_fire_spot/Fire-Spot-Thailand/mylab/data.xlsx'
    prov = pd.read_excel(path, sheet_name='Sheet1', header=0)
    prov_ids = list(prov['PROV_CODE'].unique()) # ดึงไอดีของแต่ละจังหวัด

    prov_df = pd.DataFrame()
    # วนลูป id และดึงข้อมูลมาทีละจังหวัดจนครบ 77 จังหวัด
    for id in prov_ids:
        req_prov = requests.get(api_url + str(id))   # ต่อ string
        if req_prov.status_code == 200:
            prov_json = json.loads(req_prov.text)
            df = pd.DataFrame(prov_json)
            prov_df = pd.concat([prov_df, df])
    # path output ของไฟล์ csv
    prov_df.to_csv('C:/coop_project_fire_spot/Fire-Spot-Thailand/mylab/Hospital.csv', index=False, encoding='cp874')

# example api: https://edpapim.disaster.go.th/api/eoc/Hospital?province={id}
# api_to_csv('https://edpapim.disaster.go.th/api/eoc/Hospital?province=')  # เว้้น id
