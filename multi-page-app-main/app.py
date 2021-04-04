import streamlit as st
from multiapp import MultiApp
from apps import homepage, News, forum, forecastmodel # import your app modules here

app = MultiApp()

st.markdown("""
# LIDAS

Welcome to the LIDAS navigation page

""")



# Add all your application here
app.add_app("homepage", homepage.app)
app.add_app("News", News.app)
app.add_app("forum", forum.app)
app.add_app("Azureforecastmodel", Azureforecastmodel.app)

# The main app
app.run()



