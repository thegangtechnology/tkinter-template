import tkinter as tk

color = 'red'


def main():
    app = tk.Tk()

    label = tk.Label(app, text='here', bg=color)

    def change_color():
        global color
        color = 'red' if color != 'red' else 'blue'
        label.config(bg=color)

    button = tk.Button(app, command=change_color, text='Click Me')
    label.pack()
    button.pack()
    app.mainloop()


if __name__ == '__main__':
    main()
