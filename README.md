# Min Local English Tutor

This project is a minimal implementation of a local English tutor designed to help users improve their English language skills.

## Model Used
* **Whisper-medium:** Speech to Text Model ([Hugging Face](https://huggingface.co/openai/whisper-medium))
* **Gemma3 12B:** Local LLM that runs by ollama ([Ollama](https://ollama.com/library/gemma3)) ([Google Blog](https://blog.google/technology/developers/gemma-3/))
* **Kokoro-82M:** A light weight model for text to speech ([Hugging Face](https://huggingface.co/hexgrad/Kokoro-82M))

## Usage
### `main.py`

The `main.py` script allows you to interact with the chatbot, save conversations, and load previous conversations.

#### Command-Line Arguments:
- `-l`: Specify the file to load a previous conversation from (default: `message.json`).
- `-s`: Specify the file to save the current conversation to (default: `message.json`).

#### Example Commands:
**Load and save using custom files:**
   ```bash
   python main.py -l previous_conversation.json -s new_conversation.json
   ```

### `main_audio.py`

The `main_audio.py` script allows you to interact with the chatbot using voice input and output. It supports saving and loading conversations to retain memory across sessions.

#### Run without memory:
   ```bash
   python main_audio.py
   ```

#### Enabling Memory:
To enable memory, uncomment the following lines in the script:

```python
# try:
#     mesg = load_conversation(load_file)
#     english_tutor = chatbot(mesg)
# except FileNotFoundError:
#     english_tutor = chatbot()
```

And comment out this line:

```python
# english_tutor = chatbot()
```

This allows the chatbot to load previous conversations from the file specified with the `-l` argument and save the updated conversation to the file specified with the `-s` argument.

#### Example Commands:
**Load and save using custom files:**
   ```bash
   python main_audio.py -l previous_conversation.json -s new_conversation.json
   ```

#### Commands:
- **`/r`**: Start recording your voice.
- **`/s`**: Stop recording.

#### Notes:
- Memory is disabled by default because the Whisper model may not always transcribe speech accurately, which could lead to issues when loading or saving conversations.

## Dependency

### Ollama Server:
* Use latest version to be compatible with Gemma3. [LINK](https://ollama.com/)

* Download the model [LINK](https://ollama.com/library/gemma3)

```bash
# using 12B in my case
# it takes some time when run the first time 
# only needed to run when download the model
# use /bye to exit when it is done
ollama run gemma3:12b

# use ollama server to host the model
# always run it before main.py or main_audio.py
ollama serve
```

### Python Library
* python version: 3.11.10
* library (see the attach links and check installation details is the best way to make sure it works properly)
```bash
pip install pyaudio
pip install numpy
pip install soundfile
pip install playsound
pip install ollama

# reference https://pytorch.org/get-started/locally/ for GPU or CPU
# pip3 install torch torchvision torchaudio

pip install transformers #https://huggingface.co/docs/transformers/installation
```

## My Hardware:
* RAM: 48GB
* GPU: RTX3060
* VRAM: 12GB

* try smaller model if your hardware has less VRAM or RAM 

## Remark
Upon seeing Gemma3's performance, I just can't wait to see how it performs on this task. For a 12B model, it does remarkably well on what I want with a simple instruction. It's crazy!!