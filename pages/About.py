import streamlit as st

def fanmix_page():
    st.title("🎧 Daelicent Fanmix")
    st.caption("A soundtrack for love, ruin, and everything in between.")

    songs = {
        "Lover, You Should’ve Come Over - Jeff Buckley": {
            "description": "A song full of yearning, as if sung from a distant tower where love slipped away.",
            "url": "https://youtu.be/HxfE6PJmGS8?si=hDiT753U7Jjsmj0V"
        },
        "Undress - Sombr": {
            "description": "Haunting and raw — the ache of knowing someone might never return.",
            "url": "https://youtu.be/fOQ_-gZsnYQ?si=vuIbLiNaLJvInesH"
        },
        "The 1 - Taylor Swift": {
            "description": "A soft, aching acceptance of what could’ve been.",
            "url": "https://youtu.be/KsZ6tROaVOQ?si=go9LzboK4SXqExIQ"
        },
        "Dark Paradise - Lana Del Rey": {
            "description": "The ghost of a love that never quite leaves—just like him in her thoughts.",
            "url": "https://youtu.be/dvSZQ4oMHGM?si=lqs_eydmSPLaampU"
        },
        "The Night We Met - Lord Huron": {
            "description": "A return to the moment it all began... and fell apart.",
            "url": "https://youtu.be/KtlgYxa6BMU?si=CknybMM_lOHocsqa"
        }
    }

    selected_song = st.radio("Choose a song", list(songs.keys()))

    st.subheader(selected_song)
    st.markdown(f"*{songs[selected_song]['description']}*")
    st.video(songs[selected_song]['url'])
