import streamlit as st
import base64
import os

st.title("House of the Dragon Fanpage")

IMAGE_FOLDER = "data"

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
}

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
}

def show_gif(filename, max_width="100%"):
    path = os.path.join(IMAGE_FOLDER, filename)
    with open(path, "rb") as f:
        data = f.read()
    data_url = base64.b64encode(data).decode()
    gif_html = f'<img src="data:image/gif;base64,{data_url}" alt="gif" style="max-width:{max_width};">'
    st.markdown(gif_html, unsafe_allow_html=True)

def show_character(char):
    st.header(char["Name"])
    if "Image" in char:
        if char["Name"] == "Daemon Targaryen":
            show_gif(char["Image"], max_width="60%")  # Daemon 이미지 크기 줄임
        else:
            show_gif(char["Image"])
    elif "Images" in char:
        cols = st.columns(len(char["Images"]))
        for i, img_file in enumerate(char["Images"]):
            with cols[i]:
                show_gif(img_file)

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

def show_timeline():
    st.header("Timeline")

    daemon_events = [
        ("81 AC", "Daemon Targaryen born"),
        ("Held many titles", "Prince, Commander of the City Watch, King of the Stepstones"),
        ("130 AC", "Died at Gods Eye (aged 49)")
    ]

    alicent_events = [
        ("88 AC", "Alicent Hightower born"),
        ("Unknown", "Married King Viserys I Targaryen"),
        ("133 AC", "Died in King's Landing")
    ]

    st.subheader("Daemon Targaryen Timeline")
    cols = st.columns(len(daemon_events))
    for col, (year, event) in zip(cols, daemon_events):
        with col:
            st.markdown(f"### {year}")
            st.write(event)

    st.subheader("Alicent Hightower Timeline")
    cols = st.columns(len(alicent_events))
    for col, (year, event) in zip(cols, alicent_events):
        with col:
            st.markdown(f"### {year}")
            st.write(event)

character_choice = st.sidebar.selectbox(
    "Choose a section",
    ("Daemon Targaryen", "Alicent Hightower", "Timeline")
)

if character_choice == "Daemon Targaryen":
    show_character(daemon)
elif character_choice == "Alicent Hightower":
    show_character(alicent)
else:
    show_timeline()
