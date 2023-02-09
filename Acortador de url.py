import tkinter as tk
import pyshorteners

def shorten_url():
    s = pyshorteners.Shortener()
    long_url = entry.get()
    short_url = s.tinyurl.short(long_url)
    result.config(state="normal")
    result.delete("1.0", tk.END)
    result.insert(tk.END, short_url)
    result.config(state="disabled")

root = tk.Tk()
root.title("Acortador de URL")
root.config(bg="#333")

frame1 = tk.Frame(root, bg="#333")
frame1.pack(padx=10, pady=10)

label = tk.Label(frame1, text="URL larga:", bg="#333", fg="white")
label.pack(side=tk.LEFT)

entry = tk.Entry(frame1, width=50, bg="#444", fg="white")
entry.pack(side=tk.LEFT)

frame2 = tk.Frame(root, bg="#333")
frame2.pack(padx=10, pady=10)

label = tk.Label(frame2, text="URL acortada:", bg="#333", fg="white")
label.pack(side=tk.LEFT)

result = tk.Text(frame2, height=1, width=50, state="disabled", bg="#444", fg="white")
result.pack(side=tk.LEFT)

frame3 = tk.Frame(root, bg="#333")
frame3.pack(padx=10, pady=10)

button = tk.Button(frame3, text="Acortar", command=shorten_url, bg="#444", fg="white", relief=tk.SUNKEN, bd=0)
button.pack()

root.mainloop()
