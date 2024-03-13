# -*- coding: utf-8 -*-
# 导入Pytube库
import pytube

#加载YouTube链接
video = "https://www.youtube.com/watch?v=x7X9w_GIm1s"

# 转换和下载为MP4文件
data = pytube.YouTube(video)
audio = data.streams.get_audio_only()
audio.download()

from langchain_community.document_loaders.parsers.audio import OpenAIWhisperParser
import whisper
model = whisper.load_model("tiny",download_root=r'D:\deep_learning_model\openai')
result = model.transcribe("audio.mp3")
print(result)