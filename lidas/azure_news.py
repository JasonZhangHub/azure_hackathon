import json
import requests
import streamlit as st

def search_news(region):
# Add your Bing Search V7 subscription key and endpoint
    subscription_key = "a68ed4d5936c4bcfadd908844e782b85"
    search_term = region + ", COVID19"
    search_url = "https://api.bing.microsoft.com/v7.0/news/search"

    # Create parameters for the request
    headers = {"Ocp-Apim-Subscription-Key" : subscription_key}
    params  = {"q": search_term, "textDecorations": True, "textFormat": "HTML"}
    
    # Call the API
    try:
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()
    
        descriptions = [article["description"] for article in search_results["value"]]
        
        from IPython.display import HTML
        rows = "\n\n\n".join(["<tr><td>{0}</td></tr>".format(desc)
                          for desc in descriptions])
        news = HTML("<table>"+rows+"</table>")
    except:
        news = ''
    
    return news

def search_headline(region):
    # alternatively, with a 'link' style
    link = '[Click to view {} top new headlines ](http://192.168.1.7:8501/)'.format(region)
    st.markdown(link, unsafe_allow_html=True)