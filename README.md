# Wordle-Bot 

_Solves the Wordle of the day in around 4 tries. Uses `words.txt` file from https://github.com/3b1b/videos/blob/master/_2022/wordle/data/possible_words.txt_

## Download Files
Click the green `Code` button and in the dropdown click `Download ZIP`. Once downloaded, extract the files and move them somewhere safe.  

![image](https://user-images.githubusercontent.com/110541688/184663292-fe3f6e2a-7d90-4710-99b9-fbb3f085c100.png)



## Setup and Instructions
_For Windows. Mac should follow similar process_

### 1. Download Python
Follow instructions at https://www.python.org/downloads/

### 2. Install Selenium
Search `cmd` in the Windows search bar. In the command prompt enter `pip install selenium`

### 3. Download ChromeDriver for your system
Go to https://chromedriver.chromium.org/downloads. Once downloaded, extract the file named `chromedriver.exe`. Move it somewhere safe.

### 4. Set ChromeDriver path
Copy the path of `chromedriver.exe` (e.g. "C:\username\projects\chromedriver.exe"). Right click `constants.py` >>> Open with >>> Notepad. Replace the text with the path where indicated. Save `constants.py` and close.

### 5. Run the bot
Double click `main.py`.

### 6. One last step
When the Wordle website is loaded, close the popup to begin and follow any instructions in the command prompt. Have fun!
