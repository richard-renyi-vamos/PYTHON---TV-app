import tkinter as tk
from tkinter import messagebox
import webbrowser

# Sample channel data with names and URLs
CHANNELS = {
    "Channel 1 - News": "https://www.youtube.com/watch?v=your_news_channel_url",
    "Channel 2 - Sports": "https://www.youtube.com/watch?v=your_sports_channel_url",
    "Channel 3 - Movies": "https://www.netflix.com",
    "Channel 4 - Music": "https://www.spotify.com",
    "Channel 5 - Documentaries": "https://www.nationalgeographic.com",
}

# Function to play the selected channel
def play_channel(channel_name):
    url = CHANNELS.get(channel_name)
    if url:
        webbrowser.open(url)
    else:
        messagebox.showerror("Error", "Channel URL not found!")

# Function to handle channel selection
def on_channel_select(event):
    selected_channel = channel_listbox.get(channel_listbox.curselection())
    play_channel(selected_channel)

# Create the main app window
root = tk.Tk()
root.title("TV App")
root.geometry("400x300")

# App header
header_label = tk.Label(root, text="Welcome to the TV App!", font=("Arial", 16))
header_label.pack(pady=10)

# Channel listbox
channel_listbox = tk.Listbox(root, font=("Arial", 12))
channel_listbox.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Add channels to the listbox
for channel_name in CHANNELS.keys():
    channel_listbox.insert(tk.END, channel_name)

# Play button
play_button = tk.Button(root, text="Play Channel", font=("Arial", 14), command=lambda: on_channel_select(None))
play_button.pack(pady=10)

# Event binding for double-click on a channel
channel_listbox.bind("<Double-1>", on_channel_select)

# Run the app
root.mainloop()
