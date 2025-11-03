# STREAMLIT MENTAL HEALTH EDA WEB PAGE
# Luna Pérez Troncoso

#-----------LIBRARIES LOADING-------------

import streamlit as st
import numpy as np
import pandas as pd
import geopandas as gpd
import seaborn as snss
import folium
import matplotlib as mpl
import streamlit_folium as sf
import branca.colormap as cm
from folium import plugins

#-----------DATAFRAME LOADING-------------

df_mh=pd.read_csv("./data/mental_health/1- mental-illnesses-prevalence.csv")
df_mh_burden=pd.read_csv("./data/mental_health/2- burden-disease-from-each-mental-illness(1).csv")
df_mh.columns=["country","code","year","Schizophrenia","Depressive","Anxiety","Bipolar","Eating"]
df_mh_income = df_mh[(df_mh.country =='Low-income countries')|(df_mh.country =='Lower-middle-income countries')|(df_mh.country =='Upper-middle-income countries')|(df_mh.country =='High-income countries')]
df_mh.drop(df_mh.index[(df_mh.country =='Low-income countries')|(df_mh.country =='Lower-middle-income countries')|(df_mh.country =='Upper-middle-income countries')|(df_mh.country =='High-income countries')],axis=0,inplace=True)
df_mh_world=df_mh[df_mh.country =="World"]
df_mh.drop(df_mh.index[(df_mh.country =='European Union (27)')|(df_mh.country =="World")],inplace=True)
df_mh_cont = df_mh[(df_mh.country =="Asia (IHME GBD)")|(df_mh.country =='Europe (IHME GBD)')|(df_mh.country =='America (IHME GBD)')|(df_mh.country =='Africa (IHME GBD)')]
df_mh.drop(df_mh.index[(df_mh.country =="Asia (IHME GBD)")|(df_mh.country =='Europe (IHME GBD)')|(df_mh.country =='America (IHME GBD)')|(df_mh.country =='Africa (IHME GBD)')],axis=0,inplace=True)
df_mh_burden.columns=["country","code","year","Schizophrenia","Depressive","Anxiety","Bipolar","Eating"]
df_mh_burden_income = df_mh_burden[(df_mh_burden.country == 'Low income (WB)')|(df_mh_burden.country == "Lower middle income (WB)")|(df_mh_burden.country =='Middle income (WB)')|(df_mh_burden.country =='High income (WB)')]
df_mh_burden.drop(df_mh_burden.index[(df_mh_burden.country == 'Low income (WB)')|(df_mh_burden.country == "Lower middle income (WB)")|(df_mh_burden.country =='Middle income (WB)')|(df_mh_burden.country =='High income (WB)')],axis=0,inplace=True)
df_mh_burden_WB = df_mh_burden[(df_mh_burden.country =='Europe & Central Asia (WB)')|(df_mh_burden.country =='East Asia & Pacific (WB)')|(df_mh_burden.country =='Latin America & Caribbean (WB)')|(df_mh .country =='Middle East & North Africa (WB)')|(df_mh_burden.country =='North America (WB)')|(df_mh_burden.country =='South Asia (WB)')|(df_mh_burden.country =='Sub-Saharan Africa (WB)')]
df_mh_burden.drop(df_mh_burden.index[(df_mh_burden.country =='Europe & Central Asia (WB)')|(df_mh_burden.country =='East Asia & Pacific (WB)')|(df_mh_burden.country =='Latin America & Caribbean (WB)')|(df_mh_burden.country =='Middle East & North Africa (WB)')|(df_mh_burden.country =='North America (WB)')|(df_mh_burden.country =='South Asia (WB)')|(df_mh_burden.country =='Sub-Saharan Africa (WB)')],axis=0,inplace=True)
df_mh_burden_world=df_mh_burden[df_mh_burden.country =="World"]
df_mh_burden_cont = df_mh_burden[(df_mh_burden.country =='Western Pacific Region (WHO)')|(df_mh_burden.country =='Eastern Mediterranean Region (WHO)')|(df_mh_burden.country =='European Region (WHO)')|(df_mh_burden.country =='Region of the Americas (WHO)')|(df_mh_burden.country =='African Region (WHO)')|(df_mh_burden.country =='South-East Asia Region (WHO)')]
df_mh_burden.drop(df_mh_burden.index[(df_mh_burden.country =='Western Pacific Region (WHO)')|(df_mh_burden.country =='Eastern Mediterranean Region (WHO)')|(df_mh_burden.country =='European Region (WHO)')|(df_mh_burden.country =='Region of the Americas (WHO)')|(df_mh_burden.country =='African Region (WHO)')|(df_mh_burden.country =='South-East Asia Region (WHO)')|(df_mh_burden.country =="World")|(df_mh_burden.country =='OECD Countries')],axis=0,inplace=True)

df_mh_mean=df_mh.iloc[:,1:].groupby("code").mean().iloc[:,1:]
df_mh_mean.reset_index(inplace=True,names=["code"])
df_mh_burden_mean=df_mh_burden.iloc[:,1:].groupby("code").mean().iloc[:,1:]
df_mh_burden_mean.reset_index(inplace=True,names=["code"])
df_mh_world_mean=df_mh_world.drop(["year","code"],axis=1).set_index("country").groupby("country").mean()
df_mh_mean2=df_mh.drop(["year","code"],axis=1).set_index("country").groupby("country").mean()
df_mh_burden_world_mean=df_mh_burden_world.drop(["year","code"],axis=1).set_index("country").groupby("country").mean()
df_mh_burden_mean2=df_mh_burden.drop(["year","code"],axis=1).set_index("country").groupby("country").mean()
fname = 'countries.geo.json'
geo = gpd.read_file(fname)
geo_data_1990=geo.merge(df_mh_burden[df_mh_burden.year==1990],left_on="id",right_on="code",how="inner")
geo_data_2019=geo.merge(df_mh_burden[df_mh_burden.year==2019],left_on="id",right_on="code",how="inner")
df_mh_1990=df_mh[df_mh.year==1990].drop(["year","code"],axis=1).set_index("country")
df_mh_2019=df_mh[df_mh.year==2019].drop(["year","code"],axis=1).set_index("country")
geo_data_1990b=geo.merge(df_mh_burden[df_mh_burden.year==1990],left_on="id",right_on="code",how="inner")
geo_data_2019b=geo.merge(df_mh_burden[df_mh_burden.year==2019],left_on="id",right_on="code",how="inner")
df_mh_burden_1990=df_mh_burden[df_mh_burden.year==1990].drop(["year","code"],axis=1).set_index("country")
df_mh_burden_2019=df_mh_burden[df_mh_burden.year==2019].drop(["year","code"],axis=1).set_index("country")


