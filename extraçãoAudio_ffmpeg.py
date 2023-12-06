import subprocess

def extract_audio(video_path, audio_output_path):
    command = ['ffmpeg', '-i', video_path, '-ab', '160k', '-ac', '2', '-ar', '44100', '-vn', audio_output_path]
    subprocess.run(command)
