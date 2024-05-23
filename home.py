#!/user/bin/env python

import streamlit as st

st.set_page_config(layout="wide",)

page_bg_img = f"""



<style>
@import url('https://fonts.googleapis.com/css2?family=Audiowide&display=swap');
[data-testid="stAppViewContainer"] > .main {{
background-color: #111111;
background-size: cover;
background-position: center center;
background-repeat: no-repeat;
background-attachment: local;
color: white;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
color: white;
}}
h1 {{
color: white;
}}
h2 {{
color: white;
}}
.title {{
font-size: 90px;
font-variant: all-small-caps;
font-family: "Audiowide", sans-serif;
text-shadow: 0 0 10px rgba(255, 255, 255, 0.5), 0 0 20px rgba(255, 255, 255, \
0.5), 0 0 30px rgba(255, 255, 255, 0.5);

}}
.subtitle {{
font-size: 50px;
font-variant: petite-caps;
font-family: "Audiowide", sans-serif;
text-shadow: 0 0 10px rgba(255, 255, 255, 0.5), 0 0 20px rgba(255, 255, 255,\
 0.5), 0 0 30px rgba(255, 255, 255, 0.5);

}}
a.stDownloadButton {{
  color: white !important;
  text-decoration: none;
}}
a.stDownloadButton:hover {{
  color: black !important;
}}
.img-container {{
  width: 100%;
  height: 450px;
  overflow: hidden;
}}
.img-container img {{
  width: 100%;
  height: 100%;
  object-fit: cover;
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transform: scale(1);
  -webkit-transition: all 0.3s linear;
  -moz-transition: all 0.3s linear;
  -ms-transition: all 0.3s linear;
  -o-transition: all 0.3s linear;
  transition: all 0.3s linear;
}}
.img-container:hover img {{
  transform: scale(1.1); 
}}
.mini-img-container img {{
  width: 50%;
  height: 50%;
  object-fit: cover;
  -webkit-transform: scale(1);
  -moz-transform: scale(1);
  -ms-transform: scale(1);
  -o-transform: scale(1);
  transform: scale(1);
  -webkit-transition: all 0.3s linear;
  -moz-transition: all 0.3s linear;
  -ms-transition: all 0.3s linear;
  -o-transition: all 0.3s linear;
  transition: all 0.3s linear;
}}
.mini-img-container:hover img {{
  transform: scale(1.1); 
}}
.red {{
  text-shadow: 0 0 10px rgba(255, 0, 0, 0.5),
             0 0 20px rgba(255, 0, 0, 0.5),
             0 0 30px rgba(255, 0, 0, 0.5);
  color: red;
}}
.transition {{
  -webkit-transition: all 0.3s linear;
  -moz-transition: all 0.3s linear;
  -ms-transition: all 0.3s linear;
  -o-transition: all 0.3s linear;
  transition: all 0.3s linear;
}}
article div.box-wrapper {{
  width: 100%;
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;
  padding: 20px;
}}
.flex-center {{
  display: flex;
  justify-content: center;  /* Center horizontally */
  align-items: center;  /* Center vertically */
}}
div.box-wrapper div.box {{
  width: 33%;
  height: auto;
  overflow: hidden;
  position: relative;
  display: inline-block;
}}
div.box-wrapper div.box:hover {{
  z-index: 999;
  box-shadow: 0 0 10px rgba(0,0,0,0.3);
}}
div.box img {{
  width: 100%;
  height: auto;
}}
h3 {{
color: white;
}}
.center {{
  display: flex;
  justify-content: center;
}}
.right {{
  display: flex;
  justify-content: right;
  margin: 5px;
}}
.stDownloadButton {{
  background-color: #000000;
  color: white;
  border: solid;
  border-color: #ffffff;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
  border-radius: 8px;
}}
.stDownloadButton:hover {{
  background-color: #ffffff;
}}
.justified-text {{
  text-align: justify;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

#navbar = """
#Home
#Blog
#Contact
#"""
#st.markdown(
   # f'**Digital Dystopia**<div class="right">{navbar}</div>',
  #  unsafe_allow_html=True
#)
st.divider()
st.markdown(
    f'<div class="flex-center"><div class="title">Digital</div><div class="\
    subtitle"> \
    <span class="red">When AI Goes Bad</span></div><div class="title">Dystopia\
    </div></div>',
    unsafe_allow_html=True
)

st.markdown(
    f'<div><img src="https://i.ibb.co/5YD8PsH/DALL-E-2024-05-21-14-10.png" \
     style="width:100%; height:100%; \
                   object-fit:cover;"></div>',
    unsafe_allow_html=True
)

st.markdown("<br><br>", unsafe_allow_html=True)  # Adds two line breaks

col1, col2 = st.columns(2)

with col1:
    #st.image("https://i.ibb.co/rpJJ5Fk/Pedro-Shooting-2-76.jpg")
    st.markdown(
        f'<div class="img-container"><img src="https://i.ibb.co/1qtFHH3/DALL-\
        E-2024-05-22-20-02-43-A-man-lies-in-a-small-sterile-bedroom-a-sleek-\
        black-headset-device-around.webp" style="width:90%; height:100%; \
                     object-fit:cover;"></div>',
        unsafe_allow_html=True
    )