# ---------- PAGE CONFIGURATION ----------

st.set_page_config(page_title="Global Mental Health EDA",page_icon="🧠",layout="wide",initial_sidebar_state="expanded")

# ---------- CUSTOM CSS STYLING ----------

st.markdown(
"""
    <style>
    /* SELECTBOX */
    .stSelectbox label {
        font-size: 16px !important;
        font-weight: 500 !important;
        color: #391550 !important;
    }
    /* INFO BOX COLOR CUSTOMIZATION */
    div[data-testid="stInfo"] {
        border-left: 6px solid #0747d4 !important;
        background-color: #F0F2F6 !important;
        color: #391550 !important;
    }
    /* Custom highlight box (placeholder) */
    .highlight-box {
        border-left: 6px solid #0747d4;
        background-color: #F0F2F6;
        color: black;
        padding: 12px 16px;
        border-radius: 6px;
        margin: 12px 0;
        font-size: 15px;
    }

    /* Author analysis box */
    .author-box {
        border-left: 6px solid #0747d4;
        background-color: #F0F2F6;
        color: black;
        padding: 12px 16px;
        border-radius: 6px;
        margin: 12px 0;
        font-size: 14.5px;
    }
    </style>
    """
  ,unsafe_allow_html=True)

# ---------- APP HEADER ----------

st.markdown('''<h1 style="text-align: center;color: black;"> <b>Global Mental Health EDA Dashboard</b></h1>
    <h5 style="text-align: center;color: gray"> Luna Pérez Troncoso </h5>''', unsafe_allow_html=True)
st.markdown("---")

# ---------- SIDEBAR NAVIGATION ----------

st.sidebar.title("Navigation Menu")
page = st.sidebar.radio(
    "Select Section:",
    (
        "🏠 Home",
        "📚 Introduction",
        "🗐 Data Description and Sources",
        "📊 Global Statistics",
        "🌐 Cross-Country Distributions",
        "📈 General Cross-Country Progressions",
        "🗺️ Geographic Regions Based Analysis",
        "💰 Income-Level Based Analysis",
        "🚩 Outlying Countries Visualization",
        "🔗 Disorders' Metrics Correlations",
        "🌍 Global Choropleth Maps",
        "🕰️ Comparison of Choropleth Maps by Year",
    ),
)

def highlight_box(text: str):
    html = f'''<div class="highlight-box">
    
    🔹 {text}
    
    </div>'''
    st.markdown(html, unsafe_allow_html=True)

def author_box(md_text: str):
    html = f'<div class="author-box">{md_text}</div>'
    st.markdown(html, unsafe_allow_html=True)


# ---------- SECTION TEMPLATE ----------
def section_with_selectbox(title, chart_options):
    st.header(title)

    # selectone (single choice)
    selected = st.selectbox("Select visualization:", chart_options, index=0)

    # Subheader and custom highlight box (uses #391550 accent)
    st.subheader(selected)
    highlight_box(f"Placeholder for **{selected}** visualization.")

    # separator
    st.markdown("<br></br>",unsafe_allow_html=True)

    # checkbox to show author's analysis
    show_analysis = st.checkbox("Show Author’s Analysis", value=False)
    if show_analysis:
        # You can replace the text below with actual markdown content
        author_md = """
        <h4 style="margin:0 0 8px 0;">✍️ Author’s Analysis</h4>
        <p style="margin:0;">
        This section provides the author's interpretation and concise analytical commentary 
        about the selected visualization, highlighting key patterns, anomalies, and suggested next steps.
        </p>
        """
        author_box(author_md)


# ---------- PAGE CONTENTS ----------

if page == "🏠 Home":
    st.header("Welcome to the Global Mental Health EDA")
    st.markdown("""
        This project aims to provide a **comprehensive exploration** of global mental health data, 
        covering major disorders such as anxiety, depression, bipolar, eating disorders, and schizophrenia.

        Through this dashboard, you can:
        - **Explore global statistical summaries**
        - **Visualize distributions** of prevalence and burden across countries
        - **Track long-term trends** across income levels and world regions
        - **Identify outliers and correlations** between disorder metrics
        - **Inspect global and temporal choropleth maps**
        
        ---
        ← *Use the sidebar to select any analytical section and explore the interactive visuals.*
        """)

   
elif page == "📚 Introduction":
    st.header("📚 Introduction")
    st.markdown("""
        **Mental health plays a fundamental role in the overall well-being of individuals and the stability of societies**. It shapes how people think, feel, and act, influencing their relationships, productivity, and quality of life. When mental health deteriorates, **the consequences extend beyond the individual, affecting families, workplaces, and communities at large**.

        Across the globe, mental health disorders represent a **growing public health concern**. Hundreds of millions of people experience conditions such as anxiety and depression every year, and these numbers continue to rise. It is estimated that nearly **one in three women and one in five men will experience a major depressive episode at some point in their lives**. Although disorders like schizophrenia or bipolar disorder are less frequent, their social and economic impact remains profound.

        **This exploratory data analysis (EDA) aims to investigate the global prevalence and burden of mental health disorders** across countries, continents, and socioeconomic regions. In adition to this demographic factors analysis, the study **explores how behavioral, and lifestyle factors** (such as gender, age, sleep patterns, physical activity, employment status, income level, and substance use) **relate to the two of the most prevalent mental health conditions: anxiety and depression**.

        By identifying global trends and potential contributing factors, **this analysis seeks to provide a clearer understanding of how mental health challenges manifest across different populations and what patterns may inform prevention and intervention strategies**.

        <br/><br/>

        """,unsafe_allow_html=True)


