import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()


class OpenAISummarizer:
    def __init__(self, transcript_file, summary_folder):
        # Initialize variables
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.transcript_file = transcript_file
        self.summary_folder = summary_folder

        # Ensure OpenAI API key is set
        if not self.api_key:
            raise ValueError("OpenAI API key not found in .env file.")

        # Set up OpenAI client

        # Set up OpenAI API Key
        self.client = OpenAI(
            api_key= self.api_key
        )

        # Ensure the summary folder exists
        os.makedirs(self.summary_folder, exist_ok=True)

    def read_transcript(self):
        # Read the transcript from the file
        try:
            with open(self.transcript_file, "r") as file:
                transcript = file.read()
                return transcript
        except FileNotFoundError:
            raise FileNotFoundError(
                f"Error: The file {self.transcript_file} does not exist."
            )

    def summarize_transcript(self, transcript):
        # Summarize the transcript using OpenAI
        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {
                        "role": "user",
                        "content": f"Summarize the following transcript:\n\n {transcript}",
                    }
                ],
            )
            choices = response.choices
            chat_completion = choices[0]
            summary = (
                chat_completion.message.content
            )  # Correct (this works with the Chat Completions API)
            return summary
        except Exception as e:
            raise RuntimeError(f"Error during summarization: {e}")

    def save_summary(self, summary):
        # Save the summary to a file
        summary_file = os.path.join(self.summary_folder, "summary.txt")
        try:
            with open(summary_file, "w") as file:
                file.write(summary)
            print(f"Summary saved to {summary_file}")
        except Exception as e:
            raise RuntimeError(f"Error writing summary to file: {e}")

    def run(self):
        # Run the full process
        print("Reading transcript...")
        transcript = self.read_transcript()

        print("Summarizing transcript...")
        summary = self.summarize_transcript(transcript)

        print("Saving summary...")
        self.save_summary(summary)


# Main execution
if __name__ == "__main__":
    # Define file paths
    transcript_file = "./tmp/transcript.txt"  # Path to the transcript file
    summary_folder = "./tmp/"  # Path to the folder to save summaries

    # Create an instance of TranscriptSummarizer and run the process
    summarizer = OpenAISummarizer(transcript_file, summary_folder)
    summarizer.run()
