import streamlit as st
from moviepy.editor import *

def convert_video_to_audio(video_file):
    # Extract the file path from the uploaded file object
    video_path = "" + video_file.name

    # Save the uploaded video file to the specified path
    with open(video_path, "wb") as f:
        f.write(video_file.getbuffer())

    # Convert the video to audio using MoviePy
    video = VideoFileClip(video_path)
    audio = video.audio

    # Define the output audio file path
    audio_path = video_path.replace(".mp4", ".mp3")

    # Save the audio file
    audio.write_audiofile(audio_path)

    return audio_path



# Streamlit app
def main():
    st.title("Zoom Video to Audio Converter")
    
    # File uploader
    video_file = st.file_uploader("Upload Zoom video file", type=["mp4", "mov"])
    
    if video_file is not None:
        # Convert the video to audio
        audio_file = convert_video_to_audio(video_file)
        
        st.success("Conversion complete!")
        
        # Display the audio file
        st.audio(audio_file)
        

if __name__ == "__main__":
    main()
