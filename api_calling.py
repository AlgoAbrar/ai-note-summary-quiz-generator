from google import genai
from dotenv import load_dotenv
import os
from gtts import gTTS
import io

# Load environment variables
load_dotenv()

my_api_key = os.getenv("GEMINI_API_KEY")

# Initialize client with free model
client = genai.Client(api_key=my_api_key)

def note_generator(images):
    prompt = """
    You are an expert note-taker. Look at the provided handwritten or printed notes and create a clear, well-organized summary.

    Follow these rules:
    - Use markdown headings (##) for main topics and (###) for subtopics.
    - Use bullet points for key details.
    - Keep the total summary under 250 words.
    - Do not invent information; only summarize what's visible in the images.
    - If the images contain diagrams or equations, describe them briefly in words.

    Format your response as proper markdown.
    """

    # Build contents list: images first, then prompt
    contents = []
    for img in images:
        contents.append(img)
    contents.append(prompt)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",   # ✅ Free tier model
        contents=contents
    )
    return response.text


def audio_transcription(text):
    """
    Convert text to speech using gTTS.
    Returns an in-memory audio buffer.
    """
    #markdown characters cleaner
    clean_text = text.replace("#", "").replace("*", "").replace("`", "").replace("$", "")
    clean_text = clean_text.replace("-", " ").replace("_", " ")

    speech = gTTS(clean_text, lang='en', slow=False)
    audio_buffer = io.BytesIO()
    speech.write_to_fp(audio_buffer)
    audio_buffer.seek(0)   # Important: rewind buffer before reading
    return audio_buffer


def quiz_generator(images, difficulty):
    """
    Generate a multiple-choice quiz based on the note images.
    Difficulty can be 'Easy', 'Medium', or 'Hard'.
    """
    prompt = f"""
    You are a teacher creating a {difficulty} difficulty quiz from the notes shown in the images.

    Generate exactly 15 multiple‑choice questions. Each question must include:
    - A clear question.
    - Four answer options labeled A), B), C), D).
    - After the options, state the correct answer in the format: **Correct Answer: X**

    Use markdown to format the quiz neatly (e.g., **Question 1**, bullet points for options).
    Only base questions on content actually present in the images.
    """

    contents = []
    for img in images:
        contents.append(img)
    contents.append(prompt)

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=contents
    )
    return response.text
