import streamlit as st

st.title("🎧 Daelicent Playlist")
st.caption("A soundtrack for Daelicent")

songs = {
    "Lover, You Should’ve Come Over - Jeff Buckley": {
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
        "url": "https://youtu.be/fOQ_-gZsnYQ",
        "lyrics": """
I don't wanna get undressed  
For a new person all over again.  
I don't wanna kiss someone else's neck  
And have to pretend it's yours instead.  
And I don't wanna learn another scent.  
I don't want children of another man to have the eyes of the girl I won't forget.
"""
    },
    "The 1 - Taylor Swift": {
        "url": "https://youtu.be/KsZ6tROaVOQ",
        "lyrics": """
And if my wishes came true, it would've been you.  
In my defense, I have none.  
For never leaving well enough alone.  
But it would've been fun, if you would've been the one.  
"""
    },
    "Mystery of Love - Sufjan Steven": {
        "url": "https://youtu.be/gVVhHjyC04k?si=snSYVoznmq9i_xbo",
        "lyrics": """
Like Hephaestion, who died  
Alexander's lover.  
Now my riverbed has dried.  
Shall I find no other?  
"""
    },
    "Ghost - Halsey": {
        "url": "https://youtu.be/-r7WTPeCh-I?si=ohEYcgPOyxEwEbCa",
        "lyrics": """
You say that you're no good for me.  
'Cause I'm always tugging at your sleeve.  
And I swear I hate you when you leave.  
I like it anyway.  
"""
    },
    "Dark Paradise - Lana Del Rey": {
        "url": "https://youtu.be/dvSZQ4oMHGM",
        "lyrics": """
And there's no remedy for memory, your face is like a melody.  
It won't leave my head.  
Your soul is haunting me and telling me that everything is fine.  
But I wish I was dead (dead, like you)  
"""
    },
    "The Night We Met - Lord Huron": {
        "url": "https://youtu.be/KtlgYxa6BMU",
        "lyrics": """
I had all and then most of you  
Some and now none of you.  
Take me back to the night we met.  
I don't know what I'm supposed to do,  
Haunted by the ghost of you.  
Oh, take me back to the night we met.
"""
    }
}

selected_song = st.radio("Choose a song", list(songs.keys()))

st.subheader(selected_song)
st.video(songs[selected_song]['url'])

if "lyrics" in songs[selected_song]:
    st.markdown("**Lyrics:**")
    st.markdown(songs[selected_song]["lyrics"])
