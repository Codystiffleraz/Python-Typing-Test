from words import unique_words
import tkinter as tk
import random
import time
import threading

test_words = []
runs = 0

def random_words():
    while len(test_words) < 10:
        r = random.choice(unique_words)
        test_words.append(r)
class TypeSpeedGUI:
    random_words()
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Typing Test")
        self.root.geometry("800x600")
        
        self.text = open("text.txt", "r").read().split("\n")
        
        self.frame = tk.Frame(self.root)
        
        self.sample_label = tk.Label(self.frame, text=test_words, font=("Arial", 18,), wraplength=700)
        self.sample_label.grid(row=0,column=0, columnspan=2, padx=5, pady=10)
        
        self.input_entry = tk.Entry(self.frame, width=40, font=("Arial", 24))
        self.input_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=10)
        self.input_entry.bind("<KeyPress>", self.start)
        
        self.speed_label = tk.Label(self.frame, text="Speed: \n0.00 CPS\n0.00 CPM", font=("Arial", 18,))
        self.speed_label.grid(row=2,column=0, columnspan=2, padx=5, pady=10)
        
        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset)
        self.reset_button.grid(row=3, column=0, columnspan=2, padx=5, pady=10) 
        
        self.frame.pack(expand=True)
        
        self.counter = 0
        self.running = False
        
        self.root.mainloop()

    def start(self, event):
        if not self.running:
            # if the key pressed is not shift, alt, and ctrl
            if not event.keycode in [16, 17, 18]:
                self.running = True
                t = threading.Thread(target=self.time_thread)
                t.start()
        if not self.sample_label.cget('text').startswith(self.input_entry.get()):
            self.input_entry.config(fg="red")
        else:
            self.input_entry.config(fg="black")
        if self.input_entry.get() == self.sample_label.cget('text')[:-1]:
            self.running = False
            self.input_entry.config(fg='green')
    
    def time_thread(self):
        while self.running:
            time.sleep(0.1)
            self.counter += 0.1
            cps = len(self.input_entry.get()) / self.counter
            cpm = cps * 60
            self.speed_label.config(text=f"Speed: \n{cps:.2f} CPS\n{cpm:2f} CPM")
    
    def reset(self):
        test_words.clear()
        random_words()
        self.running = False
        self.counter = 0
        self.speed_label.config(text="Speed: \n0.00 CPS\n0.00 CPM", font=("Arial", 18,))
        self.sample_label.config(text=test_words)
        self.input_entry.delete(0, tk.END)
        

TypeSpeedGUI()