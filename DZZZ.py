import tkinter as tk


def change_label():
    if label.cget("text") == "Початковий напис":
        label.config(text="Новий напис")
    else:

        label.config(text="Початковий напис")


def update_counter():
    global click_count
    click_count += 1
    counter_label.config(text=f"Кількість клацань: {click_count}")


click_count = 0

root = tk.Tk()
root.title("Click Counter")

label = tk.Label(root, text="Початковий напис", font=("Helvetica", 18))
label.pack(pady=20)

button = tk.Button(root, text="Змінити напис", command=change_label)
button.pack(pady=10)

counter_label = tk.Label(root, text=f"Кількість клацань: {click_count}")
counter_label.pack(pady=5)

button.config(command=lambda: [change_label(), update_counter()])

root.mainloop()