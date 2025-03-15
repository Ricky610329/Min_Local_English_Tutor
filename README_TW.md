# Min Local English Tutor

這個專案是一個本地英語導師的極簡實作，旨在幫助使用者提升英語能力。  

## 使用的模型  
* **Whisper-medium**：語音轉文字模型（[Hugging Face](https://huggingface.co/openai/whisper-medium)）  
* **Gemma3 12B**：由 Ollama 執行的本地 LLM（[Ollama](https://ollama.com/library/gemma3)）（[Google Blog](https://blog.google/technology/developers/gemma-3/)）  
* **Kokoro-82M**：輕量級文字轉語音模型（[Hugging Face](https://huggingface.co/hexgrad/Kokoro-82M)）  

## 使用方式  
### `main.py`  

`main.py` 腳本可讓你與聊天機器人互動、儲存對話並載入先前的對話。  

#### 命令列參數：  
- `-l`：指定要載入的對話記錄檔案（預設：`message.json`）。  
- `-s`：指定要儲存當前對話的檔案（預設：`message.json`）。  

#### 指令範例：  
**使用自訂檔案載入與儲存對話**：  
```bash  
python main.py -l previous_conversation.json -s new_conversation.json  
```  

### `main_audio.py`  

`main_audio.py` 讓你透過語音與聊天機器人互動，並支援儲存與載入對話，以在不同會話之間保留記憶。  

#### 不啟用記憶模式的執行方式：  
```bash  
python main_audio.py  
```  

#### 啟用記憶模式：  
若要啟用記憶功能，請取消註解以下程式碼：  

```python  
# try:  
#     mesg = load_conversation(load_file)  
#     english_tutor = chatbot(mesg)  
# except FileNotFoundError:  
#     english_tutor = chatbot()  
```  

並註解掉這行：  

```python  
# english_tutor = chatbot()  
```  

這樣，機器人就能從 `-l` 指定的檔案載入先前的對話，並將更新後的對話儲存到 `-s` 指定的檔案。  

#### 指令範例：  
**使用自訂檔案載入與儲存對話**：  
```bash  
python main_audio.py -l previous_conversation.json -s new_conversation.json  
```  

#### 指令列表：  
- **`/r`**：開始錄音  
- **`/s`**：停止錄音  

#### 注意事項：  
- 預設不啟用記憶模式，因為 Whisper 模型的轉錄結果可能不夠準確，這可能會導致載入或儲存對話時出錯。  

## 依賴項  

### Ollama 伺服器  
* 請使用最新版本以確保與 Gemma3 相容（[連結](https://ollama.com/)）。  
* 下載模型（[連結](https://ollama.com/library/gemma3)）。  

```bash  
# 使用 12B 版本（我的情境）  
# 第一次執行時會花些時間下載  
# 下載完畢後，可使用 /bye 指令離開  
ollama run gemma3:12b  

# 啟動 Ollama 伺服器來託管模型  
# 每次執行 main.py 或 main_audio.py 前都要先啟動  
ollama serve  
```  

### Python 套件  
* Python 版本：3.11.10  
* 套件安裝（建議參考官方文件確認詳細安裝方式，以確保正常運行）  
```bash  
pip install pyaudio  
pip install numpy  
pip install soundfile  
pip install playsound  
pip install ollama  

# 參考 https://pytorch.org/get-started/locally/ 來安裝 GPU 或 CPU 版本  
# pip3 install torch torchvision torchaudio  

pip install transformers  # https://huggingface.co/docs/transformers/installation  
```  

## 我的硬體環境  
* **RAM**：48GB  
* **GPU**：RTX 3060  
* **VRAM**：12GB  

如果你的硬體 VRAM 或 RAM 較少，可以嘗試使用較小的模型。  

## 備註  
看到 Gemma3 的表現後，我已經等不及要測試它在這個任務上的表現了！對於 12B 的模型來說，它的表現令人驚艷。只需要簡單的指令，就能達到我想要的效果，這真的太瘋狂了！

