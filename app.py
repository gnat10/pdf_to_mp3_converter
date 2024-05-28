import pyttsx3
import PyPDF2
from tkinter import *
from tkinter import ttk, filedialog, messagebox


def importpdf():
    global pdf_file
    pdf_file = filedialog.askopenfilename(filetypes=[("PDF Document", "*.pdf")])


def getpages():
    importpdf()
    pdfname = pdf_file.split('/')[-1]
    pdfname_label.config(text=pdfname)
    pdf = PyPDF2.PdfReader(pdf_file)
    totalpages = len(pdf.pages)
    number_of_pages = []
    for page in range(1, totalpages + 1):
        number_of_pages.append(page)
    startpage_combobox['values'] = number_of_pages
    endpage_combobox['values'] = number_of_pages


def gettext():
    startpage = (int(startpage_combobox.get())-1)
    endpage = (int(endpage_combobox.get()))
    book = ""
    pdf = PyPDF2.PdfReader(pdf_file)
    for num in range(startpage, endpage):
        read_pages = pdf.pages[num]
        book += read_pages.extract_text()
    return book


audiobook = pyttsx3.init()


def getspeed():
    speed = speed_spinbox.get()
    audiobook.setProperty('rate', int(speed))


def getvolume():
    volume_before = int(volume_spinbox.get())
    volume_after = volume_before/100
    audiobook.setProperty('volume', float(volume_after))


def getvoice():
    selected_voice = audio_voice.get()
    voices = audiobook.getProperty('voices')
    audiobook.setProperty('voice', voices[selected_voice].id)


def saveaudiobook():
    output = gettext()
    getspeed()
    getvolume()
    getvoice()
    audiobook_name = pdfname_label.cget('text')[0:-4]
    types = [("MP3 Files", "*.mp3")]
    output_name = filedialog.asksaveasfilename(title="Save As", filetypes=types, initialfile=audiobook_name)
    audiobook.save_to_file(output, f"{output_name}.mp3")
    audiobook.runAndWait()
    messagebox.showinfo('Success', 'Audiobook has been exported.')


pdf_file = ""


# GUI

root = Tk()

root.title("PDF to Audio Converter")
root.config(padx=20, pady=20)

frame = Frame(root)
frame.pack()

# frame1
page_title_frame = LabelFrame(frame)
page_title_frame.grid(row=0, column=0, padx=0, pady=10)
title = Label(frame, text="PDF to Audiobook Convertor", font=("Helvetica", 20))
title.grid(row=0, column=0, sticky="news", padx=20, pady=20)

# frame2
pdf_info_frame = LabelFrame(frame)
pdf_info_frame.grid(row=1, column=0, sticky="news", padx=0, pady=10)
pdfname_label = Label(pdf_info_frame, text="Please Import PDF")
pdfname_label.grid(row=0, column=1, padx=20, pady=20)
importButton = Button(pdf_info_frame, text="Import PDF", command=getpages)
importButton.grid(row=0, column=0, padx=20, pady=20)

# frame3
page_details_frame = LabelFrame(frame, text="Audiobook Settings")
page_details_frame.grid(row=2, column=0, padx=0, pady=10)

# frame3.1
pdf_pages_frame = LabelFrame(page_details_frame)
pdf_pages_frame.grid(row=0, column=0, sticky="news", padx=25, pady=10)


def end_page_limit(event):
    new_values = ()
    for i in startpage_combobox["values"]:
        if i >= startpage_combobox.get():
            new_values = new_values + tuple(i)
    endpage_combobox["values"] = new_values


start_page = Label(pdf_pages_frame, text="Start Page")
start_page.grid(row=0, column=0)
startpage_combobox = ttk.Combobox(pdf_pages_frame, textvariable="", state='readonly')
startpage_combobox.grid(row=1, column=0)
startpage_combobox.bind("<<ComboboxSelected>>", end_page_limit)

end_page = Label(pdf_pages_frame, text="End Page")
end_page.grid(row=2, column=0)
endpage_combobox = ttk.Combobox(pdf_pages_frame, textvariable="", state='readonly')
endpage_combobox.grid(row=3, column=0)


# frame3.2
audiobook_settings_frame = LabelFrame(page_details_frame)
audiobook_settings_frame.grid(row=0, column=1, sticky="news", padx=25, pady=10)
speed_label = Label(audiobook_settings_frame, text="Speed")
speed_label.grid(row=0, column=0)
speedvar = DoubleVar(value=200)
speed_spinbox = Spinbox(audiobook_settings_frame, from_=50, to=300, textvariable=speedvar)
speed_spinbox.grid(row=1, column=0)
volume_label = Label(audiobook_settings_frame, text="Volumes")
volume_label.grid(row=2, column=0)
volumevar = DoubleVar(value=100)
volume_spinbox = Spinbox(audiobook_settings_frame, from_=25, to=100, textvariable=volumevar)
volume_spinbox.grid(row=3, column=0)

# frame 4
voices_label_frame = LabelFrame(frame, text="Voice Preferences")
voices_label_frame.grid(row=3, column=0, sticky="news")
audio_voice = IntVar()
male_voice_radio = Radiobutton(voices_label_frame, text="Male", variable=audio_voice, value=0)
male_voice_radio.grid(row=0, column=1, sticky="news")
female_voice_radio = Radiobutton(voices_label_frame, text="Female", variable=audio_voice, value=1)
female_voice_radio.grid(row=0, column=2, sticky="news")

# frame 5
saveButton = Button(frame, text="Save mp3", command=saveaudiobook)
saveButton.grid(row=4, column=0, sticky="news", padx=0, pady=10)

root.mainloop()
