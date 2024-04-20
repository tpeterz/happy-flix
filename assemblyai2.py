# pip install assemblyai

import assemblyai as aai

aai.settings.api_key = "24e1a5e53b1e2d7c046ea031947ce1f4"

audio_url = "https://storage.googleapis.com/aai-web-samples/news.mp4"

transcriber = aai.Transcriber()
transcript = transcriber.transcribe(audio_url)
print(transcript.text)

# # transcript = transcriber.transcribe("./my-local-audio-file.wav")




# import assemblyai

# assemblyai.api_key = "749e003ea85a41cdaf81280177420e92"
# transcriber = assemblyai.Transcriber()

# transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# # transcript = transcriber.transcribe("./my-local-audio-file.wav")

# print(transcript.text)


# from assemblyai import Transcriber

# transcriber = Transcriber(api_key="749e003ea85a41cdaf81280177420e92")

# transcript = transcriber.transcribe("https://storage.googleapis.com/aai-web-samples/news.mp4")
# # transcript = transcriber.transcribe("./my-local-audio-file.wav")

# print(transcript.text)
