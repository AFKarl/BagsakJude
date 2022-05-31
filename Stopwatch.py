from cgitb import text
import tkinter as tk
from tkinter.font import BOLD
from turtle import back

class stopwatch(tk.Frame):

    def __init__(self,window=None):
        super().__init__(window)
        self.window = window
        self.new_time = ""
        self.running = False
        self.total_minutes = 0
        self.total_seconds = 0
        self.total_miliseconds = 0
        self.pack
        self.laps = 0
        self.features()
        self.lap_dictionary = {
            "0": self.lap_1,
            "1": self.lap_2,
            "2": self.lap_3,
            "3": self.lap_4,
            "4": self.lap_5,
            "5": self.lap_6,
            "6": self.lap_7,
            "7": self.lap_8,
            "8": self.lap_9,
            "9": self.lap_10,
        }

    def features(self):

        self.stopwatch_label = tk.Label(text='00:00:00', font=('courier', 50))
        self.stopwatch_label.pack(pady=5, ipady=20)

        self.lap_1 = tk.Label(text="00:00:00", font=("courier", 15), height="1")
        self.lap_1.pack()
        self.lap_2 = tk.Label(text="00:00:00", font=("courier", 15), height="1")
        self.lap_2.pack()
        self.lap_3 = tk.Label(text="00:00:00", font=("courier", 15), height="1")
        self.lap_3.pack()
        self.lap_4 = tk.Label(text="00:00:00", font=("courier", 15), height="1")
        self.lap_4.pack()
        self.lap_5 = tk.Label(text="00:00:00", font=("courier", 15), height="1")
        self.lap_5.pack()
        self.lap_6 = tk.Label(text="00:00:00", font=("courier", 15), height="1")
        self.lap_6.pack()
        self.lap_7 = tk.Label(text="00:00:00", font=("courier", 15), height="1")
        self.lap_7.pack()
        self.lap_8 = tk.Label(text="00:00:00", font=("courier", 15), height="1")
        self.lap_8.pack()
        self.lap_9 = tk.Label(text="00:00:00", font=("courier", 15), height="1")
        self.lap_9.pack()
        self.lap_10 = tk.Label(text="00:00:00", font=("courier", 15), height="1")
        self.lap_10.pack()

        self.start_time_button = tk.Button(text='Start', height=2, width=10, font=('Segoe UI Semibold', 15), command=self.start_time)
        self.start_time_button.pack(anchor='s', side=tk.LEFT)

        self.pause_time_button = tk.Button(text='Stop', height=2, width=11, font=('Segoe UI Semibold', 15), command=self.pause_time)
        self.pause_time_button.pack(anchor='s', side=tk.LEFT)

        self.split_time_button = tk.Button(text='Splits/Laps', height=2, width=11, font=('Segoe UI Semibold', 15), command=self.split_time)
        self.split_time_button.pack(anchor='s', side=tk.LEFT)

        self.reset_button = tk.Button(text='Reset', height=2, width=10, font=('Segoe UI Semibold', 15), command=self.reset_time)
        self.reset_button.pack(anchor='s', side=tk.LEFT)

        self.window.title("STOPWATCH")


    def split_time(self):
        if self.running:
            lap_length = [x for x in range(len(self.lap_dictionary))]

            if  self.laps in lap_length:
                self.lap_dictionary[str(self.laps)].configure(text=self.stopwatch_label['text'])
                self.laps += 1

            else:
                self.laps = 0
                for key, value in self.lap_dictionary.items():
                    value.configure(text="00:00:00")
                self.lap_dictionary[str(self.laps)].configure(text=self.stopwatch_label['text'])
                
        
    def start_time(self):
        if not self.running:
            self.change()
            self.running = True


    def pause_time(self):
        if self.running:
            self.stopwatch_label.after_cancel(self.new_time)
            self.running = False


    def reset_time(self):
        if self.running:
            self.reset_button.after_cancel(self.new_time)
            self.running = False

            for key, value in self.lap_dictionary.items():
                value.configure(text="00:00:00")
                self.laps = 0


        self.total_miliseconds, self.total_minutes, self.total_seconds = 0,0,0
        self.stopwatch_label.config(text='00:00:00')


    def change(self):
        self.total_miliseconds += 1
        if self.total_miliseconds == 60:
            self.total_seconds +=1
            self.total_miliseconds = 0
        if self.total_minutes == 60:
            self.total_minutes += 1
            self.total_seconds = 0
    
        total_minutes_string = f'{self.total_minutes}' if self.total_minutes>9 else f'0{self.total_minutes}'
        total_seconds_string = f'{self.total_seconds}' if self.total_seconds>9 else f'0{self.total_seconds}'
        total_miliseconds_string = f'{self.total_miliseconds}' if self.total_miliseconds>9 else f'0{self.total_miliseconds}'

        self.stopwatch_label.config(text=total_minutes_string + ':' + total_seconds_string + ":" + total_miliseconds_string)
        
        self.new_time = self.stopwatch_label.after(10,self.change)


root = tk.Tk()
obj = stopwatch(window=root)
obj.mainloop()
