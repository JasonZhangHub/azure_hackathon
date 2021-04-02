# first embedding works perfectly if hosted via discourse, which we don't
# from streamlit_discourse import st_discourse
# https://discuss.streamlit.io/t/discourse-component/8061
# http://20.44.228.152/t/conditions-in-malaysia/17
# discourse_url = "20.44.228.152"
# topic_id = 17
# st_discourse(discourse_url, topic_id)


# with a 'button' style
from bokeh.models.widgets import Div
import streamlit as st

if st.button('Go to Lidas Forum'):
    js = "window.open('http://20.44.228.152)"  # New tab or window
    js = "window.location.href = 'http://20.44.228.152'"  # Current tab
    html = '<img src onerror="{}">'.format(js)
    div = Div(text=html)
    st.bokeh_chart(div)

# alternatively, with a 'link' style
link = '[Go to Lidas Forum](http://20.44.228.152)'
st.markdown(link, unsafe_allow_html=True)