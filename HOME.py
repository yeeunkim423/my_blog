import streamlit as st

st.title("🍃 Comfort Place for Daelicent")
st.caption("This is my comfort place for Daelicent")

url = "https://github.com/yeeunkim423/my_blog/raw/main/images/alicent-daemon.jpg"
st.image(url, caption="The look of love", use_container_width=True)

st.header("Welcome to my page!")

st.caption("Daelicent playlist")

with st.expander("Lover, you should've come over - Jeff Buckey"):
    st.write("""
   So I'll wait for you, love.  
   And I'll burn.  
   Will I ever see your sweet return?  
   Oh, will I ever learn?  
   Oh-oh, lover, you should've come over.  
   'Cause it's not too late.  
    """)
    st.video("https://youtu.be/HxfE6PJmGS8?si=hDiT753U7Jjsmj0V")  

with st.expander("Undress - Sombr"):
    st.write("""
    And I don't wanna learn another scent.  
    I don't want children of another man to have the eyes of the girl I won't forget.
    """)
    st.video("https://youtu.be/fOQ_-gZsnYQ?si=vuIbLiNaLJvInesH")  
    
with st.expander("the 1 - Taylor Swift"):
    st.write("""
    And if my wishes came true, it would've been you.  
    In my defense, I have none.  
    For never leaving well enough alone.  
    But it would've been fun, if you would've been the one.
    """)
    st.video("https://youtu.be/KsZ6tROaVOQ?si=go9LzboK4SXqExIQ")  
