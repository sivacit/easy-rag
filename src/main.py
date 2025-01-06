import summary
from summary.openai import OpenAISummarizer
from summary.youtube import YouTubeTranscript

def main():
    print("Welcome to the YouTube Summarizer!")

    # Get YouTube URL from the user
    youtube_url = input("Enter the YouTube video URL: ")
    
    # Create an instance of YouTubeSummarizer and run the process
    summarizer = YouTubeTranscript(youtube_url)
    summarizer.run()

    # Create an instance of OpenAISummarizer and run the process
    summarizer = OpenAISummarizer("/tmp/transcript.txt", "./tmp/")
    summarizer.run()    

if __name__ == "__main__":
    main()
