import streamlit as st
import base64
import os

st.title("House of the Dragon Fanpage")

IMAGE\_FOLDER = "data"

daemon = {
"Name": "Daemon Targaryen",
"Aliases": \["Prince of the City", "Lord Flea Bottom", "The rogue prince"],
"Titles": \[
"Prince",
"Ser",
"Commander of the City Watch",
"Master of coin",
"Master of laws",
"King of the Stepstones and the Narrow Sea",
"Lord of Runestone (claimant; briefly)",
"Protector of the Realm"
],
"Allegiances": \["House Targaryen", "Blacks"],
"Culture": "Crownlands",
"Born": "81 AC",
"Died": "22nd day of the 5th moon of 130 AC (aged 49) at the Gods Eye",
"Parents": {"Father": "Baelon Targaryen", "Mother": "Alyssa Targaryen"},
"Spouses": \["Lady Rhea Royce", "Lady Laena Velaryon", "Princess Rhaenyra Targaryen"],
"Issue": \["Baela Targaryen", "Rhaena Targaryen", "Stillborn son", "Aegon III Targaryen", "Viserys II Targaryen", "Visenya Targaryen"],
"Portrayed by": "Matt Smith",
"Image": "daemon.gif",
}

alicent = {
"Name": "Alicent Hightower",
"Alias": \["The Queen in Chains"],
"Titles": \["Lady", "Queen", "Dowager Queen"],
"Allegiances": \["House Hightower", "House Targaryen", "Greens"],
"Culture": "Reach",
"Born": "88 AC",
"Died": "133 AC in King's Landing",
"Parents": {"Father": "Otto Hightower"},
"Spouse": "King Viserys I Targaryen",
"Issue": \["Aegon II Targaryen", "Helaena Targaryen", "Aemond Targaryen", "Daeron Targaryen"],
"Portrayed by": "Olivia Cooke / Emily Carey (young)",
"Images": \["alicent1.gif", "alicent2.gif"],
}

def show\_gif(filename, max\_width="100%"):
path = os.path.join(IMAGE\_FOLDER, filename)
with open(path, "rb") as f:
data = f.read()
data\_url = base64.b64encode(data).decode()
gif\_html = f'<img src="data:image/gif;base64,{data_url}" alt="gif" style="max-width:{max_width};">'
st.markdown(gif\_html, unsafe\_allow\_html=True)

def show\_character(char):
st.header(char\["Name"])
if "Image" in char:
if char\["Name"] == "Daemon Targaryen":
show\_gif(char\["Image"], max\_width="60%")  # Daemon 이미지 크기 줄임
else:
show\_gif(char\["Image"])
elif "Images" in char:
cols = st.columns(len(char\["Images"]))
for i, img\_file in enumerate(char\["Images"]):
with cols\[i]:
show\_gif(img\_file)

```
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
```

character\_choice = st.sidebar.selectbox(
"Choose a section",
("Daemon Targaryen", "Alicent Hightower", "Timeline")
)

if character\_choice == "Daemon Targaryen":
show\_character(daemon)
elif character\_choice == "Alicent Hightower":
show\_character(alicent)
else:
st.header("Timeline")
st.write("""
**Daemon Targaryen Timeline:**
\- Born in 81 AC.
\- Held titles including Prince, Commander of the City Watch, and King of the Stepstones.
\- Died at Gods Eye in 130 AC.

```
**Alicent Hightower Timeline:**
- Born in 88 AC.
- Married King Viserys I Targaryen.
- Became Queen, later Dowager Queen.
- Died in King's Landing in 133 AC.
""")
```
