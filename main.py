def main():
    folder_id = 'YOUR_FOLDER_ID'
    service = authenticate_drive()
    new_videos = watch_folder(folder_id)

    for video in new_videos:
        download_video(service, video['id'], video['name'])
        audio_path = './audios/meeting_audio.wav'
        extract_audio('./videos/' + video['name'], audio_path)
        transcription = transcribe_audio(audio_path)
        summary = analyse_transcription(transcription)
        summary_folder_id = 'YOUR_SUMMARY_FOLDER_ID'
        create_google_docs(summary, summary_folder_id)
        delete_video_file(service, video['id'])
