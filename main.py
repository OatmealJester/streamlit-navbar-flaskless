import streamlit as st
import utils as utl
from views import home,Misson,analysis,options,configuration
import pandas as pd
import plotly.express as px
st.set_page_config(layout="wide", page_title='Main Page')

st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "Misson":
        Misson.load_view()
    elif route == "analysis":
        analysis.load_view()
    elif route == "options":
        options.load_view()
    elif route == "configuration":
        configuration.load_view()
    elif route == None:
        home.load_view()
        
navigation()

