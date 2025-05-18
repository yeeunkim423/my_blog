import streamlit as st
from PIL import Image
import os

# Page title
st.title("House of the Dragon Fanpage")

# Image folder path
IMAGE_FOLDER = "data"

# Daemon Targaryen data
daemon = {
    "Name": "Daemon Targaryen",
    "Aliases": ["Prince of the City", "Lord Flea Bottom", "The rogue prince"],
    "Titles": [
        "Prince",
        "Ser",
        "Commander of the City Watch",
        "Master of coin",
        "Master of laws",
        "King of the Stepstones and the Narrow Sea",
        "Lord of Runestone (claimant; briefly)",
        "Protector of the Realm"
    ],
    "Allegiances": ["House Targaryen", "Blacks"],
    "Culture": "Crownlands",
    "Born": "81 AC",
    "Died": "22nd day of the 5th moon of 130 AC (aged 49) at the Gods Eye",
    "Parents": {"Father": "Baelon Targaryen", "Mother": "Alyssa Targaryen"},
    "Spouses": ["Lady Rhea Royce", "Lady Laena Velaryon", "Princess Rhaenyra Targaryen"],
    "Issue": ["Baela Targaryen", "Rhaena Targaryen", "Stillborn son", "Aegon III Targaryen", "Viserys II Targaryen", "Visenya Targaryen"],
    "Portrayed by": "Matt Smith",
    "Image": "daemon.gif",
    "Timeline": [
        "81 AC: Born to Baelon and Alyssa Targaryen",
        "Served as Commander of the City Watch",
        "Claimed Lordship of Runestone briefly",
        "Married three times: Lady Rhea Royce, Lady Laena Velaryon, Princess Rhaenyra Targaryen",
        "Became King of the Stepstones and the Narrow Sea",
        "130 AC: Died at the Gods Eye"
    ]
}

# Alicent Hightower data
alicent = {
    "Name": "Alicent Hightower",
    "Alias": ["The Queen in Chains"],
    "Titles": ["Lady", "Queen", "Dowager Queen"],
    "Allegiances": ["House Hightower", "House Targaryen", "Greens"],
    "Culture": "Reach",
    "Born": "88 AC",
    "Died": "133 AC in King's Landing",
    "Parents": {"Father": "Otto Hightower"},
    "Spouse": "King Viserys I Targaryen",
    "Issue": ["Aegon II Targaryen", "Helaena Targaryen", "Aemond Targaryen", "Daeron Targaryen"],
    "Portrayed by": "Olivia Cooke / Emily Carey (young)",
    "Images": ["alicent1.gif", "alicent2.gif"],
    "Timeline": [
        "88 AC: Born to Otto Hightower",
        "Married King Viserys I Targaryen",
        "Mother of four: Aegon II, Helaena, Aemond, Daeron",
        "Played a key role in the Greens faction during the Targaryen civil war",
        "133 AC: Died in King's Landing"
    ]
}

def load_image(filename):
    path = os.path.join(IMAGE_FOLDER, filename)
    try:
        img = Image.open(path)
        return img
    except Exception as e:
        st.error(f"Error loading image: {filename}")
        return None

# Function to display character info with images and timeline
def show_character(char):
    st.header(char["Name"])
    # Show images
    if "Image" in char:
        img = load_image(char["Image"])
        if img:
            st.image(img, use_column_width=True)
    elif "Images" in char:
        cols = st.columns(len(char["Images"]))
        for i, img_file in enumerate(char["Images"]):
            img = load_image(img_file)
            if img:
                cols[i].image(img, use_column_width=True)
    # Text info
    st.subheader("Aliases")
    st.write(", ".join(char.get("Aliases", char.get("Alias", []))))
    st.subheader("Titles")
    for title in char["Titles"]:
        st.write("- " + title)
    st.subheader("Allegiances and Culture")
    st.write(", ".join(char["Allegiances"]) + f" (Culture: {char['Culture']})")
    st.subheader("Born and Died")
    st.write(f"Born: {char['Born']}")
    st.write(f"Died: {char['Died']}")
    st.subheader("Parents")
    for relation, name in char["Parents"].items():
        st.write(f"{relation}: {name}")
    st.subheader("Spouse(s)")
    spouses = char.get("Spouses") or char.get("Spouse")
    if isinstance(spouses, list):
        st.write(", ".join(spouses))
    else:
        st.write(spouses)
    st.subheader("Children")
    st.write(", ".join(char["Issue"]))
    st.subheader("Portrayed by")
    st.write(char["Portrayed by"])
    
    # Timeline section
    st.subheader("Timeline")
    for event in char.get("Timeline", []):
        st.write(f"- {event}")

# Sidebar for character selection
character_choice = st.sidebar.selectbox(
    "Choose a character",
    ("Daemon Targaryen", "Alicent Hightower")
)

# Display selected character info
if character_choice == "Daemon Targaryen":
    show_character(daemon)
else:
    show_character(alicent)
