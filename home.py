# streamlit_app.py
import streamlit as st
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString, Polygon
import folium
from streamlit_folium import st_folium
import geopandas as gpd
from streamlit_elements import elements, dashboard, mui, editor, media, lazy, sync, nivo


st.set_page_config(page_title='Nasa Fire Detection', layout='wide')

# Add a title
st.title("Nasa Fire Detection")

# Add text
st.write("Welcome to COOP Project")



# Fire point
firepoint_gdf = gpd.read_file(r'C:\coop_project_fire_spot\Fire-Spot-Thailand\data\2023-05-22')
df = firepoint_gdf.loc[:, ['latitude', 'longitude', 'confidence', 'th_date', 'th_time', 'ADM3_TH', 'ADM2_TH', 'ADM1_TH']]
def mapping_color(x):
    if 0 <= x <= 50:
        return 'green'
    elif 51 <= x <= 80:
        return 'orange'
    elif 81 <= x <= 100:
        return 'red'

firepoint_gdf['color'] = firepoint_gdf['confidence'].map(mapping_color)

with st.container():
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.selectbox('จังหวัด', [])

    with col2:
        st.selectbox('อำเภอ', [])
    
    with col3:
        st.selectbox('ตำบล', [])

    map_col, table_col = st.columns([1, 1])
    with map_col:
        # Create a Folium Map
        m = folium.Map(location=[13.747859255857563, 100.55926174468401], zoom_start=6, crs='EPSG3857')

        fg = folium.FeatureGroup(name="Fire Point")

        for point in firepoint_gdf.itertuples():
            fg.add_child(
                folium.Marker(
                    location=[point.latitude, point.longitude],
                    # popup=f"{point.ADM3_TH}, {point.ADM2_TH}, {point.ADM1_TH}",
                    tooltip=f"{point.ADM3_TH}, {point.ADM2_TH}, {point.ADM1_TH}",
                    icon=folium.Icon(color=point.color)
                    # if capital.state == st.session_state["selected_state"]
                    # else None,
                )
            )

        # Display the map in the Streamlit app
        st_folium(m, feature_group_to_add=fg, width=600, height=600)

    with table_col:
        tab1, tab2 = st.tabs(["ข้อมูล", "รายงานสรุปรายวัน"])
        with tab1:
            st.write(df)



