import streamlit as st

st.set_page_config(page_title="About Daelicent", layout="centered")

st.title("About Daelicent")
st.caption("Introducing Alicent Hightower and Daemon Targaryen from House of the Dragon")

# Alicent section
st.header("Alicent Hightower")
st.image(
    "https://upload.wikimedia.org/wikipedia/en/9/98/Alicent_Hightower_House_of_the_Dragon.jpg",
    caption="Alicent Hightower (House of the Dragon)",
    use_container_width=True,
)
st.markdown(
    """
- **Actresses:** Emily Carey (young), Olivia Cooke (adult)  
- **Role:** Daughter of Otto Hightower, wife of King Viserys I, mother to key Targaryen heirs  
- **Personality:** Ambitious, politically savvy, and emotionally complex  
- **Story significance:** Central figure in the Targaryen civil war known as the Dance of the Dragons  
"""
)

st.markdown("---")

# Daemon section
st.header("Daemon Targaryen")
st.image(
    "https://upload.wikimedia.org/wikipedia/en/4/42/Daemon_Targaryen_House_of_the_Dragon.jpg",
    caption="Daemon Targaryen (House of the Dragon)",
    use_container_width=True,
)
st.markdown(
    """
- **Actor:** Matt Smith  
- **Role:** Younger brother of King Viserys I, a Targaryen prince  
- **Personality:** Charismatic, cunning, skilled warrior, unpredictable  
- **Story significance:** Central to the succession conflict and complex family dynamics  
"""
)

st.markdown("---")

