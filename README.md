# NCAIR_Whisper


### Build 
- Installing emscripten
```
# Use WSL to use emscripten easily
sudo apt install emscripten # to install emscripten in wsl
# To Install emscripten in windows you would have to use chocolatey
choco install emscripten
```
- Build using emscripten
```
# build using Emscripten (v3.1.2)
git clone https://github.com/ggerganov/whisper.cpp
cd whisper.cpp
mkdir build-em && cd build-em
emcmake cmake ..
make -j # using make in windows may create problems .... linux env is preferred
```
- Getting out all relevant files
```
# You can make a separate folder named new_folder containing only the relevant files
  # After running the above code snippet you would get folders inside build-em
# go to build-em/bin/stream.wasm and copy all 3 files index.html , stream.js , helpers.js to new_folder
# go to build-em/bin and copy libstream.worker.js to new_folder
```
### Running the server and starting transcription
- After the build just start live server from index.html , now you can start speech to text transcription
- In case of errors follow the steps below

### Errors
1. Error in fetching the ml models
   - In this case download the ml models explicitly from the links in index.html and saving them in the new_folder ( folder containing the html and all js files )
   - Then modify the links in the html file so match the path eg :
     ```
     # In my case all files are there in 'Final_builds/02_Stream.wasm_final'
      function loadWhisper(model) {
                let urls = {
                    'tiny.en': 'http://127.0.0.1:5872/Final_builds/02_Stream.wasm_final/ggml-model-whisper-tiny.en.bin',
                    'base.en': 'http://127.0.0.1:5872/Final_builds/02_Stream.wasm_final/ggml-model-whisper-base.en.bin',

                    'tiny-en-q5_1':  'https://whisper.ggerganov.com/ggml-model-whisper-tiny.en-q5_1.bin',
                    'base-en-q5_1':  'https://whisper.ggerganov.com/ggml-model-whisper-base.en-q5_1.bin',
                };
     ```
2. Shared array buffer not defined or Module.Fs not defined
   - you can use token from this [page](https://developer.chrome.com/blog/enabling-shared-array-buffer/#origin-trial) to enable SharedArrayBuffer without requiring the page to be cross-origin isolated. However, it has an expiration date.
   - In your web page, you only need to add following tag into tag
```
<head>
    <meta http-equiv="origin-trial" content="{token}">
</head>
```
- Checkout this page for more details https://stackoverflow.com/questions/70535752/enable-sharedarraybuffer-on-localhost
