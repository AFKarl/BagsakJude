import tkinter as tk

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

    def features(self):

        self.stopwatch_label = tk.Label(text='00:00:00', font=('Arial', 50))
        self.stopwatch_label.pack(pady=5, ipady=20)

        self.lap_1 = tk.Label(text="00:00:00", font=("Arial", 15), height="1")
        self.lap_1.pack()
        self.lap_2 = tk.Label(text="00:00:00", font=("Arial", 15), height="1")
        self.lap_2.pack()
        self.lap_3 = tk.Label(text="00:00:00", font=("Arial", 15), height="1")
        self.lap_3.pack()
        self.lap_4 = tk.Label(text="00:00:00", font=("Arial", 15), height="1")
        self.lap_4.pack()
        self.lap_5 = tk.Label(text="00:00:00", font=("Arial", 15), height="1")
        self.lap_5.pack()

        self.start_time_button = tk.Button(text='Start', height=2, width=10, font=('Arial', 15),)
        self.start_time_button.pack(anchor='s', side=tk.LEFT)

        self.pause_time_button = tk.Button(text='Stop', height=2, width=11, font=('Arial', 15), )
        self.pause_time_button.pack(anchor='s', side=tk.LEFT)

        self.split_time_button = tk.Button(text='Splits/Laps', height=2, width=11, font=('Arial', 15),)
        self.split_time_button.pack(anchor='s', side=tk.LEFT)

        self.reset_button = tk.Button(text='Reset', height=2, width=10, font=('Arial', 15),)
        self.reset_button.pack(anchor='s', side=tk.LEFT)

        self.window.title("STOPWATCH")


root = tk.Tk()
obj = stopwatch(window=root)
obj.mainloop()