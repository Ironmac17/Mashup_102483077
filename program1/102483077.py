import sys
import os
import warnings
import yt_dlp
from pydub import AudioSegment

warnings.filterwarnings("ignore")

TEMP_DIR = "temp"


def download_audio(singer, n):
    os.makedirs(TEMP_DIR, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{TEMP_DIR}/%(id)s.%(ext)s',
        'quiet': True,
        'no_warnings': True,
        'noplaylist': True,
        'ignoreerrors': True,

        'extractor_args': {
            'youtube': {'player_client': ['android']}
        },

        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }]
    }

    files = []

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(
                f"ytsearch{n}:{singer} official song", download=True
            )

            if 'entries' in info:
                for entry in info['entries']:
                    if entry:
                        filename = ydl.prepare_filename(entry)
                        filename = filename.rsplit(".", 1)[0] + ".mp3"
                        files.append(filename)
    except Exception as e:
        print("Download error:", e)

    return files


def create_mashup(files, duration, output):
    final_audio = AudioSegment.empty()

    for file in files:
        try:
            audio = AudioSegment.from_file(file)
            clip = audio[:duration * 1000]
            final_audio += clip
        except:
            continue

    final_audio.export(output, format="mp3")


def main():
    try:
        if len(sys.argv) != 5:
            print("Usage: python <rollnumber>.py <SingerName> <NoVideos> <DurationSec> <OutputFile>")
            return

        singer = sys.argv[1]
        n = int(sys.argv[2])
        duration = int(sys.argv[3])
        output = sys.argv[4]

        # validation
        if n <= 10:
            print("Error: Number of videos must be greater than 10.")
            return

        if duration <= 20:
            print("Error: Duration must be greater than 20 seconds.")
            return

        print("Downloading songs...")
        files = download_audio(singer, n)

        if not files:
            print("No files downloaded.")
            return

        print("Creating mashup...")
        create_mashup(files, duration, output)

        print("Mashup created successfully:", output)

    except ValueError:
        print("Error: Invalid numeric input.")
    except Exception as e:
        print("Unexpected error:", e)


if __name__ == "__main__":
    main()
