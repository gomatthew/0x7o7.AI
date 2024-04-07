import requests

data = {
    "model": "Qwen-VL-Chat",
    "messages": [{"role": "user",
                  "content": [{"image": open(r'C:\Users\Supinfo\PycharmProjects\AITEST\test\4.机票-行程单.jpg', 'rb')},
                              {"text": "这是什么"}]}],
    # // "functions": none,
    "temperature": 0.17,
    # // "top_p": Optional[float] = None,
    # // "max_length": None,
    "stream": False
    # // "stop":  None
}

response = requests.post("http://218.77.58.142:35064/v1/chat/completions",data={'stream':False,'temperature': 0.17,'model':'Qwen-VL-Chat','messages':[{"role": "user",
                  "content": [
                              {"text": "这是什么"}]}]}, files=dict(file=open(r'C:\Users\Supinfo\PycharmProjects\AITEST\test\4.机票-行程单.jpg','rb'),fileType='png'))
print(response.text)
# res = requests.post("http://218.77.58.142:35064/v1/chat/completions",data = data)
# print(res.text)
