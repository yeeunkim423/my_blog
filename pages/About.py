import streamlit as st

st.title("🎧 Daelicent Fanmix")
st.caption("A soundtrack for love, ruin, and everything in between.")

songs = {
    "Lover, You Should’ve Come Over - Jeff Buckley": {
        "description": "A song full of yearning, as if sung from a distant tower where love slipped away.",
        "url": "https://youtu.be/HxfE6PJmGS8",
        "lyrics": """
So I'll wait for you, love.  
And I'll burn.  
Will I ever see your sweet return?  
Oh, will I ever learn?  
Oh-oh, lover, you should've come over.  
'Cause it's not too late.  
"""
    },
    "Undress - Sombr": {
        "description": "Haunting and raw — the ache of knowing someone might never return.",
        "url": "https://youtu.be/fOQ_-gZsnYQ",
        "lyrics": """
And I don't wanna learn another scent.  
I don't want children of another man to have the eyes of the girl I won't forget.
"""
    },
    "The 1 - Taylor Swift": {
        "description": "A soft, aching acceptance of what could’ve been.",
        "url": "https://youtu.be/KsZ6tROaVOQ",
        "lyrics": """
    And if my wishes came true, it would've been you.  
    In my defense, I have none.  
    For never leaving well enough alone.  
    But it would've been fun, if you would've been the one.  
"""
    },
    "Dark Paradise - Lana Del Rey": {
        "description": "The ghost of a love that never quite leaves—just like him in her thoughts.",
        "url": "https://youtu.be/dvSZQ4oMHGM",
        "lyrics": """
Every time I close my eyes  
It's like a dark paradise  
No one compares to you  
I'm scared that you won't be waiting on the other side  
"""
    },
    "The Night We Met - Lord Huron": {
        "description": "A return to the moment it all began... and fell apart.",
        "url": "https://youtu.be/KtlgYxa6BMU",
        "lyrics": """
I had all and then most of you  
Some and now none of you  
Take me back to the night we met  
"""
    }
}

selected_song = st.radio("Choose a song", list(songs.keys()))

st.subheader(selected_song)
st.markdown(f"*{songs[selected_song]['description']}*")
st.video(songs[selected_song]['url'])

if "lyrics" in songs[selected_song]:
    st.markdown("**Lyrics:**")
    st.markdown(songs[selected_song]["lyrics"])
