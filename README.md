# ARYA - Artificially Recreating Your Assistant

Arya is a Python-based voice assistant that can recognize speech, respond to commands, search Wikipedia, open websites, play music, and send emails.

## Features

- Greets the user based on the time of the day.
- Recognizes voice commands using Google Speech Recognition.
- Searches Wikipedia and reads out summaries.
- Opens commonly used websites like YouTube, Google, and Stack Overflow.
- Plays music from a specified directory.
- Tells the current time.
- Opens applications like VS Code, Task Manager, and Brave Browser.
- Sends emails using Gmail.
- Includes fun responses for casual conversations.
- Exits the program upon request.

## Installation

### Prerequisites
Ensure you have Python installed (Python 3.x recommended).  
You also need the following Python libraries:

```sh
pip install pyttsx3 speechRecognition wikipedia
```

## Usage

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/arya-voice-assistant.git
   cd arya-voice-assistant
   ```

2. Run the script:
   ```sh
   python arya.py
   ```

3. Speak commands such as:
   - "Open Google"
   - "Play songs"
   - "What is Python in Wikipedia?"
   - "Send email to Ritesh"

## Configuration

- **Email Sending:**  
  Update the `sendEmail()` function with your Gmail credentials.  
  **Warning:** Using plain-text credentials is insecure. Consider using OAuth or environment variables instead.

- **Music Directory:**  
  Modify `music_dir` with your preferred folder containing music files.

- **Application Paths:**  
  Update the paths in `os.startfile()` to match your system.

## Notes

- **SAPI5 Voice Engine:** This is a Microsoft Speech API that allows text-to-speech (TTS) functionality.
- **Speech Recognition:** The script uses Google Speech Recognition (internet required).
- **Security:** Avoid hardcoding credentials in the script. Use environment variables or secure authentication.

## License

This project is open-source under the MIT License.

---

👨‍💻 Developed by Ritesh Doijode
