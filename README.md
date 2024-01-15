# Wordle-Bot 

_Solves today's Wordle in around 4 tries. Uses word list from https://github.com/3b1b/videos/blob/master/_2022/wordle/data/possible_words.txt_

![Wordle Bot](https://user-images.githubusercontent.com/110541688/184686791-cf79a323-7ca0-4ff0-85e9-f50da5cbf511.gif)

## Download Files
Click the green `Code` button and in the dropdown click `Download ZIP`. Once downloaded, extract the files and move them to somewhere safe.

![image](https://user-images.githubusercontent.com/110541688/184663292-fe3f6e2a-7d90-4710-99b9-fbb3f085c100.png)

## UPDATE 01.15.2024
Selenium has recently been updated. As of the time of this update, only steps 1, 5, and 6 must be run.

## Setup and Instructions
_For Windows. Mac should follow similar process_

### 1. Download Python
Follow instructions at https://www.python.org/downloads/

### 2. Install Selenium
Search `cmd` in the Windows search bar. In the command prompt enter `pip install selenium`

### 3. Download ChromeDriver for your system
Go to https://chromedriver.chromium.org/downloads. Once downloaded, extract the file named `chromedriver.exe`. Move it to somewhere safe.

### 4. Set ChromeDriver path
Copy the path of `chromedriver.exe` (e.g. `C:\username\projects\chromedriver.exe`). Right click `constants.py` >>> Open with >>> Notepad. Replace the text with the path where indicated. Save `constants.py` and close.

### 5. Run the bot
Double click `main.py`.

### 6. One last step
When the Wordle website is loaded, close the popup on the website to begin. Follow any instructions in the command prompt. Have fun!
