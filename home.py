# streamlit_app.py
import streamlit as st
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon
import folium
from streamlit_folium import st_folium
import geopandas as gpd
from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo


st.set_page_config(layout='wide')

# Add a title
st.title("Nasa Fire Detection")

# Add text
st.write("Welcome to Streamlit!")


# Province Data
# gdf_thailand = gpd.read_file('Prov')
# province = dict(zip(gdf_thailand['Ecart_Prov'].unique(), gdf_thailand['PROV_CODE'].unique()))


# Fire point
firepoint_gdf = gpd.read_file(r'C:\coop_project_fire_spot\Fire-Spot-Thailand\data\2023-05-22')


layout = [
    # Editor item is positioned in coordinates x=0 and y=0, and takes 6/12 columns and has a height of 3.
    dashboard.Item("map", 0, 0, 6, 3),
    # Chart item is positioned in coordinates x=6 and y=0, and takes 6/12 columns and has a height of 3.
    dashboard.Item("table", 6, 0, 6, 3),
    # Media item is positioned in coordinates x=0 and y=3, and takes 6/12 columns and has a height of 4.
    # dashboard.Item("media", 0, 2, 12, 4),
]

df = firepoint_gdf.loc[:, ['latitude', 'longitude', 'confidence', 'th_date', 'th_time', 'ADM3_TH', 'ADM2_TH', 'ADM1_TH']]
# table_html = df.to_html(index=False, classes=["table", "table-striped"])

# with elements("demo"):
#     with dashboard.Grid(layout, draggableHandle=".draggable"):
#         with mui.Card(key="editor", sx={"display": "flex", "flexDirection": "column"}):
#             mui.CardHeader(title="Editor", className="draggable")
#             with mui.CardContent(sx={"flex": 1, "minHeight": 0}):

st.write(df)

# Create a Folium Map
m = folium.Map(location=[13.747859255857563, 100.55926174468401], zoom_start=6, crs='EPSG3857')

fg = folium.FeatureGroup(name="Fire Point")

for point in firepoint_gdf.itertuples():
    fg.add_child(
        folium.Marker(
            location=[point.latitude, point.longitude],
            # popup=f"{point.ADM3_TH}, {point.ADM2_TH}, {point.ADM1_TH}",
            tooltip=f"{point.ADM3_TH}, {point.ADM2_TH}, {point.ADM1_TH}",
            icon=folium.Icon(color="orange")
            # if capital.state == st.session_state["selected_state"]
            # else None,
        )
    )

# Add the geometries to the map
# folium.GeoJson(filterByProvince(fire_point_th, province.get(option)).__geo_interface__).add_to(m)

# Display the map in the Streamlit app
st_folium(m, feature_group_to_add=fg, width=600, height=600)
# st_folium(m, width=1200, height=600,)

