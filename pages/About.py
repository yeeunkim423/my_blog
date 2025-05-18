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

character_choice = st.sidebar.selectbox(
    "Choose a section",
    ("Daemon Targaryen", "Alicent Hightower", "Timeline")
)

if character_choice == "Daemon Targaryen":
    show_character(daemon)
elif character_choice == "Alicent Hightower":
    show_character(alicent)
elif character_choice == "Timeline":
    st.header("Daemon & Alicent Timeline")

    events = [
        {"year": "81 AC", "headline": "Daemon Targaryen born", "text": "Daemon Targaryen was born in 81 AC."},
        {"year": "88 AC", "headline": "Alicent Hightower born", "text": "Alicent Hightower was born in 88 AC."},
        {"year": "97 AC", "headline": "Daemon marries Lady Rhea Royce", "text": "Daemon married Lady Rhea Royce."},
        {"year": "103-104 AC", "headline": "Daemon serves as Master of Coin and Master of Laws", "text": "Daemon briefly served as Master of Coin from 103 to 104 AC, and Master of Laws for six months after."},
        {"year": "106 AC", "headline": "Viserys and Alicent's wedding & Daemon's Stepstones campaign", "text": (
            "King Viserys I Targaryen married Alicent Hightower. "
            "Daemon allied with Corlys Velaryon to wage war for the Stepstones, "
            "leading an army with his dragon Caraxes." )},
        {"year": "108 AC", "headline": "Daemon kills Craghas Drahar", "text": "Daemon made enemies in Lys, Myr, and Tyrosh and slew Craghas Drahar."},
        {"year": "109 AC", "headline": "Daemon declares himself King of the Stepstones and Narrow Sea", "text": "After conquering most islands, Daemon proclaimed himself king."},
        {"year": "111 AC", "headline": "Daemon returns to King's Landing", "text": "Bored with ruling, Daemon returned to the capital."},
        {"year": "114 AC", "headline": "Princess Rhaenyra married", "text": "Princess Rhaenyra Targaryen got married."},
        {"year": "115 AC", "headline": "Rhea Royce dies", "text": "Daemon's wife, Rhea Royce, died from a horse fall."},
        {"year": "116 AC", "headline": "Birth of Baela and Rhaena Targaryen", "text": "Baela and Rhaena were born in Pentos."},
        {"year": "120 AC", "headline": "Daemon marries Rhaenyra Targaryen", "text": "At age 39, Daemon married his niece Rhaenyra, the Princess of Dragonstone."},
        {"year": "120 AC", "headline": "Laena Velaryon dies", "text": "Laena Velaryon, Daemon's wife, died."},
        {"year": "129 AC", "headline": "Death of King Viserys I", "text": "King Viserys I Targaryen died in his sleep on the third day of the third moon."},
        {"year": "130 AC", "headline": "Death of Daemon Targaryen", "text": "Daemon died at Gods Eye at age 49."},
        {"year": "133 AC", "headline": "Death of Alicent Hightower", "text": "Alicent died in King's Landing."},
    ]

    def year_to_int(year):
        try:
            return int(year.split()[0])
        except:
            return 0

    events.sort(key=lambda e: year_to_int(e["year"]))

    st.markdown("""
    <style>
    .timeline {
      position: relative;
      max-width: 700px;
      margin: 0 auto;
      padding-left: 30px;
      border-left: 3px solid #4a90e2;
    }
    .timeline-item {
      position: relative;
      margin-bottom: 30px;
    }
    .timeline-item::before {
      content: '';
      position: absolute;
      left: -10px;
      top: 5px;
      width: 15px;
      height: 15px;
      background-color: #4a90e2;
      border-radius: 50%;
      border: 3px solid white;
    }
    .timeline-year {
      font-weight: 700;
      color: #4a90e2;
      margin-bottom: 5px;
    }
    .timeline-headline {
      font-size: 1.2rem;
      font-weight: 600;
      margin: 0;
      color: #2c3e50;
    }
    .timeline-text {
      margin: 5px 0 0 0;
      color: #34495e;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="timeline">', unsafe_allow_html=True)

    for event in events:
        st.markdown(f'''
        <div class="timeline-item">
            <div class="timeline-year">{event['year']}</div>
            <h3 class="timeline-headline">{event['headline']}</h3>
            <p class="timeline-text">{event['text']}</p>
        </div>
        ''', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