elif page =="🗐 Data Description and Sources":
    st.header("🗐 Data Description and sources")
    st.markdown("""
            The both datasets are composed by **two text columns**. The first one identify the **entities** (country, continent, geographic region or grouped countries data classified by income level), whereas the second one refers to the **year**. Each entity and year has information of the **prevalence and** the **burden** of five relevant **mental health disorders**: **anxiety** disorders, **bipolar** disorders, **depressive** disorders, **eating** disorders and **schizophrenia** spectrum disorders.   
                 
            Both prevalence and burden data are age-standardized and comes from both mixed sex. **Prevalence** data is **expressed in percentages** of prevalence, whereas **burden** is **meassured by Disability-Adjusted Life Years (DALYs) rate per 100.000 Population**. Disability-adjusted life years (DALYs) represent the sum of years lost to premature death and years lived with disability.

            <p align="center"><img src="https://nccid.ca/wp-content/uploads/sites/2/2015/03/gbd1.png"/></p>
            
            ---

        """,unsafe_allow_html=True)
    st.header("Data Sources")
    st.markdown("""
        Global mental health disorders prevalence and burden data were obtained from a [kaggle dataset](https://www.kaggle.com/datasets/imtkaggleteam/mental-health) shared by Mohamadreza Momeni in CSV format.   
                  
        This data was collected throught [OurWorldInData](https://ourworldindata.org/) platform from two main sources: [Global Burden of Disease study by Institute for Health Metrics and Evaluation (GBD-IHME)](https://ghdx.healthdata.org/) from the University of Washington and [World Health Organization (WHO)](https://www.who.int/).

        <br/><br/>
        """,unsafe_allow_html=True)  


elif page == "📊 Global Statistics":
    st.header("📊 Global Statistics")
    selected = st.selectbox("Select visualization:", ["Global Descriptive Statistics of Prevalence by Disorder","Global Descriptive Statistics of Burden by Disorder","Overall Summary Prevalence Statistics","Overall Summary Burden Statistics"], index=0)
    st.subheader(selected)
    if selected == "Global Descriptive Statistics of Prevalence by Disorder":
        st.markdown('''
                    <div class="highlight-box">
            
                    It's important to emphasize that **standard deviations do not represent the variation of prevalence and burden through the different countries**. These standard deviations summerize the variation of the global prevalence of these disorders between 1990 and 2019.")
        
                    </div>
                    ''',unsafe_allow_html=True)
        st.markdown("<br/><br/>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;color: gray'>Age Standarized Global Mental Health Disorders Prevalence (%) Statistics<h5/>",unsafe_allow_html=True)
        st.dataframe(df_mh_world.describe().iloc[1:,1:].T.style.background_gradient(cmap="rocket_r", axis=0),use_container_width=True)
        st.image("./img/bar.png",use_column_width= "always")

    if selected == "Global Descriptive Statistics of Burden by Disorder":
        st.markdown('''
                    <div class="highlight-box">
            
                    It's important to emphasize that **standard deviations do not represent the variation of prevalence and burden through the different countries**. These standard deviations summerize the variation of the global prevalence of these disorders between 1990 and 2019.")
        
                    </div>
                    ''',unsafe_allow_html=True)
        st.markdown("<br/><br/>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;color: gray'>Age Standarized Global Mental Health Disorders DALYs Rate per 100000 Population Statistics<h5/>",unsafe_allow_html=True)
        st.dataframe(df_mh_burden_world.describe().iloc[1:,1:].T.style.background_gradient(cmap="rocket_r", axis=0),use_container_width=True)
        st.image("./img/bar.png",use_column_width= "always")

    if selected == "Overall Summary Prevalence Statistics":
        st.markdown("<br/><br/>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;color: gray'>Age Standarized Cross-Country Mental Health Disorders Prevalence (%) Statistics<h5/>",unsafe_allow_html=True)
        st.dataframe(df_mh.describe().iloc[1:,1:].T.style.background_gradient(cmap="rocket_r", axis=0),use_container_width=True)
        st.image("./img/bar.png",use_column_width= "always")

    if selected == "Overall Summary Burden Statistics":
        st.markdown("<br/><br/>", unsafe_allow_html=True)
        st.markdown("<h5 style='text-align: center;color: gray'>Age Standarized Cross-Country Mental Health Disorders DALYs Rate per 100000 Population Statistics<h5/>",unsafe_allow_html=True)
        st.dataframe(df_mh_burden.describe().iloc[1:,1:].T.style.background_gradient(cmap="rocket_r", axis=0),use_container_width=True)
        st.image("./img/bar.png",use_column_width= "always")


    # separator
    st.markdown("---")

    # checkbox to show author's analysis
    show_analysis = st.checkbox("Show Author’s Analysis", value=True)
    if show_analysis:
        st.markdown("""
        <h4 style="margin:0 0 8px 0;">✍️ Author’s Analysis</h4>
                    
        <div class="author-box">  

        <p style="margin:0;">         
        
        When analyzing both prevalence and DALY rates together, a clear pattern emerges:
        - **Depressive and anxiety disorders** are the **most prevalent globally** (≈3.5–3.8%) but show a **moderate individual burden** (≈105–185 DALYs). This suggests that while they are **widespread**, their average **severity per case is lower** compared to less common disorders.
        - In contrast, **schizophrenia and eating disorders** have very **low prevalence** (≈0.16–0.29%) but high DALY rates (≈360–594), indicating a **severe impact on individual** functioning and **quality of life**.
        - **Bipolar disorder** lies in between, with **moderate values in both prevalence (≈0.49%) and burden (≈34 DALYs)**.
        Overall, this combined view highlights two key challenges for global mental health:
        - High-prevalence disorders (depression, anxiety) require broad preventive and treatment coverage due to their societal reach.
        - Low-prevalence but high-burden disorders (schizophrenia, eating disorders) demand specialized and intensive care resources to reduce individual disability.

        </p>
        <div/>                                                     
        """, unsafe_allow_html=True)

        st.markdown("<br/><br/>", unsafe_allow_html=True)

elif page == "🌐 Cross-Country Distributions":
    section_with_selectbox(
        "🌐 Cross-Country Distributions",
        [   "Global DALYs Distribution by Disorder",
            "Prevalence Distributions",
            "DALYs Distributions",
            "Prevalence vs. Burden Scatterplots",
        ],
    )

