import tkinter as tk
from tkinter import filedialog, messagebox
from ukrainian_tts.tts import TTS, Voices, Stress
import IPython.display as ipd

tts = TTS(device="cpu")


def generate_audio():
    text = text_entry.get("1.0", "end-1c")  # Get text from text entry
    selected_voice = voice_var.get()  # Get selected voice
    if not text:
        messagebox.showwarning("Warning", "Please enter the text.")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
    if file_path:
        with open(file_path, mode="wb") as file:
            _, output_text = tts.tts(text, selected_voice, Stress.Dictionary.value, file)
        messagebox.showinfo("Success", f"Audio saved at {file_path}")
        print("Accented text:", output_text)
    else:
        messagebox.showwarning("Warning", "No file selected.")


# Function to handle Ctrl+V (paste)
def paste_text(event=None):
    try:
        text_entry.insert(tk.INSERT, window.clipboard_get())
    except tk.TclError:
        pass  # Ignore if there's nothing to paste

# Initialize Tkinter window
window = tk.Tk()
window.title("Ukrainian TTS")

# Create text entry box
tk.Label(window, text="Enter Text:").pack()
text_entry = tk.Text(window, height=10, width=50)
text_entry.pack()

# Bind Ctrl+V to the paste function
text_entry.bind('<Control-v>', paste_text)

# Create voice selection dropdown
tk.Label(window, text="Select Voice:").pack()
voice_var = tk.StringVar(value=Voices.Mykyta.value)
voice_options = [Voices.Mykyta.value, Voices.Tetiana.value, Voices.Dmytro.value, Voices.Lada.value, Voices.Oleksa.value]
voice_menu = tk.OptionMenu(window, voice_var, *voice_options)
voice_menu.pack()

# Create button to generate audio
generate_button = tk.Button(window, text="Generate Audio", command=generate_audio)
generate_button.pack()

# Start the Tkinter loop
window.mainloop()
