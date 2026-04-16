import streamlit as st
from api_calling import note_generator, audio_transcription, quiz_generator
from PIL import Image

# ---------- Page Config ----------
st.set_page_config(page_title="Note Summary & Quiz", layout="wide")
st.title("📝 Note Summary and Quiz Generator")
st.markdown("Upload up to 3 images of your notes and get a **summary**, **audio version**, and a **custom quiz**.")
st.divider()

# ---------- Sidebar Controls ----------
with st.sidebar:
    st.header("⚙️ Controls")

    # Image uploader
    images = st.file_uploader(
        "Upload your note photos",
        type=['jpg', 'jpeg', 'png'],
        accept_multiple_files=True,
        help="You can upload up to 3 images."
    )

    pil_images = []
    if images:
        if len(images) > 3:
            st.error("❌ Maximum 3 images allowed.")
        else:
            st.subheader("📷 Uploaded Images")
            cols = st.columns(len(images))
            for i, img_file in enumerate(images):
                pil_img = Image.open(img_file)
                pil_images.append(pil_img)
                with cols[i]:
                    st.image(pil_img, use_container_width=True)

    # Difficulty selector
    difficulty = st.selectbox(
        "Select quiz difficulty",
        ("Easy", "Medium", "Hard"),
        index=None,
        placeholder="Choose difficulty..."
    )

    # Action button
    generate_btn = st.button("🚀 Generate Notes & Quiz", type="primary", use_container_width=True)

# ---------- Main Area ----------
if generate_btn:
    # Validation
    if not pil_images:
        st.error("📸 Please upload at least one image.")
    elif not difficulty:
        st.error("⚡ Please select a quiz difficulty.")
    else:
        # --- Note Summary ---
        with st.container(border=True):
            st.subheader("📄 Your Notes Summary")
            with st.spinner("🤖 AI is writing your notes..."):
                try:
                    notes = note_generator(pil_images)
                    st.markdown(notes)
                    st.session_state["generated_notes"] = notes   # Save for audio
                except Exception as e:
                    st.error(f"Failed to generate notes: {e}")
                    st.stop()

        # --- Audio Transcription ---
        with st.container(border=True):
            st.subheader("🔊 Audio Version")
            with st.spinner("🎙️ Generating audio..."):
                try:
                    audio_buffer = audio_transcription(st.session_state["generated_notes"])
                    st.audio(audio_buffer, format="audio/mp3")
                except Exception as e:
                    st.error(f"Audio generation failed: {e}")

        # --- Quiz ---
        with st.container(border=True):
            st.subheader(f"❓ Quiz ({difficulty} Difficulty)")
            with st.spinner("🧠 AI is creating questions..."):
                try:
                    quiz_md = quiz_generator(pil_images, difficulty)
                    st.markdown(quiz_md)
                except Exception as e:
                    st.error(f"Quiz generation failed: {e}")

else:
    # Welcome message when nothing is generated yet
    st.info("👈 Upload your images and select a difficulty in the sidebar, then click **Generate**.")