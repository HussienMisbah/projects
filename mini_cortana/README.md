## Description :

- it works only on windows platform , tested on win 10 
- take voice from user as input and perform actions
- using a prefix before the desired action to maintain accuracy
- functions :

=> Open applications installed on windows

=> Open and read files from system  “text to speech”

=> Open any website user asks for

=> Open any partition on the PC

=> Open camera , music player , ..  

and other functions can be found on the usage guide below


## installation guide :

[+] first in your cmd type ``python --version`` and depending on output download suitable wheel for Pyaudio 
    link: https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

ex : PyAudio‑0.2.11‑cp39‑cp39‑win_amd64.whl is for python 3.9 and win x64 

[+] download this project link :

https://downgit.github.io/#/home?url=https://github.com/HussienMisbah/projects/tree/master/mini_cortana

[+] install requirements by :

```
pip install -r requirements.txt
```
you may face error at Pyaudio part so after it use 

```
pip install "wheel name you downloaded"
```

now all should be good try use it :

```
python script.py
```

## Usage Guide  :

```
         [+] quit : exits the program  
         [+] reset: clean the screen "cmd"   
         [+] camera : opens camera
         [+] partition followed by partition letter ex: partition c
         [+] open followed by application name ex : open firefox 
         [+] read followed by .txt file ex : read test  
         [+] website followed by website name ex : website facebook  
         [+] music : opens spotify " should be installed to run it " 
         default path for program is C
```


