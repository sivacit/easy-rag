# YouTube Summarizer

This project allows you to download audio from a YouTube video, transcribe it using Whisper, and save the transcript to a file.

## Prerequisites

- Python 3.7 or higher
- `yt-dlp` for downloading YouTube audio
- `whisper` for transcription

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/summarizer.git
    cd summarizer
    ```

2. Create a virtual environment and activate it:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

4. Install `yt-dlp`:

    ```sh
    pip install yt-dlp
    ```

5. Install `whisper`:

    ```sh
    pip install git+https://github.com/openai/whisper.git
    ```

## Usage

1. Run the script:

    ```sh
    python src/summary/youtube.py
    ```

2. Enter the YouTube video URL when prompted.

## Project Structure

```
summarizer/
├── src/
│   └── summary/
│       └── youtube.py
├── requirements.txt
└── README.md
```

## Cleaning Up

To clean up temporary files created during the process, you can call the `cleanup` method:

```python
summarizer.cleanup()
```

## License

This project is licensed under the MIT License.