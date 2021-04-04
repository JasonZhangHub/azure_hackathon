import streamlit as st

def search_forum(region):
    # if st.button('Go to Lidas Forum'):
    #     js = "window.open('http://20.44.228.152)"  # New tab or window
    #     js = "window.location.href = 'http://20.44.228.152'"  # Current tab
    #     html = '<img src onerror="{}">'.format(js)
    #     div = Div(text=html)
    #     st.bokeh_chart(div)

    # alternatively, with a 'link' style
    link = '[Go to {} Forum](http://20.44.228.152)'.format(region)
    st.markdown(link, unsafe_allow_html=True)