elif page == "📈 General Cross-Country Progressions":
    section_with_selectbox(
        "📈 General Cross-Country Progressions",
        [
            "Prevalence Trends (1990–2017)",
            "Burden (DALYs) Trends (1990–2017)",
            "Disorder-Specific Progression Comparison",
        ],
    )

elif page == "🗺️ Geographic Regions Based Analysis":
    section_with_selectbox(
        "🗺️ Geographic Regions Based Analysis",
        [
            "Regional Mean Prevalence Comparison",
            "Regional Burden Comparison",
            "Regional Time Series Trends",
        ],
    )

elif page == "💰 Income-Level Based Analysis":
    section_with_selectbox(
        "💰 Income-Level Based Analysis",
        [
            "Prevalence by Income Level",
            "DALYs Rate by Income Level",
            "Temporal Trends by Income Level",
        ],
    )

elif page == "🚩 Outlying Countries Visualization":
    section_with_selectbox(
        "🚩 Outlying Countries Visualization",
        [
            "Top 10 Countries Above Global Mean (by Disorder)",
            "Bottom 10 Countries Below Global Mean (by Disorder)",
            "Z-score Maps or Boxplots",
        ],
    )

elif page == "🔗 Disorders' Metrics Correlations":
    section_with_selectbox(
        "🔗 Disorders' Metrics Correlations",
        [
            "Correlation Matrix (Prevalence & DALYs)",
            "Scatterplots by Disorder Pair",
            "Heatmap of Cross-Disorder Relationships",
        ],
    )

