import subprocess
import tkinter as tk
import os

profiles = ["Default", "Profile 1", "Profile 2", "Profile 3", "Profile 9", "Profile 10"]

def open_chrome_windows():
    url = url_entry.get()
    for profile in profiles:
        subprocess.Popen(["/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", "--new-window", "--profile-directory=" + profile, url])

def close_terminal():
    app_name = "Terminal"
    os.system(f"pkill {app_name}")

def on_close():
    close_terminal()
    window.destroy()

# Create the tkinter window
window = tk.Tk()

# Add a label and entry for the website URL
url_label = tk.Label(window, text="링크:")
url_label.pack()
url_entry = tk.Entry(window)
url_entry.pack()

# Add a button to open Chrome windows
button = tk.Button(window, text="열기", command=open_chrome_windows)
button.pack()

# set window size
window_width = 200
window_height = 100
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# calculate x and y coordinates for centering window
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

# set window position and title
window.geometry('{}x{}+{}+{}'.format(window_width, window_height, x, y))
window.title("다계정 열기")

# register the on_close() function with the protocol() method
window.protocol("WM_DELETE_WINDOW", on_close)

# Run the tkinter event loop
window.mainloop()
