import pytube
import whisper

youtubeUrl = "https://www.youtube.com/watch?v=yhpo_IHP86A"
youtubeVideo = pytube.Youtube(youtubrUrl)

audio = youtubeVideo.streams.get_audio_only()
audio.download(filename='tmp.mp4')

model = whisper-load_model("small")
result = model.transcribe('tmp.mp4')

print(result["text"])
