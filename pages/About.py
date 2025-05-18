import streamlit as st

# Page title
st.title("House of the Dragon Fanpage")

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
    "Portrayed by": "Matt Smith"
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
    "Portrayed by": "Olivia Cooke / Emily Carey (young)"
}

# Function to display character info
def show_character(char):
    st.header(char["Name"])
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
    if isinstance(char.get("Spouses") or char.get("Spouse"), list):
        st.write(", ".join(char.get("Spouses") or char.get("Spouse")))
    else:
        st.write(char.get("Spouses") or char.get("Spouse"))
    st.subheader("Children")
    st.write(", ".join(char["Issue"]))
    st.subheader("Portrayed by")
    st.write(char["Portrayed by"])

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
