import wave

# Specify the path to your .wav file
wav_file_path = "FindMe.wav"

# Open the .wav file for reading
with wave.open(wav_file_path, 'rb') as wav_file:
    # Get the audio file's parameters
    sample_width = wav_file.getsampwidth()
    frame_rate = wav_file.getframerate()
    num_channels = wav_file.getnchannels()
    num_frames = wav_file.getnframes()

    # Read audio data from the file
    audio_data = wav_file.readframes(num_frames)
    print(audio_data)
# Now, you have the audio data in the 'audio_data' variable as a binary string
# You can further process or play the audio data as needed

