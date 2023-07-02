from aip import AipSpeech
import speech_recognition as sr

APP_ID = "35604450"
API_KET = "PqpBNvXfHZH2PZARr5P7zdrK"
SECRET_KEY = "tARVBQcHviHwZe3C1OyU5K5dZZ3wBIaY"

client = AipSpeech(APP_ID, API_KET, SECRET_KEY)
r = sr.Recognizer()

def _record(if_cmu:bool = False, rate=16000):
    with sr.Microphone(sample_rate=rate) as source:
        # 校准噪声
        r.adjust_for_ambient_noise(source, duration=1)
        print("You can speak now~")
        audio = r.listen(source, timeout=20, phrase_time_limit=2)

    file_name = "./speech.wav"
    with open(file_name, "wb") as f:
        f.write(audio.get_wav_data())

    if if_cmu:
        return audio
    else:
        return _get_file_content(file_name)

# 从本地文件中加载音频 作为后续百度语音服务的输入
def _get_file_content(file_name):
    with open(file_name, 'rb') as f:
        audio_data = f.read()
    return audio_data

def speech_to_text(audio_path: str = "test.wav", if_microphone: bool = True):
    # 麦克风输入 采样频率必须为8的倍数 我们使用16000和上面保持一致
    if if_microphone:
        result = client.asr(_record(), 'wav', 16000, {
            'dev_pid': 1737  # 识别英文
        })
    # 从文件中读取
    else:
        result = client.asr(_get_file_content(audio_path), 'wav', 16000, {
            'dev_pid': 1737  # 识别英文
        })
    if result["err_msg"] != "success.":
        return "语音识别失败：" + result["err_msg"]
    else:
        return result['result'][0]
 
result = speech_to_text()
print(result)


    
    