elif page == "🌍 Global Choropleth Maps":
    st.header("🌍 Global Choropleth Maps")
    selected = st.selectbox("Select visualization:", ["Global Prevalence Choropleth Maps","Global Burden Choropleth Maps"], index=0)
    if selected == "Global Prevalence Choropleth Maps":
        selected_d = st.selectbox("Select disorder group:", ["Anxiety disorders","Bipolar disorders","Depressive disorders","Eating disorders","Schizophrenia disorders"], index=0)
        st.markdown(" ")
        st.markdown(f"<h5 style='text-align: center;color: gray'>Global {selected_d} Prevalence Choropleth Maps<h5/>",unsafe_allow_html=True)
        selected_key=selected_d.replace(" disorders","")
        geo_data=geo.merge(df_mh_mean,left_on="id",right_on="code",how="inner")
        colormap = cm.linear.YlOrRd_09.scale(geo_data[selected_key].min(), geo_data[selected_key].max()).to_step(7)
        m = folium.Map(location=[0,0],zoom_start=2,width=1030,height=1000,control_scale=True)
        folium.TileLayer('CartoDB positron',name="Light Map",control=False,attr = "Luna Pérez Troncoso").add_to(m)
        colormap.caption = f"{selected_key} Disorders Prevalence %"
        style_function = lambda x: {"weight":0.1,'color':'black','fillColor':colormap(x['properties'][selected_key]), 'fillOpacity':0.9}
        highlight_function = lambda x: {'fillColor': '#000000', 'color': '#FFFFFF', 'fillOpacity': 0.5, 'weight': 0.5}
        NIL=folium.features.GeoJson(geo_data,style_function=style_function,control=False,highlight_function=highlight_function,tooltip=folium.features.GeoJsonTooltip(fields=['name',selected_key],aliases=['Country',f'{selected_key} Disorders Prevalence %'],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),sticky=True))
        colormap.add_to(m)
        m.add_child(NIL)
        sf.st_folium(m,width=1030, height=1000)

        st.markdown("<br/><br/>", unsafe_allow_html=True)
        st.markdown("---")

        show_dataframe1 = st.checkbox("Show Fold Change Pertentage DataFrame", value=False)       
        if show_dataframe1:
            st.image("./img/bar2.png",use_column_width= "always")
            cmap = mpl.colormaps['bwr']
            st.dataframe(pd.DataFrame(100*df_mh_mean2.values/df_mh_world_mean.values,columns=df_mh_mean2.columns,index=df_mh_mean2.index).style.background_gradient(cmap=cmap, vmin=50,vmax=150),use_container_width=True)
            st.markdown("<br/><br/>", unsafe_allow_html=True)
        st.markdown("---")

        show_analysis = st.checkbox("Show Author’s Analysis", value=True)
        if show_analysis:
            st.markdown("""
            <h4 style="margin:0 0 8px 0;">✍️ Author’s Analysis</h4>
                        
            <div class="author-box">  

            <p style="margin:0;">         
                    
            **Schizophrenia**
            - **Highest deviations:** The **United States**, **New Zealand**, **Australia**, and several **Western European nations** (Netherlands, Ireland) display **substantially higher prevalence** than the global mean.   
            - **Lowest deviations:** **Sub-Saharan African nations** such as **Somalia, Malawi, Mozambique, Burundi**, and the **Democratic Republic of Congo** are positioned **far below the world average**.  
            - **Interpretation:** The pattern suggests that **schizophrenia is more frequently diagnosed in high-income contexts**, likely due to **better detection systems**, while **underdiagnosis and limited psychiatric resources** explain the low apparent prevalence in poorer regions.

            **Depressive Disorders**
            - **Highest deviations:** The **most extreme values** are found in **African and Middle Eastern countries** like **Uganda, Palestine, Greenland, and the Central African Republic**.
            - **Lowest deviations:** On the other end, **East Asian countries** (notably **Japan, South Korea, Singapore, and Myanmar**) display the **lowest fold changes**,  **60% to 45%**.  
            - **Interpretation:** These results point to a **dual cultural and socioeconomic influence**,**high measured depression** in low-resource regions may reflect **social instability, conflict, and limited support systems**, while **East Asian underrepresentation** could stem from **underreporting due to stigma and cultural norms** that discourage seeking mental health care.

            **Anxiety Disorders**
            - **Highest deviations:** **Portugal, Brazil, New Zealand, and several Northern European nations** (Norway, Ireland, Switzerland, Netherlands) show **significantly elevated anxiety prevalence**.  
            - **Lowest deviations:** Conversely, **Central and East Asian countries**, including **Uzbekistan, Kyrgyzstan, Mongolia, and Vietnam**, fall **well below the global mean**.  
            - **Interpretation:** Anxiety appears **most pronounced in Western societies**, where **lifestyle stressors and cultural openness to diagnosis** contribute to higher measured rates, while **lower values in Asia** likely reflect a **combination of cultural minimization and limited diagnostic exposure**.

            **Bipolar Disorders**
            - **Highest deviations:** The **Oceania and Western Hemisphere** dominate the top ranks, **New Zealand, Australia, Brazil, the UK, and several South American countries** exhibit **much higher prevalence** than the global average.  
            - **Lowest deviations:** **East Asian and Pacific island countries** (e.g., **China, North Korea, Taiwan, Papua New Guinea, Micronesia**) display **substantially lower levels**.  
            - **Interpretation:** This bipolar pattern suggests **strong regional clustering**, where **diagnostic sophistication and awareness** in wealthier regions contrast with **significant underrecognition** in developing nations.

            **Eating Disorders**
            - **Highest deviations:** The **most striking differences globally**, with **Australia, Monaco, New Zealand, Spain, and Italy** showing **massive positive deviations**.  
            - **Lowest deviations:** **Sub-Saharan and Southeast Asian countries** such as **Somalia, Ethiopia, Myanmar, Cambodia**, and **Mozambique** appear **far below the mean**.  
            - **Interpretation:** Eating disorders are **heavily concentrated in high-income Western contexts**, strongly tied to **cultural ideals of thinness and social comparison**, while **largely absent or underdetected** in regions with different beauty norms or food insecurity.

            In conclusion, the results reveal a **clear geographical and socioeconomic polarization**, where **high-income nations tend to exceed global means**, while **low-income and lower-middle-income countries fall well below them**. **Wealthier nations show higher prevalence and greater diagnostic visibility**, **poorer nations remain underrepresented in clinical data** — masking potentially significant unmet needs. Breaking this trend, in **depressive disorders**, some **African and conflict-affected regions** surpass global averages, reflecting **psychosocial stressors** and **humanitarian crises** rather than diagnostic bias. The results thus reinforce that **mental health prevalence patterns are shaped not only by biology, but by culture, reporting practices, and structural disparities in healthcare access**.

            </p>
            <div/>                                                     
            """, unsafe_allow_html=True)
            st.markdown("<br/><br/>", unsafe_allow_html=True)


    if selected == "Global Burden Choropleth Maps":
        selected_d = st.selectbox("Select disorder group:", ["Anxiety disorders","Bipolar disorders","Depressive disorders","Eating disorders","Schizophrenia disorders"], index=0)
        st.markdown(" ")
        st.markdown(f"<h5 style='text-align: center;color: gray'>Global {selected_d} DALYs Rate Choropleth Maps<h5/>",unsafe_allow_html=True)
        selected_key=selected_d.replace(" disorders","")
        geo_data=geo.merge(df_mh_burden_mean,left_on="id",right_on="code",how="inner")
        colormap = cm.linear.YlOrRd_09.scale(geo_data[selected_key].min(), geo_data[selected_key].max()).to_step(7)
        m = folium.Map(location=[0,0],zoom_start=2,width=1030,height=1000,control_scale=True)
        folium.TileLayer('CartoDB positron',name="Light Map",control=False,attr = "Luna Pérez Troncoso").add_to(m)
        colormap.caption = f"{selected_key} Disorders DALYs Rate per 100000 population"
        style_function = lambda x: {"weight":0.1,'color':'black','fillColor':colormap(x['properties'][selected_key]), 'fillOpacity':0.9}
        highlight_function = lambda x: {'fillColor': '#000000', 'color': '#FFFFFF', 'fillOpacity': 0.5, 'weight': 0.5}
        NIL=folium.features.GeoJson(geo_data,style_function=style_function,control=False,highlight_function=highlight_function,tooltip=folium.features.GeoJsonTooltip(fields=['name',selected_key],aliases=['Country',f'{selected_key} Disorders DALYs Rate per 100000 population'],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),sticky=True))
        colormap.add_to(m)
        m.add_child(NIL)
        sf.st_folium(m,width=1030, height=1000)
        st.markdown("<br/><br/>", unsafe_allow_html=True)
        st.markdown("---")

        show_dataframe2 = st.checkbox("Show Fold Change Percentage DataFrame", value=False)
        if show_dataframe2:
            cmap = mpl.colormaps['bwr']
            st.dataframe(pd.DataFrame(100*df_mh_burden_mean2.values/df_mh_burden_world_mean.values,columns=df_mh_burden_mean2.columns,index=df_mh_burden_mean2.index).style.background_gradient(cmap=cmap, vmin=50,vmax=150),use_container_width=True)
        st.markdown("---")

        show_analysis = st.checkbox("Show Author’s Analysis", value=True)
        if show_analysis:
            st.markdown("""
            <h4 style="margin:0 0 8px 0;">✍️ Author’s Analysis</h4>
                          
            <div class="author-box">  

            <p style="margin:0;">         
                    
            **Schizophrenia**
            - **Highest-burden countries:** **Uganda, Palestine, Greenland, Central African Republic, Congo, Angola, Equatorial Guinea, Gabon, Gambia, Greece**.  
            - **Lowest-burden countries:** Sub-Saharan African and several East Asian nations.  
            - **Interpretation:** Elevated DALY rates in certain African and conflict-affected regions reflect **high disease burden**, whereas lower rates in other low-income countries may partly result from **limited diagnostic capacity**, suggesting potential underestimation.

            **Depressive Disorders**
            - **Highest-burden countries:** **United States, New Zealand, Australia, Netherlands, Greenland, Ireland, Guam, Northern Mariana Islands, Singapore, Vietnam**.  
            - **Lowest-burden countries:** East Asian nations (Japan, South Korea, Myanmar) and some low-income regions.  
            - **Interpretation:** Burden is elevated in high-income countries due to **higher reporting and treatment access**, whereas cultural norms and healthcare limitations may contribute to lower apparent DALYs in other regions.

            **Anxiety Disorders**
            - **Highest-burden countries:** **New Zealand, Northern Ireland, Australia, England, Brazil, Paraguay, UK, Israel, Argentina, Chile**.  
            - **Lowest-burden countries:** Central and East Asian nations, including Vietnam, Kyrgyzstan, Uzbekistan.  
            - **Interpretation:** DALY burden for anxiety is concentrated in Western countries, likely reflecting both **lifestyle stressors and healthcare detection**, while low-burden regions may experience **underdiagnosis**.

            **Bipolar Disorders**
            - **Highest-burden countries:** **Australia, Monaco, New Zealand, Spain, Italy, Luxembourg, Austria, San Marino, Andorra, Switzerland**.  
            - **Lowest-burden countries:** East Asian and Pacific Island nations.  
            - **Interpretation:** High DALY rates indicate **substantial disease burden** in wealthier countries with robust diagnostic systems, whereas low values in developing regions may reflect **underrecognition and reporting gaps**.

            **Eating Disorders**
            - **Highest-burden countries:** **Portugal, Brazil, New Zealand, Iran, Northern Ireland, Norway, Netherlands, Ireland, Switzerland, Cyprus**.  
            - **Lowest-burden countries:** Sub-Saharan and Southeast Asian countries.  
            - **Interpretation:** Burden is heavily concentrated in high-income contexts, driven by **cultural and lifestyle factors**, while low-burden regions may face **diagnostic gaps or different cultural drivers of disease**.

            Wealthier nations show **consistently higher DALY rates** across multiple mental health disorders. Lower-income countries often appear underrepresented, although some conflict-affected regions (e.g., certain African countries) show extreme burden. **Bipolar and anxiety disorders exhibit DALY rates 6 times above the global mean**, illustrating concentrated disease burden **in specific countries**. The combined analysis of countries with **highest and lowest DALY rates** demonstrates that mental health burden is **shaped by socioeconomic, cultural, and healthcare factors**, not only biological risk. These results highlight the need for **globally targeted mental health strategies** that address both **underdiagnosis in low-resource regions** and **high disease burden in wealthier countries**.

            </p>
            <div/>                                                     
            """, unsafe_allow_html=True)

        st.markdown("<br/><br/>", unsafe_allow_html=True)


