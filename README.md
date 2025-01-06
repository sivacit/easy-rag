# YouTube Summarizer

This project allows you to download audio from a YouTube video, transcribe it using Whisper, and save the transcript to a file.

## Executive Summary

The YouTube Summarizer is a tool designed to simplify the process of extracting and transcribing audio from YouTube videos. By leveraging `yt-dlp` for downloading audio and OpenAI's `whisper` for transcription, this project provides a seamless way to convert spoken content into text. This can be particularly useful for creating subtitles, generating notes, or simply archiving spoken content in a textual format.

## Prerequisites

- Python 3.7 or higher
- uv package manager

Install `uv` with our standalone installers:

#### On macOS and Linux
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### On Windows
```sh
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Or, from PyPI:

#### With pip
```sh
pip install uv
```

#### Or pipx
```sh
pipx install uv
```

If installed via the standalone installer, `uv` can update itself to the latest version:
```sh
uv self update
```

See the installation documentation for details and alternative installation methods.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/sivacit/yt-summarizer.git
    cd yt-summarizer
    ```

2. Once you install `uv` and clone the repo, go to the project home directory `yt-summarizer`, and run the command:

    ```sh
    uv install
    ```
    This will create a virtual environment and install the required packages.

## Generating OpenAI API Key

To use OpenAI's services, you need to generate an API key. Follow these steps:

1. Go to the OpenAI website: [OpenAI](https://www.openai.com/)
2. Sign up for an account or log in if you already have one.
3. Navigate to the API section of the website.
4. Click on the "Create API Key" button.
5. Copy the generated API key and add it to your `.env` file:

    ```
    OPENAI_API_KEY=your_api_key_here
    ```

## Usage

1. Run the script:

    ```sh
    uv src/main.py
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