with col2:
    st.header("The Story")
    st.subheader("Dark Anthology Series")
    content = f'<div class="justified-text"> <span style="font-weight:bold;">\
    Digital Dystopia: </span> When AI Goes Bad - Enter a world where AI promises\
    perfection in every aspect of life-from caregiving to commuting. \
    As humanity embraces these advancements, the sinister undercurrents of \
    control and manipulation emerge, leading to a dystopian reality. \
    How far will we go before realizing the cost of our dependence on AI?\
    </div>'

    st.markdown(content, unsafe_allow_html=True)

    # Offer a download button for a PDF file

    ai_child = "https://www.wattpad.com/1447674760-digital-dystopia-ep-01-\
    ai-child-ep-01-ai-child"

    dream_control = "https://www.wattpad.com/1448051786-digital-dystopia-ep-\
    04-dream-control-ep-04-dream"

    more_episodes = "https://www.wattpad.com/1448051786-digital-dystopia-ep-\
      04-dream-control-ep-04-dream"

    st.markdown("<br><br>", unsafe_allow_html=True)
    col3, col4 = st.columns(2)

    with (col3):
        st.header("Preview")
        st.subheader("AI Child")
        st.markdown(
            f'<div><div class="mini-img-container">\
            <img src="https://i.ibb.co/5YD8PsH/DALL-E-2024-05-21-14-10.png" \
            style="width:100%; height:100%; \
                               object-fit:cover;"></div></div>',
            unsafe_allow_html=True
        )
        content = """
        **Story**: parents adopt an AI child as a test run for parenting, \
        but the experiment spirals out of control as the AI develops \
        disturbing behaviors.
        """
        st.markdown(content)
        st.markdown(f"""
        <div class="center">
            <a href="{ai_child}" download="Pedro-Schreier-Crew-United-\
            Profil-626413.pdf"\
             class="stDownloadButton">
                Read Online
            </a>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("<br><br>", unsafe_allow_html=True)  # Adds two line breaks
        st.subheader("Dream Control")
        st.markdown(
            f'<div><div class="mini-img-container">\
                    <img src="https://i.ibb.co/1qtFHH3/DALL-E-2024-05-22-20-02\
                    -43-A-\
                    man-lies-in-a-small-sterile-bedroom-a-sleek-black-headset\
                    -device-\
                    around.webp" style="width:100%; height:100%; \
                                       object-fit:cover;"></div></div>',
            unsafe_allow_html=True
        )
        content = """
               **Story**: A sleep aid device uses AI to curate dreams, \
               but when users start losing the ability to distinguish dreams \
               from reality, the line between restful sleep and waking \
               nightmare blurs.
               """
        st.markdown(content)
        st.markdown(f"""
               <div class="center">
                   <a href="{dream_control}" download="Pedro-Schreier-\
                   Crew-United-Profil-626413.pdf"\
                    class="stDownloadButton">
                       Read Online
                   </a>
               </div>
               """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
# Center and style the download button
st.markdown(f"""
<div class="center">
                   <a href="{more_episodes}" download="Pedro-Schreier-\
                   Crew-United-Profil-626413.pdf"\
                    class="stDownloadButton">
                      More Episodes
                   </a>
</div>
""", unsafe_allow_html=True)

tab1, tab2 = st.tabs(["Photos", "Videos"])

with tab1:
   st.subheader("More Episodes")
   st.markdown("Made in :flag-br:")
   col1, col2, col3, col4 = st.columns(4)
   with col1:
       st.markdown(
           f'<div class="img-container"><img src="https://i.ibb.co/Y2pYRk0/\
           Orginial.png" style="width:100%; height:100%; \
           object-fit:cover;"></div>',
           unsafe_allow_html=True
       )
   with col2:
       st.markdown(
           f'<div class="img-container"><img src="https://i.ibb.co/nQ64cxM/IMG\
           -0225-2.png" style="width:100%; height:100%; \
                 object-fit:cover;"></div>',
           unsafe_allow_html=True
       )
   with col3:
       st.markdown(
           f'<div class="img-container"><img src="https://i.ibb.co/mbSGZ0Q/716\
           -CFCE6-BD73-4-E76-BCCC-27-F0-\
       FC018424.jpg" style="width:100%; height:100%; \
                        object-fit:cover;"></div>',
           unsafe_allow_html=True
       )
   with col4:
       st.markdown(
           f'<div class="img-container"><img src="https://i.ibb.co/wp2rnHj/ef9\
           0c5d9-6bec-44a6-89b4-\
       ce1aa908e9d2-3.jpg" style="width:100%; height:100%; \
                               object-fit:cover;"></div>',
           unsafe_allow_html=True
       )

with tab2:
   st.header("Videos")
   col1, col2, col3 = st.columns(3)
   with col1:
       st.video("https://youtu.be/ByHh7jh3E9E")
   with col2:
       st.video("https://youtu.be/0DhkGtY-B84")
   with col3:
       st.video("https://youtu.be/uNpIaQk6ikg")

little = """
    www.pedroschreier.de | 2024
    """
with st.expander("Contact"):
    st.write('''
        schreierpedro@gmail.com
    ''')
st.write(little)