elif page == "🕰️ Comparison of Choropleth Maps by Year":
    st.header("🕰️ Comparison of Choropleth Maps by Year")
    selected = st.selectbox("Select visualization:", ["Global Prevalence in 1990 vs 2019 Comparison Choropleth Maps","Global Burden in 1990 vs 2019 Comparison Choropleth Maps"], index=0)
    if selected == "Global Prevalence in 1990 vs 2019 Comparison Choropleth Maps":
        selected_d = st.selectbox("Select disorder group:", ["Anxiety disorders","Bipolar disorders","Depressive disorders","Eating disorders","Schizophrenia disorders"], index=0)
        st.markdown(" ")
        st.markdown(f"<h5 style='text-align: center;color: gray'>Global {selected_d} Prevalence Choropleth Maps<h5/>",unsafe_allow_html=True)
        selected_key=selected_d.replace(" disorders","")
        colormap = cm.linear.YlOrRd_09.scale(geo_data_1990[selected_key].min(), geo_data_2019[selected_key].max()).to_step(7)
        m = plugins.DualMap(location=[0,0],zoom_start=1,control_scale=True)
        folium.TileLayer('CartoDB positron',name="Light Map",control=False,attr = "Luna Pérez Troncoso").add_to(m)
        colormap.caption = f"{selected_key} Disorders Prevalence %"
        style_function = lambda x: {"weight":0.1,'color':'black','fillColor':colormap(x['properties'][selected_key]), 'fillOpacity':0.9}
        highlight_function = lambda x: {'fillColor': '#000000', 'color': '#FFFFFF', 'fillOpacity': 0.5, 'weight': 0.5}
        NIL_1990=folium.features.GeoJson(geo_data_1990,style_function=style_function,control=False,highlight_function=highlight_function,tooltip=folium.features.GeoJsonTooltip(fields=['name',selected_key],aliases=['Country',f'{selected_key} Disorders Prevalence %'],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),sticky=True))
        NIL_2019=folium.features.GeoJson(geo_data_2019,style_function=style_function,control=False,highlight_function=highlight_function,tooltip=folium.features.GeoJsonTooltip(fields=['name',selected_key],aliases=['Country',f'{selected_key} Disorders Prevalence %'],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),sticky=True))
        colormap.add_to(m.m2)
        m.m1.add_child(NIL_1990)
        m.m2.add_child(NIL_2019)
        sf.folium_static(m,width=1030, height=500)
        st.markdown("<h5 style='text-align: center;color: black'> 1990 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; 2019 <h5/>",unsafe_allow_html=True)
        st.markdown("---")

        show_dataframe1 = st.checkbox("Show Fold Change Pertentage DataFrame", value=False)       
        if show_dataframe1:
            st.image("./img/bar2.png",use_column_width= "always")
            cmap = mpl.colormaps['bwr']
            st.dataframe((df_mh_2019/df_mh_1990*100).style.background_gradient(cmap=cmap, vmin=50,vmax=150),use_container_width=True)
            st.markdown("<br/><br/>", unsafe_allow_html=True)
        st.markdown("---")

        show_analysis = st.checkbox("Show Author’s Analysis", value=True)
        if show_analysis:
            st.markdown("""
            <h4 style="margin:0 0 8px 0;">✍️ Author’s Analysis</h4>
                        
            <div class="author-box">  

            <p style="margin:0;">         
                    
            Fold-change (FC) values describe the relative change in disorder prevalence between **1990 and 2019**:
            - **FC = 100** → no net change.
            - **FC > 100** → increased prevalence.
            - **FC < 100** → decreased prevalence.

            Across all disorders and 190+ countries, FC values generally cluster between **95 and 110**, indicating **moderate but widespread shifts** rather than explosive growth or collapse. However, certain disorders and countries show **systematic trends**, suggesting changing sociocultural, diagnostic, and epidemiological dynamics. **Stable biological disorders** (schizophrenia, bipolar) remained constant. **Culturally and psychosocially sensitive disorders** (anxiety, depression, eating) have **expanded considerably**, especially in **urbanized, high-income, or rapidly modernizing societies**. Geographic differences reveal that **Western lifestyle patterns and diagnostic capacity** amplify recorded prevalence, while **limited surveillance in low-income regions** may obscure true changes.

            **Cross-Disorder Global Trends**

            | Disorder | Global Pattern | Key Insights |
            |-----------|----------------|---------------|
            | **Schizophrenia** | Stable (mostly 97–103) | Prevalence remained almost unchanged globally. Small growth in parts of SE Asia and Eastern Europe (e.g., Cambodia, Myanmar), slight declines in Western Europe. Reflects biological constancy and limited diagnostic drift. |
            | **Depressive Disorders** | Highly variable (80–115) | Strong polarization: sharp decreases (<90) in Western & Northern Europe (Austria, France, Finland), but **substantial increases** (>110) in parts of Latin America (Mexico, Uruguay) and Asia (Malaysia). Suggests rising detection and societal stress in developing high-income contexts. |
            | **Anxiety Disorders** | Systematic increase (100–110, occasionally >120) | Most consistent global rise. Largest surges in **Americas, Middle East, and South-East Asia** (Brazil, Turkey, Nepal). Only limited declines (Japan, Norway). Indicates intensification of stress-related conditions linked to urbanization, digital exposure, and economic transitions. |
            | **Bipolar Disorders** | Near-neutral (≈100) | Minimal variation globally. Small positive deviations in Australia, Uruguay, Ireland; negligible change elsewhere. Likely reflects diagnostic stability and long-term chronic nature of the condition. |
            | **Eating Disorders** | Strong upward trend, highly heterogeneous | The **most dynamic disorder**: FC values frequently exceed **130–170** (e.g., China, Myanmar, Laos, Vietnam, Australia). Indicates dramatic expansion of prevalence, tied to **Westernization, media exposure, and shifting beauty ideals**. Isolated declines (<95) in poorer African and Pacific regions (e.g., Libya, Somalia). |

            **Regional and Cultural Patterns**

            - **Europe & North America:**  
            Mixed evolution. Depressive and anxiety disorders largely increased in Southern and Eastern Europe (Portugal, Poland), while Northern Europe often shows slight declines in depression but **stable or rising anxiety**. Eating disorders exhibit the **strongest growth** in high-income Western countries, consistent with cultural and societal pressures.

            - **Asia-Pacific:**  
            Marked **surge in eating and anxiety disorders**, especially in East and South-East Asia (China +72%, Vietnam +54%, Thailand +40%). Rapid modernization, digital globalization, and changing body image norms contribute to this trend. Schizophrenia and bipolar remain mostly unchanged.

            - **Middle East & North Africa:**  
            Moderate increases in anxiety and eating disorders (Iran, Egypt, Saudi Arabia). Depression trends are mixed, with some declines (Libya) likely linked to socio-political instability and under-reporting.

            - **Sub-Saharan Africa:**  
            Slight overall increases in anxiety and schizophrenia, but **limited diagnostic growth**. Some countries (Uganda, Ghana, Tanzania) show small positive FCs, while others (Burundi, Somalia) exhibit declines, possibly due to limited health surveillance and diagnostic access.

            - **Latin America:**  
            Clear upward trajectory for anxiety and depression in several nations (Mexico, Chile, Uruguay, Brazil). Cultural shifts, economic instability, and greater recognition of mental health are probable drivers. Eating disorders also rising sharply.

            - **High-Income Island States (Australia, New Zealand, Malta):**  
            Exhibit some of the **strongest positive fold changes** in eating disorders (+130–145), reflecting both higher awareness and genuine prevalence increase.  
            
            **Notable Outliers**

            - **Equatorial Guinea (Eating FC ≈ 246)** – extreme outlier; may reflect data artefacts or emerging high-income consumption patterns.
            - **China (Eating FC ≈ 172)** – one of the strongest true increases, aligning with cultural westernization.
            - **Singapore (Depression FC ≈ 71)** – significant decline; possible under-detection or public-health progress.
            - **Norway (Depression FC ≈ 109)** and **United States (Depression FC ≈ 115)** – rising depression levels despite high income, supporting the stress–diagnosis hypothesis.
                                    
            </p>
            <div/>                                                     
            """, unsafe_allow_html=True)
            st.markdown("<br/><br/>", unsafe_allow_html=True)


    if selected == "Global Burden in 1990 vs 2019 Comparison Choropleth Maps":
        selected_d = st.selectbox("Select disorder group:", ["Anxiety disorders","Bipolar disorders","Depressive disorders","Eating disorders","Schizophrenia disorders"], index=0)
        st.markdown(" ")
        st.markdown(f"<h5 style='text-align: center;color: gray'>Global {selected_d} DALYs Rate Choropleth Maps<h5/>",unsafe_allow_html=True)
        selected_key=selected_d.replace(" disorders","")
        colormap = cm.linear.YlOrRd_09.scale(geo_data_1990b[selected_key].min(), geo_data_2019b[selected_key].max()).to_step(7)
        m = plugins.DualMap(location=[0,0],zoom_start=1,control_scale=True)
        folium.TileLayer('CartoDB positron',name="Light Map",control=False,attr = "Luna Pérez Troncoso").add_to(m)
        colormap.caption = f"{selected_key} Disorders DALYs Rate per 100000 population"
        style_function = lambda x: {"weight":0.1,'color':'black','fillColor':colormap(x['properties'][selected_key]), 'fillOpacity':0.9}
        highlight_function = lambda x: {'fillColor': '#000000', 'color': '#FFFFFF', 'fillOpacity': 0.5, 'weight': 0.5}
        NIL_1990=folium.features.GeoJson(geo_data_1990b,style_function=style_function,control=False,highlight_function=highlight_function,tooltip=folium.features.GeoJsonTooltip(fields=['name',selected_key],aliases=['Country',f'{selected_key} Disorders DALYs Rate per 100000 Population'],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),sticky=True))
        NIL_2019=folium.features.GeoJson(geo_data_2019b,style_function=style_function,control=False,highlight_function=highlight_function,tooltip=folium.features.GeoJsonTooltip(fields=['name',selected_key],aliases=['Country',f'{selected_key} Disorders DALYs Rate per 100000 Population'],
        style=("background-color: white; color: #333333; font-family: arial; font-size: 12px; padding: 10px;"),sticky=True))
        colormap.add_to(m.m2)
        m.m1.add_child(NIL_1990)
        m.m2.add_child(NIL_2019)
        sf.folium_static(m,width=1030, height=500)
        st.markdown("<h5 style='text-align: center;color: black'> 1990 &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp; 2019 <h5/>",unsafe_allow_html=True)
        st.markdown("---")

        show_dataframe2 = st.checkbox("Show Fold Change Percentage DataFrame", value=False)
        if show_dataframe2:
            cmap = mpl.colormaps['bwr']
            st.dataframe((df_mh_burden_2019/df_mh_burden_1990*100).style.background_gradient(cmap=cmap, vmin=50,vmax=150),use_container_width=True)
        st.markdown("---")

        show_analysis = st.checkbox("Show Author’s Analysis", value=True)
        if show_analysis:
            st.markdown("""
            <h4 style="margin:0 0 8px 0;">✍️ Author’s Analysis</h4>
                          
            <div class="author-box">  

            <p style="margin:0;">         
                    
            Overall, the distribution of DALYs fold-change values shows **limited global variation** (typically between 95 and 110), but **directionally divergent trends** emerge across disorders and regions. These differences reveal how **medical progress, health system capacity, and cultural factors** shape the actual lived impact of mental illness beyond prevalence alone. **Chronic and biologically rooted disorders** (schizophrenia, bipolar) maintained or increased their burden in developing regions, highlighting care inequities. **Culturally sensitive disorders** (depression, anxiety, eating) show rising burden in **high-income and rapidly modernizing countries**, where **social pressures and digital environments magnify psychological strain**. In summery, developed countries' **individuals **live longer but with persistent functional impairment**.

            **Cross-Disorder Global Trends**

            | Disorder | Global Pattern | Key Insights |
            |-----------|----------------|---------------|
            | **Schizophrenia** | Mild decrease globally (≈95–100), but increases in South & East Asia (India, Malaysia, South Korea, Vietnam). | Stable prevalence but variable outcomes: countries with limited long-term treatment (South/Southeast Asia, parts of Eastern Europe) show rising DALY rates, indicating persistent disability despite possible diagnostic progress. |
            | **Depressive Disorders** | Broad stability (≈98–104) with moderate increases in low- and middle-income nations. | Reflects partial improvements in management in high-income regions (Europe, North America) but growing severity and chronicity elsewhere. Suggests that awareness increased faster than effective care. |
            | **Anxiety Disorders** | Almost universally stable (≈99–101). | Although prevalence increased, the **burden per capita remained constant**, suggesting that anxiety disorders are **better managed or less disabling** despite spreading more widely. High-income countries show DALY plateaus, pointing to therapeutic containment. |
            | **Bipolar Disorder** | Strong and consistent increases (110–160, peaking at >170 in China, Myanmar, Vietnam). | Indicates a **rising chronic disability load**, even where prevalence barely changed. Suggests that individuals live longer with bipolar disorder but with sustained impairment, reflecting treatment-resistant or recurrent forms. |
            | **Eating Disorders** | Mild but widespread increase (≈102–108, locally >120 in some Asian and American nations). | The expansion in DALYs is less pronounced than the rise in prevalence, implying some improvement in case management. However, countries such as the UK, Spain, and Turkey show marked growth (>105), revealing persistent disability linked to cultural and social pressures. |

            **Regional and Cultural Patterns**

            - **Europe & North America:**  
            - Burden **declines slightly** for schizophrenia and depression (e.g., France, Finland, UK).  
            - **Increases for bipolar and eating disorders**, especially in Southern and Western Europe (Spain, Portugal, Italy, UK).  
            - Suggests that while medical treatment reduces mortality and some disability, **sociocultural pressures sustain functional burden** for affective and eating disorders.  
            - The **United States and Uruguay** stand out with high DALYs increases in multiple disorders (schizophrenia +22%, anxiety +5%, eating +8%), indicating a persistent mental health strain despite advanced healthcare access.

            - **Asia-Pacific:**  
            - Strong upward trends in **bipolar and schizophrenia DALYs** (India +50%, China +71%, Thailand +40%, Vietnam +54%).  
            - **Eating disorder burden rises** moderately in high-growth economies (Malaysia, Laos, Thailand).  
            - Reflects the **psychosocial cost of rapid modernization**, cultural transition, and unequal access to long-term psychiatric care.

            - **Middle East & North Africa:**  
            - Moderate increases in burden for bipolar and eating disorders (Iran, Egypt, Saudi Arabia).  
            - Slight reductions in depression and anxiety suggest growing treatment capacity in wealthier states.  
            - In contrast, **Libya** and **Syria** show mixed signals—declines in prevalence but persistent or worsening DALY rates—hinting at underreporting and disrupted healthcare access.

            - **Sub-Saharan Africa:**  
            - Generally **stable or slightly increased DALYs** (≈101–105 across disorders).  
            - Stronger rises for **bipolar** and **eating disorders** in Uganda, Tanzania, and Mozambique.  
            - Reflects emerging recognition and improved survival rather than an actual rise in disease frequency.

            - **Latin America:**  
            - **Increasing DALYs** for affective and bipolar disorders (Mexico +20%, Brazil +15%).  
            - Cultural modernization and health system strain drive worsening disability profiles, even as prevalence stabilizes.  
            - **Eating disorders** show particularly strong growth in Brazil and Mexico, reinforcing the sociocultural link between economic development and mental health burden.

            - **High-Income Island States (Australia, New Zealand, Iceland):**  
            - Bipolar disorder DALYs rose steeply (Australia +43%), suggesting that **chronic management improvements extend lifespan but not full recovery**.  
            - Slight gains in eating disorder DALYs mirror global cultural exposure and urban pressures.

            **Notable Outliers**

            - **United States (+22.7% in schizophrenia, +8.4% in eating disorders)** – suggests increasing functional impairment despite stable prevalence.  
            - **Myanmar and Vietnam (>160% DALYs increase for bipolar)** – extreme outliers driven by regional health inequities and limited psychiatric coverage.  
            - **Spain and Turkey** – strong increases across several disorders, reflecting cultural convergence and diagnostic intensification.  
            - **Singapore** – marked decline in schizophrenia DALYs (−32%), possibly due to early intervention programs and healthcare modernization.  

            </p>
            <div/>                                                     
            """, unsafe_allow_html=True)

        st.markdown("<br/><br/>", unsafe_allow_html=True)


# ---------- FOOTER ----------
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray; font-size: 1em;'>© 2025 Global Mental Health EDA — Luna Pérez Troncoso </p>",unsafe_allow_html=True)