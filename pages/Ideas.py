import streamlit as st

st.set_page_config(page_title="Daelicent Fic Ideas", layout="centered")

st.title("🖋️ Daelicent Fic Notes & Ideas")
st.caption("Organize your fic universe and keep your imagination flowing.")

# 탭 생성
tab1, tab2 = st.tabs(["📓 Fic Notebook", "💡 Fic Prompts"])

# 📓 메모장 탭
with tab1:
    st.subheader("📓 Your Fic Notebook")

    # 세션 초기화
    if "fic_notes" not in st.session_state:
        st.session_state.fic_notes = []

    if "selected_prompts" not in st.session_state:
        st.session_state.selected_prompts = []

    # 폼으로 새 노트 추가
    with st.form("fic_form", clear_on_submit=True):
        new_note = st.text_area("💭 Add a new idea or scene:", height=100)
        submitted = st.form_submit_button("➕ Add")

        if submitted and new_note.strip():
            st.session_state.fic_notes.append(new_note.strip())
            st.success("Note added!")

    # 저장된 노트 보여주기
    st.markdown("---")
    if st.session_state.fic_notes:
        for i, note in enumerate(reversed(st.session_state.fic_notes), 1):
            st.markdown(f"**{len(st.session_state.fic_notes) - i + 1}.** {note}")
            if st.button("📤 Send to Prompts", key=f"send_{i}"):
                st.session_state.selected_prompts.append(note)
                st.success("Note sent to prompts!")
    else:
        st.info("No notes yet. Start writing!")

    # 초기화 옵션
    with st.expander("⚙️ Clear all notes"):
        if st.button("🗑️ Delete All"):
            st.session_state.fic_notes = []
            st.success("Notebook cleared.")

# 💡 아이디어 정리 탭
with tab2:
    st.subheader("💡 Fic Prompt Ideas")

    st.markdown("""
    - 👑 *Daemon as a single father AU with Alicent as the teacher at Milo’s daycare.*
    - 🕊️ *Enemies-to-lovers CEO AU where Alicent is a PR manager hired to fix Daemon’s image.*
    - 🩸 *A post-canon fic where Alicent is the last person alive who remembers who Daemon truly was.*
    - ✨ *Modern social media AU: Daemon’s ex comments on Alicent’s photo.*
    - 🎭 *Reincarnation AU: Alicent meets Daemon in every life but always forgets him at the end.*
    """)

    # Show selected prompts
    if st.session_state.selected_prompts:
        st.markdown("---")
        st.subheader("Your Selected Prompts")
        for prompt in st.session_state.selected_prompts:
            st.markdown(f"- {prompt}")
    else:
        st.info("No selected prompts yet. Use the button to send notes here.")
