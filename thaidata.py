import pandas as pd

class Province:
    def __init__(self):
        self.url = r'C:\coop_project_fire_spot\Fire-Spot-Thailand\data\all_tambons.xlsx'
        self.prov_df = pd.read_excel(self.url, sheet_name='Sheet1', header=0)

    def get_all_name(self):
        return sorted(list(self.prov_df['ADM1_TH'].unique()))

class Amphoe:
    def __init__(self):
        self.url = r'C:\coop_project_fire_spot\Fire-Spot-Thailand\data\all_tambons.xlsx'
        self.prov_df = pd.read_excel(self.url, sheet_name='Sheet1', header=0)

    def get_all_name(self):
        return list(self.prov_df['ADM2_TH'].unique())
    
    def search(self, prov_name: str):
        if prov_name != '-':
            return sorted(list(self.prov_df[self.prov_df['ADM1_TH']==prov_name]['ADM2_TH'].unique()))
        else:
            return []
        
class Tambon:
    def __init__(self):
        self.url = r'C:\coop_project_fire_spot\Fire-Spot-Thailand\data\all_tambons.xlsx'
        self.prov_df = pd.read_excel(self.url, sheet_name='Sheet1', header=0)

    def get_all_name(self):
        return list(self.prov_df['ADM3_TH'].unique())
    
    def search(self, prov_name: str, amphoe_name: str):
        return sorted(list(self.prov_df[(self.prov_df['ADM1_TH']==prov_name) & (self.prov_df['ADM2_TH']==amphoe_name)]['ADM3_TH'].unique()))