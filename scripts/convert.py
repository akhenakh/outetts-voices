import os
import subprocess

# After generating all your WAV files
for name in ["en_us_female_speaker", "en_us_male_speaker", "fr_can_female_speaker", "fr_can_female2_speaker", "fr_can_male_speaker"]:
    wav_file = f"{name}.wav"
    mp3_file = f"{name}.mp3"
    
    # Convert WAV to MP3 using FFmpeg
    subprocess.run([
        "ffmpeg", 
        "-i", wav_file, 
        "-codec:a", "libmp3lame", 
        "-qscale:a", "2", 
        mp3_file
    ])
