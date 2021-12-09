from tkinter import*
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from gtts import gTTS
from tkinter.font import Font
from pygame import mixer
import speech_recognition as sr
from io import BytesIO
import os


mixer.init()

#luodaan funktio, joka kutsuu valintaikkuna valinnan perusteella toista
#funktiota. Jos slow speech valinta on valittu, kutsutaan slowSpeech funktiota
#jne.
def selectFunc():
    if Slow.get() == 1:
        slowSpeech()
        
    if fast.get() == 1:
        fastSpeech()

#luodaan funktio, jolla toteutetaan tekstistä puheeksi toiminta hidastetulla
#äänellä. Hidas puhe valitaan antamalla slow parametrin arvoksi True.
#savefile muuttujaan tallennetaan käyttäjän syöttämä tiedoston nimi ja
#mytext muuttujaan käyttäjän syöttämä teksti, joka halutaan muuttaa puheeksi.
#mytext muuttujaan annetaan text parametrin arvoksi.
#language muuttujaan tallennetaan käyttäjän syöttämä kielikoodi ja annetaan
#se lang parametrin arvoksi.
        
def slowSpeech():
    filetype = [('MP-3','*.mp3')]
    savefile = filedialog.asksaveasfilename(filetypes = filetype, defaultextension = filetype)
    mytext = (Entry.get(enterText))
    language = (Entry.get(setLang))
    myobj = gTTS(text = mytext, lang = language, slow=True)
    myobj.save(savefile)

#luodaan funktio, jolla toetutetaan normaali nopeuksinen puheääni. nopeus muutetaan normaaliksi
#antamalla slow parametrin arvoksi False.
def fastSpeech():
    filetype = [('MP-3','*.mp3')]
    savefile = filedialog.asksaveasfilename(filetypes = filetype, defaultextension = filetype)
    mytext = (Entry.get(enterText))
    language = (Entry.get(setLang))
    myobj = gTTS(text = mytext, lang = language, slow=False)
    myobj.save(savefile)

    
#luodaan funktio, jolla avataan tallennettu äänitiedosto ja toistetaan valittu
#tiedosto.
def playSpeech():
    loadfile = filedialog.askopenfilename()
    mixer.music.load(loadfile)
    mixer.music.play()

#luodaan funktio, jolla äänitiedoston toistaminen keskeytetään.
def stopSpeech():
    mixer.music.stop()
    
#luodaan funktio, joka näyttää ohjekekstin kysymysmerkkipainiketta painettaessa.
def showInfo():
    messagebox.showinfo('?','Showing as language codes, en = english, fi = finnish etc.')

#luodaan funktio, jolla toteutetaan puheen tunnistus.
def recognise():

    lang = (Entry.get(setVoiceLang))
    rec = sr.Recognizer()
    
    with sr.Microphone() as source:
        voice = rec.listen(source)
    #try/except virheenkäsittely.
    try:
        text = rec.recognize_google(voice,language=lang)
        textbox.insert(INSERT,'You said: ',END)
        textbox.insert(INSERT,text,END)
    except:
        textbox.insert(INSERT,'try again',END)

def clearAll():
    Slow.set(0)
    fast.set(0)

#luodaan root niminen pohjakomponentti ja annetaan sen taustaväriksi vaalean sininen.
root = Tk()
root.configure(background = 'light blue')
root.title('TxtToSpeech')

#luodaan frame komponentit, joiden avulla muut komponentit asemoidaan, annetaan
#komponenttien taustaväriksi vaalean sininen.
frame1 = Frame()
frame1.configure(background = 'light blue')
frame2 = Frame()
frame2.configure(background = 'light blue')
frame3 = Frame()
frame3.configure(background = 'light blue')
frame4 = Frame()
frame4.configure(background = 'light blue')
frame5 = Frame()
frame5.configure(background = 'light blue')

#tallennetaan muuttujaan otsikossa käytettävä fontti.
titlefont = Font(family = 'Bodoni MT')

languages = ['en','fi','fr','de','sv','et']
setLang = ttk.Combobox(frame2, width = 5, values = languages)

voiceLang = ['fi-FI','en-GB','fr-FR']
setVoiceLang = ttk.Combobox(frame5, width = 5, values = voiceLang)

#luodaan label-komennolla tekstikomponentit.
name = Label(root, text = 'Text to speech',font = titlefont,bg = 'light blue')
recongiseName = Label(root, text = 'Recognise speech',font = titlefont,bg = 'light blue')
enterLabel = Label(frame1, text = 'Write your text here',font = titlefont,bg = 'light blue')
langLabel = Label(frame2, text = 'Select a language',font = titlefont,bg = 'light blue')
voiceLang = Label(frame5, text = 'Set a language: ')
textbox = Text(root,width = 20, height = 5)

#luodaan entry komennolla syötekentätä
enterText = Entry(frame1)


#luodaan button komennolla painikkeet, command komennolla kerrotaan
#mikä funktio suoritetaan, kun painiketta on painettu.

savebtn = Button(frame3,text = 'Save', command = selectFunc)
playbtn = Button(frame3,text = 'Play', command = playSpeech)
stopbtn = Button(frame3,text = 'Stop', command = stopSpeech)
questionbtn = Button(frame2, text = '?', command = showInfo)
recbtn = Button(root, text = 'Start recognise',command = recognise)
clearbtn = Button(root, text = 'Clear all selections', command = clearAll)


#luodaan valintaruudut.
Slow = IntVar()
slowSelect = Checkbutton(frame4, text = 'Slow speech rate',variable = Slow,bg = 'light blue')

fast = IntVar()
fastSelect = Checkbutton(frame4, text = 'Normal speech rate',variable = fast,bg = 'light blue')

#pakataan komponentit, pady ja padx komennoilla lisätään tyhjää tilaa
#komponenttien ympärille.
name.pack()
frame1.pack()
enterLabel.pack(side=LEFT)
enterText.pack(side=RIGHT,pady=4,padx=4)
frame2.pack()
langLabel.pack(side=LEFT)
setLang.pack(side=LEFT,pady=4,padx=4)

questionbtn.pack(side=RIGHT)
frame4.pack()
slowSelect.pack()
fastSelect.pack()
frame3.pack()
savebtn.pack(side=LEFT,pady=4,padx=4)
playbtn.pack(side=RIGHT,pady=4,padx=4)
stopbtn.pack(pady=4,padx=4)
recongiseName.pack(pady=4)
frame5.pack()
voiceLang.pack(side=LEFT,pady=4,padx=4)
setVoiceLang.pack(side=RIGHT,pady=4)
textbox.pack()
recbtn.pack(pady=4)
clearbtn.pack()
mainloop()
