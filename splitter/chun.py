import os
import streamlit as st
from pydub import AudioSegment

# Function to split an audio file into chunks
def split_audio(audio_file, num_chunks):
    audio = AudioSegment.from_file(audio_file)
    duration = len(audio)
    chunk_duration = int(duration / num_chunks)

    audio_chunks = []
    for i in range(num_chunks):
        start_time = i * chunk_duration
        end_time = (i + 1) * chunk_duration
        chunk = audio[start_time:end_time]
        audio_chunks.append(chunk)

    return audio_chunks

# Main app
def main():
    st.title("Audio Splitter")
    audio_file = st.file_uploader("Upload an audio file", type=["mp3", "wav"])
    num_chunks = st.number_input("Number of Chunks", min_value=1, step=1, value=2)

    if audio_file is not None:
        audio = AudioSegment.from_file(audio_file)
        st.audio(audio_file, format='audio/wav')

        if st.button("Split Audio"):
            audio_chunks = split_audio(audio_file, num_chunks)
            for i, chunk in enumerate(audio_chunks):
                st.audio(chunk.export(format='wav'), format='audio/wav', start_time=0, key=f"chunk_{i}")

# Run the app
if __name__ == "__main__":
    main()
