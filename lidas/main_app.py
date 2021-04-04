import streamlit as st
from streamlit import components
import matplotlib.pyplot as plt
import pandas as pd
from countrymapping import COUNTRY_MAPPINGS
from azure_news import search_news,search_headline
from azure_forum import search_forum
from azure_forecast import forecast

def home(homepage_path, contact_path):
    '''The home page. '''
    with open(homepage_path, 'r', encoding='utf-8') as homepage: 
        st.write(homepage.read())
        
    contact_us_ui(contact_path, if_home=True)
    
def contact_us_ui(contact_path, if_home=False): 
    if not if_home: 
        st.write('# New Features 💡')
        st.text_input('Send us suggestions', 'Write something...')
        if_send = st.button('Send')
        if if_send: 
            st.success('Thank you:) Your suggestions have been received. ')
            st.balloons()
    with open(contact_path, 'r', encoding='utf-8') as contact: 
        st.write(contact.read())
        
def forecast_ui(forecast_ui_path, if_home=False): 
    with open(forecast_ui_path, 'r', encoding='utf-8') as forecast_ui: 
        st.write(forecast_ui.read())

def geoservice_ui(geoservice_ui_path, if_home=False): 
    with open(geoservice_ui_path, 'r', encoding='utf-8') as geoservice_ui: 
        st.write(geoservice_ui.read())

def newsfeed_ui(newsfeed_ui_path, if_home=False): 
    with open(newsfeed_ui_path, 'r', encoding='utf-8') as newsfeed_ui: 
        st.write(newsfeed_ui.read())
        
def community_ui(community_ui_path, if_home=False): 
    with open(community_ui_path, 'r', encoding='utf-8') as community_ui: 
        st.write(community_ui.read())

def main():
    '''Add control flows to organize the UI sections. '''
    st.sidebar.image('./docs/lidaslogo.png', width=250)
    st.sidebar.write('') # Line break
    st.sidebar.header('LIDAS')
    country = st.sidebar.selectbox(label = "Select a Country", index = 0,
                               options = list(COUNTRY_MAPPINGS.keys()))
    region = st.sidebar.selectbox(label = "Select a Region",   
                                  options = COUNTRY_MAPPINGS[country]) 

    side_menu_selectbox = st.sidebar.radio(
        'Menu', ('Home', 'Forecast','Geoservice','News Feed','Community'))
    if side_menu_selectbox == 'Home':
        home(homepage_path='./docs/homepage.md', contact_path='./docs/contact_us.md')
    elif side_menu_selectbox == 'Forecast':
        forecast_ui(forecast_ui_path='./docs/forecast_ui.md')
        st.markdown('Below is the trend chart and forecasted number in **{}**'.format(region))
        st.pyplot(forecast(region))
        
    elif side_menu_selectbox == 'Geoservice':
        geoservice_ui(geoservice_ui_path='./docs/geoservice_ui.md')
        option = st.selectbox(
                            'Searching',
                            ('Pharmacy', 'Clinics', 'Hospitals'))
        radius = st.selectbox(
                            'within',
                            ('5km', '10km', '15km'))
        if option =='Pharmacy' and region == 'Kuala Lumpur':
            st.image('./docs/kuala lumpur pharmcy.png')
        if option =='Clinics' and region == 'Kuala Lumpur':
            st.image('./docs/kuala lumpur clinic.png')
        if option =='Hospitals' and region == 'Kuala Lumpur':
            st.image('./docs/kuala lumpur hospital.png')
        if option =='Pharmacy' and region == 'Johor':
            st.image('./docs/johor pharmcy.png')
        if option =='Clinics' and region == 'Johor':
            st.image('./docs/johor clinic.png')
        if option =='Hospitals' and region == 'Johor':
            st.image('./docs/johor hospital.png')

    elif side_menu_selectbox == 'News Feed':
        newsfeed_ui(newsfeed_ui_path='./docs/newsfeed_ui.md')
        search_headline(region)
        region_news = search_news(region) #region html news
        raw_html = region_news._repr_html_()
        components.v1.html(raw_html, height=600, scrolling=True)
    elif side_menu_selectbox == 'Community':
        community_ui(community_ui_path='./docs/community_ui.md')
        st.markdown('Click below to view **{}** forum details'.format(region))
        search_forum(region)

if __name__ == '__main__': 
    st.set_page_config(page_title='LIDAS', page_icon='./docs/lidaslogo.png', layout='centered', initial_sidebar_state='auto')
    try: 
        main()
    except: 
        st.error('Oops! Something went wrong...')
        raise
