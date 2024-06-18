import os
import re
import tkinter as tk
from tkinter import ttk, messagebox
from pytube import YouTube
from pydub import AudioSegment

def to_kebab_case(text):
    """Convert text to kebab-case."""
    return re.sub(r'[\W_]+', '-', text).strip().lower()

def download_video_as_mp3(url, output_path, progress_var):
    try:
        # Create a YouTube object
        yt = YouTube(url, on_progress_callback=lambda stream, chunk, bytes_remaining: update_progress(progress_var, bytes_remaining, stream.filesize))

        # Select the audio stream
        stream = yt.streams.filter(only_audio=True).first()

        # Create the author's directory if it doesn't exist
        author_directory = os.path.join(output_path, to_kebab_case(yt.author))
        os.makedirs(author_directory, exist_ok=True)

        # Download the audio stream
        audio_file = stream.download(author_directory)

        # Convert the downloaded file to MP3
        base, ext = os.path.splitext(audio_file)
        mp3_file = os.path.join(author_directory, to_kebab_case(yt.title) + '.mp3')

        AudioSegment.from_file(audio_file).export(mp3_file, format="mp3")

        # Optionally, remove the original downloaded file
        os.remove(audio_file)

        messagebox.showinfo("Success", f"MP3 downloaded: {mp3_file}")
    except Exception as e:
        messagebox.showerror("Error", f"Error downloading the MP3: {e}")

def update_progress(progress_var, bytes_remaining, total_size):
    progress = (total_size - bytes_remaining) / total_size * 100
    progress_var.set(progress)

def on_download_button_click(url_entry, output_entry, progress_var):
    url = url_entry.get()
    output_path = output_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube video URL.")
        return
    if not output_path:
        output_path = "."
    progress_var.set(0)
    download_video_as_mp3(url, output_path, progress_var)

def main():
    # Create the Tkinter root window
    root = tk.Tk()
    root.title("Tube2MP3 Master")

    # Set window size
    root.geometry("600x300")

    # Set window background color
    root.configure(bg="#282c34")

    # URL label and entry
    tk.Label(root, text="YouTube Video URL:", fg="white", bg="#282c34", font=("Helvetica", 12, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky='e')
    url_entry = tk.Entry(root, width=50)
    url_entry.grid(row=0, column=1, padx=10, pady=10)

    # Output path label and entry
    tk.Label(root, text="Output Directory:", fg="white", bg="#282c34", font=("Helvetica", 12, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky='e')
    output_entry = tk.Entry(root, width=50)
    output_entry.grid(row=1, column=1, padx=10, pady=10)

    # Download button
    progress_var = tk.DoubleVar()
    download_button = tk.Button(root, text="Download", command=lambda: on_download_button_click(url_entry, output_entry, progress_var), bg="#61afef", fg="white", font=("Helvetica", 12, "bold"))
    download_button.grid(row=2, column=0, columnspan=2, pady=10)

    # Progress bar
    progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
    progress_bar.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky='ew')

    # Add some padding around the widgets
    for widget in root.winfo_children():
        widget.grid_configure(padx=5, pady=5)

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()

