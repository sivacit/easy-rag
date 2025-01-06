import subprocess
import whisper

class YouTubeTranscript:
    def __init__(self, youtube_url, audio_file="/tmp/audio.mp3", transcript_file="/tmp/transcript.txt"):
        self.youtube_url = youtube_url
        self.audio_file = audio_file
        self.transcript_file = transcript_file

    def download_audio(self):
        """
        Downloads audio from the YouTube video using yt-dlp.
        """
        try:
            command = [
                "yt-dlp", "--extract-audio", "--audio-format", "mp3",
                "-o", self.audio_file, self.youtube_url
            ]
            subprocess.run(command, check=True)
            print(f"Audio downloaded successfully as {self.audio_file}")
        except subprocess.CalledProcessError as e:
            print(f"Error downloading audio: {e}")
            exit()

    def transcribe_audio(self):
        """
        Transcribes the downloaded audio using Whisper.
        """
        try:
            model = whisper.load_model("base")  # You can replace "base" with "tiny", "small", etc.
            result = model.transcribe(self.audio_file)
            return result["text"]
        except Exception as e:
            print(f"Error during transcription: {e}")
            exit()

    def save_transcript(self, transcript):
        """
        Saves the transcribed text to a file.
        """
        try:
            with open(self.transcript_file, "w") as f:
                f.write(transcript)
            print(f"Transcript saved to {self.transcript_file}")
        except Exception as e:
            print(f"Error saving transcript: {e}")
            exit()

    def run(self):
        """
        Executes the full process: download, transcribe, and save the transcript.
        """
        print("Downloading audio...")
        self.download_audio()

        print("Transcribing audio...")
        transcript = self.transcribe_audio()

        print("Saving transcript...")
        self.save_transcript(transcript)

    def cleanup(self):
        """
        Cleans up temporary files.
        """
        try:
            subprocess.run(["rm", self.audio_file])
            subprocess.run(["rm", self.transcript_file])
            print("Temporary files cleaned up.")
        except Exception as e:
            print(f"Error cleaning up temporary files: {e}")
            exit()        


# Main execution
if __name__ == "__main__":
    print("Welcome to the YouTube Summarizer!")

    # Get YouTube URL from the user
    youtube_url = input("Enter the YouTube video URL: ")

    # Create an instance of YouTubeTranscript and run the process
    summarizer = YouTubeTranscript(youtube_url)
    summarizer.run()
