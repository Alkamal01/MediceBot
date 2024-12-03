# MediceBot - AI-Powered Healthcare Diagnosis and Treatment Recommendations

MediceBot is a healthcare solution designed to empower doctors and healthcare professionals by using AI for accurate medical diagnosis and treatment recommendations. The platform takes input from users regarding symptoms, medical history, and basic demographic information, processes the data using Google's generative AI models, and provides preliminary diagnoses and recommended treatment plans. Additionally, the application supports multi-language translation and generates downloadable DOCX files with the diagnosis and treatment details.

## Features

- **Multi-Language Support**: The app provides translation options in English, Hausa, Yoruba, Igbo, Spanish, and French for a wider reach.
- **AI-Powered Diagnosis and Treatment**: Uses Google's Gemini AI model to analyze symptoms and medical history to generate a diagnosis and treatment plan.
- **Text-to-Speech Conversion**: Converts diagnosis and treatment text to speech for improved accessibility.
- **Downloadable DOCX File**: Generates a DOCX file with the diagnosis and treatment plan, which users can download.
- **Customizable User Input**: Allows users to specify gender, age, symptoms, and medical history through an interactive sidebar.

## Requirements

- Python 3.7+
- Streamlit
- Google Generative AI SDK (`google-generativeai`)
- Langchain
- Google Cloud Translation API (`googletrans`)
- Python-docx
- Dotenv for managing environment variables
- pyttsx3 or Google TTS API for Text-to-Speech functionality (if implementing voice output)

## Installation

1. Clone the repository or download the files.

   ```bash
   git clone https://github.com/yourusername/medicebot.git
   cd medicebot

2. Install the necessary dependencies.

   ```bash
   pip install -r requirements.txt

3. Set up environment variables. Create a .env file in the root directory and add your Google API key:

    ```bash
    GOOGLE_API_KEY=your-google-api-key

4. Run the app:

    ```bash
    streamlit run app.py

## Usage

1. Open the app in your browser at the address provided by Streamlit (usually http://localhost:8501).
From the sidebar, select the user’s gender, age, symptoms, and medical history.
2. Choose the language for the output.
3. Click on the "Get Diagnosis and Treatment Plan" button.
5. The AI will process the data and display the diagnosis and treatment plan.
6. The diagnosis and treatment plan will be available in both text form on the screen and as a downloadable DOCX file.
7. The app will also convert the text into speech if the text-to-speech feature is implemented.

## Code Breakdown

# User Inputs:

- Users input their gender, age, symptoms, and medical history through the sidebar interface.
- Inputs are translated into English using the Google Translate API.

# AI Processing:

- The app uses Google's Gemini model for generating diagnosis and treatment plans. The data is formatted into prompts using the PromptTemplate class from Langchain.

# Translation:

- The diagnosis and treatment plan are translated into the selected language and displayed on the screen.

# DOCX Generation:

- A DOCX file is created using python-docx and allows users to download the report.

# Text-to-Speech:

- The text-based diagnosis and treatment plan can be converted into speech using a TTS library (either pyttsx3 or Google TTS API).

# Folder Structure
``` bash
    medicebot/
    │
    ├── app.py               # Main application file
    ├── requirements.txt     # Python dependencies
    ├── .env                 # Environment variables (Google API key)
    └── assets/
        └── medicebot.webp   # Image for the sidebar
```

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Contributing
Feel free to fork the repository, make improvements, and create pull requests. Contributions are welcome!





