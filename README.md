## PDF to Audiobook Converter
A .pdf files to .mp3 convertor, coded in Python. This script also have a GUI created in Tkinter for easy use. With the choice to edit the audio however the user want such as, the speed and volume of the audio, start and end pages to read as well as the choice to choose a male or female audio. Though it was a challenge to study the pyttsx3 library to use it to convert, this program helps so that I can listen to a book while also doing something else.
### How It Works
- The user will provide the .pdf file
- The user edit the settings on how they want the output to be
- .mp3 file get exported
- The user can listen to the newly exported audiobook
### Demo
https://github.com/gnat10/pdf_to_mp3_converter/assets/171052837/26930de1-9663-4498-9b9f-c4efe61338ac

### Requirements and Usage
Clone/Download this repo 
```bash
https://github.com/gnat10/pdf_to_mp3_converter.git
```
check `requirements.txt` or:
```shell
pyttsx3
PyPDF2
tkinter
```
Go to the root dir and create a virtual env with the **requirements.txt** file.
```bash
pip3 install -r requirements.txt
```
Run the script
```bash
python app.py
```
This will run the program!
