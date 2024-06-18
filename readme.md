# Tube2MP3 Master

Tube2MP3 Master is a Python application that allows you to download YouTube videos as MP3 files. It provides a simple and elegant graphical user interface (GUI) for entering the YouTube URL and specifying the output directory.

## Features

- Downloads audio from YouTube videos and converts it to MP3.
- Organizes downloaded MP3 files in directories named after the video author.
- Provides a progress bar to indicate download progress.
- User-friendly GUI built with Tkinter.

## Requirements

- Python 3.6+
- `pytube`
- `pydub`
- `tkinter`
- `ffmpeg` (for audio conversion)

## Installation

1. **Clone the repository:**
   git clone https://github.com/EnigmaK9/youtube-to-mp3
   cd tube2mp3-master

### Create and activate a virtual environment:

`
python3 -m venv myenv
source myenv/bin/activate

### Install the required Python packages:

`
pip install pytube pydub

Install ffmpeg:

### On Debian/Ubuntu:

`
sudo apt install ffmpeg


### On MacOS using Homebrew:

`
brew install ffmpeg


## Usage
Run the application:

`
python Tube2MP3.py

Enter the YouTube video URL and the output directory in the GUI.

Click the "Download" button to start the download and conversion process.


