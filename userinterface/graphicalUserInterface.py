from tkinter import *
from tkinter import messagebox

# used openweathermap api and postman


class GUI:
    def __init__(self, controller):
        self._controller = controller

        self.root = Tk()
        self.root.title("Weather Application")
        self.root.iconbitmap("../WeatherApplication/weather.ico")
        self.root.config(bg='white')

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width / 2) - (550 / 2)  # make the main window pop on the middle of the screen
        y = (screen_height / 2) - (400 / 2)
        self.root.geometry(f'{550}x{400}+{int(x)}+{int(y)}')

    def get_weather(self, arg):
        city = self.city_entry.get()
        try:
            self.important_label.config(text='')
            self.less_important_label.config(text='')

            important_info, less_important_info = self._controller.get_weather(city)

            self.important_label.config(text=important_info)
            self.less_important_label.config(text=less_important_info)
        except KeyError:
            messagebox.showerror('Error', 'Please introduce a city that exists!')
            self.city_entry.delete(0, END)

    def start(self):
        entry_font = ('Castellar', 25, 'bold')
        labels_font = ('Castellar', 15, 'bold')

        self.city_entry = Entry(self.root, justify='center', width=50, border=2, font=entry_font)
        self.city_entry.pack(pady=15)
        self.city_entry.focus()     # the user can type directly when he opens the application
        self.city_entry.bind('<Return>', self.get_weather)

        self.important_label = Label(self.root, bg='white', font=labels_font)
        self.important_label.pack(pady=25)

        self.less_important_label = Label(self.root, bg='white', font=labels_font)
        self.less_important_label.pack()

        self.root.mainloop()
