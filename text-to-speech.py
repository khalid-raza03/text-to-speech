import tkinter as tk
import pyttsx3

class text_to_speech():
    def __init__(self, master):
        self.master = master
        self.master.title("Text to Speech Converter")
        screen_width = self.master.winfo_screenwidth() 
        screen_height = self.master.winfo_screenheight()
        
        self.master.geometry(f"{screen_width}x{screen_height}+0+0")
        
        # Project Title design
        projectTitle = tk.Label(self.master, text="Text to speech converter" , bg="black", fg="white",  font=("Sans-serif", 30, "bold"), padx=20, pady=40 )
        
        projectTitle.pack(side="top", fill="x")
        projectFrame = tk.Frame(self.master, bg="plum")
        projectFrame.place(x=425, y=150, width=700, height=400)
        
        # Frame Title
        frameTitle = tk.Label(projectFrame, text="Write your desired text to get started !", font=("Sans-serif", 18, "bold") )
        
        frameTitle.grid(row=0, column=0, padx=20, pady=40, sticky="ew")
        projectFrame.grid_columnconfigure(0, weight=1)
        
        # Text Area styles
        self.textArea = tk.Text(projectFrame, bd=2, relief="sunken", font=("Sans-serif", 15), wrap="word", height=5)
        self.textArea.grid(row=1, column=0, padx=10, pady=20, sticky="nsew")
        projectFrame.grid_rowconfigure(1, weight=1)
        
        # Clear Button UI
        convertBtn = tk.Button(projectFrame, command=self.tts, text="Extract Speech", font=("Sans-serif", 16, "bold"), bg="blue", fg="white")
        convertBtn.grid(row=2, column=0, padx=20, pady=20, sticky="ew")
        
    def tts(self):
        value = self.textArea.get('1.0', tk.END).strip()
        if value:
            engine = pyttsx3.init()
            engine.say(value)
            engine.runAndWait()
            self.clearText()
            
    def clearText(self):
        self.textArea.delete('1.0', tk.END)        

        
master = tk.Tk()
obj = text_to_speech(master)
master.mainloop()         
            
        
        