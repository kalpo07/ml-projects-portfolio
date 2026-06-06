# Multimodal Hate Speech Detector

A machine learning application that detects potentially harmful language from text, audio, and video files.

This project combines text processing, speech-to-text transcription, and text classification in a single workflow. It is designed as a portfolio-ready application with a modular code structure, clean organization, and support for future enhancements.

---

## Overview

The application allows users to upload text files, recorded audio clips, or video files for analysis. Depending on the input type, the system either reads the text directly or transcribes spoken content into text. The extracted text is then preprocessed, split into chunks, and analyzed using a hate/offensive speech classification model.

The project is intended as a moderation-assistance tool and as a demonstration of how natural language processing and speech processing can be combined in a multimodal AI application.

---

## Features

- Supports text, audio, and video input files
- Reads and extracts text from supported text formats
- Transcribes speech from audio files
- Extracts audio from video files and transcribes it
- Splits long text into chunks for classification
- Performs hate/offensive speech detection on each chunk
- Displays overall and chunk-level results
- Allows JSON export of results
- Uses a modular and maintainable project structure

---

## Supported Input Types

### Text Files
- `.txt`
- `.md`
- `.csv`
- `.json`

### Audio Files
- `.wav`
- `.mp3`
- `.m4a`
- `.aac`
- `.flac`
- `.ogg`

### Video Files
- `.mp4`
- `.mov`
- `.avi`
- `.mkv`
- `.webm`

---

## Tech Stack

### Programming Language
- Python

### Application Framework
- Streamlit

### Machine Learning / NLP
- Transformers
- PyTorch

### Speech Processing
- OpenAI Whisper

### Media Processing
- MoviePy
- FFmpeg

### Data Handling
- Pandas
- NumPy

### Testing and Development
- Pytest
- Git
- GitHub

---

## How It Works

1. The user uploads a text, audio, or video file.
2. The system identifies the file type.
3. Text files are read directly.
4. Audio files are transcribed into text.
5. Video files have their audio extracted and then transcribed.
6. The resulting text is cleaned and split into chunks.
7. Each chunk is passed to a text classification model.
8. The application shows an overall moderation result and detailed chunk-level output.

---

## Project Structure

```text
multimodal-hate-speech-detector/
├── .github/
│   └── workflows/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── utils.py
│   ├── text_processing.py
│   ├── media_processing.py
│   ├── classifier.py
│   └── ui.py
├── data/
├── notebooks/
├── sample_inputs/
├── screenshots/
├── tests/
├── .gitignore
├── Dockerfile
├── README.md
├── requirements.txt
└── run.py
