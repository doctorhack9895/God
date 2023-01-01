import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="SCARY FISH", page_icon=":tada:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()    

lottie_coding = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_35nnyxzu.json")

with st.container():
    st.title(" Doctor Hack ")
    st.subheader("Hello, my dear prey, you have been captured. Don't be concerned. Everything should be read:wave:")
    st.write("You touched the link right, then you will deeply regret it.  ")
    st.write("[If you want to know more about me and my others hobbies>](shorturl.at/nBCZ5)")


with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What i do")
        st.write("##")
        st.write(
    
          "  Everyone is unaware of something unique and distinctive about me\n"

          "  1) If I am going to target someone, it will not be out of vengeance or malice.\n"

           " 2) If I get my target in my hands, I will not let it live easily; instead, I will destroy its entire life inch by inch.\n"

           " 3) If I am silent or do not make any move, it means I am planning something terrifying and ridiculously bad.\n"
        )

    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")    


with st.container():
    st.write("---")
    st.header("IF YOU LOOK HERE, YOU WILL FLEE.")
    st.subheader("MY BAD TEMPERED JOBS")
    st.write("i am a Psycho path")