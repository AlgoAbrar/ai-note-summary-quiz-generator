
# Ai Note Summary & Quiz Generator

A Streamlit web app that turns your handwritten or printed notes into:
- A clean, structured summary (using Google Gemini AI)
- An audio version of the summary (text-to-speech)
- A multiple-choice quiz at your chosen difficulty level

All from just **uploading up to 3 images** of your notes!



## Features

- **AI-Powered Note Summarization**  
  Upload photos of your notes and get a well-organized markdown summary using **Gemini 1.5 Flash** (free tier).

- **Audio Transcription**  
  Listen to your notes on the go with automatically generated speech (gTTS).

- **Custom Quiz Generation**  
  Test your knowledge with a 3-question multiple-choice quiz. Choose from Easy, Medium, or Hard difficulty.

- **Multi-Image Support**  
  Combine up to 3 images into one cohesive summary and quiz.

- **Beginner-Friendly UI**  
  Clean sidebar controls, progress spinners, and clear error messages guide you through every step.

---

## Live Demo

> *Coming soon!*  
> You can run it locally in under 5 minutes – see instructions below.

---

## Technologies Used

- [Streamlit](https://streamlit.io/) – Web interface
- [Google Gemini API](https://ai.google.dev/) – AI text & vision (Gemini 1.5 Flash)
- [gTTS](https://github.com/pndurette/gTTS) – Text-to-speech conversion
- [Pillow](https://python-pillow.org/) – Image handling

---

## Prerequisites

- Python 3.8 or higher
- A [Google AI Studio API key](https://aistudio.google.com/apikey) (free tier works perfectly)

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/algoabrar/note-summary-quiz-generator.git
   cd note-summary-quiz-generator
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your API key**  
   Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```
   > 🔒 **Never commit this file to GitHub!** It's already listed in `.gitignore`.

---

## 🏃 Running the App

Once everything is installed and your `.env` file is ready, run:

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 📖 How to Use

1. **Upload Images**  
   In the sidebar, click *"Upload your note photos"* and select up to 3 images (JPG, JPEG, PNG).

2. **Choose Quiz Difficulty**  
   Select **Easy**, **Medium**, or **Hard** from the dropdown.

3. **Generate**  
   Click the **"🚀 Generate Notes & Quiz"** button.

4. **View & Interact**  
   - Read your AI-generated notes (formatted with markdown headings and bullets).  
   - Listen to the audio version.  
   - Take the quiz and check your answers against the provided correct answers.

---

## 📁 Project Structure

```
.
├── app.py                 # Streamlit frontend
├── api_calling.py         # Backend functions (Gemini, gTTS)
├── requirements.txt       # Python dependencies
├── .env                   # Your API key (ignored by git)
├── .gitignore
└── README.md
```

---

## 🔧 Troubleshooting

| Issue | Possible Solution |
|-------|-------------------|
| `ModuleNotFoundError` | Run `pip install -r requirements.txt` again. |
| API key error | Make sure your `.env` file exists and contains `GEMINI_API_KEY=...`. |
| Audio not playing | gTTS requires an internet connection for speech synthesis. |
| Images not loading | Check that the uploaded files are valid JPEG/PNG images. |

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request if you have ideas for improvements.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

## 🙏 Acknowledgements

- Google for the generous free tier of Gemini API.
- The Streamlit team for an amazing framework.
- gTTS for simple text-to-speech.

---

Happy learning! 📚✨
```

Simply copy everything above and paste it into your `README.md` file. Remember to replace `your-username` in the clone URL with your actual GitHub username, and consider adding a screenshot named `screenshot.png` to your repository if you'd like the image placeholder to work.