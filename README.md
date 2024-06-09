# Voice Assistant Ragnar

Ragnar is a voice-activated personal assistant built using Python. It recognizes voice commands to perform various tasks such as searching Wikipedia, opening websites, launching applications, and providing the current date and time.

## Features

- **Voice Commands**: Recognizes and executes spoken commands.
- **Wikipedia Search**: Provides brief summaries from Wikipedia.
- **Open Websites**: Opens popular websites like Google, YouTube, Instagram, etc.
- **Open Applications**: Launches installed applications (e.g., VS Code, Discord).
- **Date and Time**: Announces the current date and time.
- **Exit Command**: Allows the user to exit the program gracefully.

## Requirements

- Python 3.x
- pyttsx3
- SpeechRecognition
- wikipedia
- webbrowser
- pyaudio

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/voice-assistant-ragnar.git
    cd voice-assistant-ragnar
    ```

2. **Install the required packages**:
    ```bash
    pip install pyttsx3 SpeechRecognition wikipedia pyaudio
    ```

3. **Run the script**:
    ```bash
    python ragnar.py
    ```

## Usage

Run the script and give voice commands such as:
- "Search Wikipedia for Python programming language"
- "Open Google"
- "What's the date today?"
- "What's the time now?"
- "Exit"

## Customization

Customize application paths and add more commands in the `ragnar.py` script.


