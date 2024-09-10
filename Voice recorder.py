import tkinter as tk
from tkinter import messagebox
import threading
import sounddevice as sd
import wavio
import numpy as np

class VoiceRecorder:
    def __init__(self, master):
        self.master = master
        master.title("Voice Recorder")

        self.is_recording = False
        self.is_paused = False
        self.frames = []


        self.start_button = tk.Button(master, text="Start Recording", command=self.start_recording)
        self.start_button.pack(pady=10)

        self.pause_button = tk.Button(master, text="Pause Recording", command=self.pause_recording, state=tk.DISABLED)
        self.pause_button.pack(pady=10)

        self.stop_button = tk.Button(master, text="Stop Recording", command=self.stop_recording, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

    def start_recording(self):
        self.is_recording = True
        self.is_paused = False
        self.frames = []
        self.start_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.NORMAL)


        threading.Thread(target=self.record).start()

    def pause_recording(self):
        if self.is_paused:
            # Resume recording
            self.is_paused = False
            self.pause_button.config(text="Pause Recording")
            print("Recording resumed...")
        else:
            # Pause recording
            self.is_paused = True
            self.pause_button.config(text="Resume Recording")
            print("Recording paused...")

    def stop_recording(self):
        self.is_recording = False
        self.start_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.DISABLED)

    def record(self):
        sampling_rate = 44100
        channels = 2
        dtype = 'int16'

        print("Recording started...")
        with sd.InputStream(samplerate=sampling_rate, channels=channels, dtype=dtype, callback=self.audio_callback):
            while self.is_recording:
                if not self.is_paused:
                    sd.sleep(100)
        print("Recording finished!")

        # Concatenate all frames and save as WAV file
        audio_data = np.concatenate(self.frames, axis=0)
        filename = "recorded_audio.wav"
        wavio.write(filename, audio_data, sampling_rate, sampwidth=2)
        print(f"Audio recorded and saved as {filename}")
        messagebox.showinfo("Recording Finished", f"Audio recorded and saved as {filename}")

    def audio_callback(self, indata, frames, time, status):
        if not self.is_paused:
            self.frames.append(indata.copy())


root = tk.Tk()
app = VoiceRecorder(root)
root.mainloop()
