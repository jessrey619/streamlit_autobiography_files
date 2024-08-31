import streamlit as st
import pandas as pd

# Set the page title and icon
st.set_page_config(page_title="Garrido Autobiography", page_icon="📖")

# Set the title
st.title('Garrido Autobiography')

# Display the author's name
st.write('By: Jessrey Vincent P. Garrido')

# Sidebar with list of sections
section = st.sidebar.radio("Navigate to:", ["Personal Data", "Hobbies", "Aspirations", "Life Motto"])

id_img_url = "https://github.com/jessrey619/streamlit_autobiography_files/blob/main/ID%20Photo.jpg?raw=true"
motto_img_url = "https://github.com/jessrey619/streamlit_autobiography_files/blob/main/motto_gif.gif?raw=true"

# Divider
st.divider()

# Sample data
data = {
    'Hobby': ['Playing with Friends', 'Hanging out with my closest circle of friends', 'Reading Manga and Manhuwa and watching Anime', 'Talking with my family'],
    'Rating (1-10)': [10, 8, 7, 9]
}

df = pd.DataFrame(data)

# Content based on sidebar selection
if section == "Personal Data":
    # Tabs within Personal Data
    tab1, tab2 = st.tabs(["General Data", "Educational Background"])
    
    with tab1:
        # Custom CSS to center the content
        st.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center;">
                <img src="{id_img_url}" width="300">
                <p>ID Photo</p>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.subheader("Personal Data")
        st.write("Name: Jessrey Vincent P. Garrido")
        st.write("Age: 24")
        st.write("Birthday: March 21, 2000")
        st.write("Address: Labangon, Cebu City, Cebu, 6000")
    
    with tab2:
        st.markdown(
        f"""
        <div style="display: flex; flex-direction: column; align-items: center;">
            <h2>Educational Background</h2>
        </div>
        
        <div>
            <h3>Elementary:</h3>
            &nbsp;&nbsp;&nbsp; Saint Joseph College<br>
            &nbsp;&nbsp;&nbsp; 2007-2013
        </div>
        
        <div>
            <h3>High School:</h3>
            &nbsp;&nbsp;&nbsp; Saint Joseph College<br>
            &nbsp;&nbsp;&nbsp; 2013-2017
        </div>
        
        <div>
            <h3>Senior High School:</h3>
            &nbsp;&nbsp;&nbsp; Saint Joseph College<br>
            &nbsp;&nbsp;&nbsp; 2017-2019
        </div>
        
        <div>
            <h3>College:</h3>
            &nbsp;&nbsp;&nbsp; CIT - University<br>
            &nbsp;&nbsp;&nbsp; Bachelor of Science in Information Technology<br>
            &nbsp;&nbsp;&nbsp; 2020 - Present<br>
        </div>
        """,
        unsafe_allow_html=True
    )


elif section == "Hobbies":
    st.subheader("Hobbies")
    st.bar_chart(df.set_index('Hobby'))

elif section == "Aspirations":
    st.subheader("Aspirations")
    st.write("1. To become a successful IT GUY")
    st.write("2. To help my family in any way shape or form")
    st.write("3. To become stable financially and mentally and to have enough to even give back to my community")

elif section == "Life Motto":
    st.subheader("Life Motto")
    st.markdown(
            f"""
            <div style="display: flex; flex-direction: column; align-items: center;">
                <img src="{motto_img_url}" width="500">
            </div>
            """,
            unsafe_allow_html=True
                )
    # st.image("https://github.com/jessrey619/streamlit_autobiography_files/blob/main/motto_gif.gif?raw=true", width=500)
    # st.write("Give what you can and live as you want because the only person who's approval you need is yours")
