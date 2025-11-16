import tkinter as tk
from tkinter import filedialog, ttk
import os
import threading
from SZip_Extract import extract_sz
from SZip_Compress import compress_szip

class SZipGUI:
    def __init__(self, root):
        self.root = root
        root.title("S-zip Utility 🗂️")
        root.geometry("520x430")

        self.mode = tk.StringVar(value="extract")

        # --- Mode ---
        frame_mode = tk.LabelFrame(root, text="Mode")
        frame_mode.pack(fill="x", padx=10, pady=5)

        tk.Radiobutton(frame_mode, text="Extract (.sz → folder)", variable=self.mode, value="extract").pack(anchor="w")
        tk.Radiobutton(frame_mode, text="Compress (folder → .sz)", variable=self.mode, value="compress").pack(anchor="w")

        # --- Input Path ---
        frame_in = tk.LabelFrame(root, text="Input")
        frame_in.pack(fill="x", padx=10, pady=5)

        self.entry_in = tk.Entry(frame_in)
        self.entry_in.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        tk.Button(frame_in, text="Browse...", command=self.browse_input).pack(side="right", padx=5)

        # --- Output Path ---
        frame_out = tk.LabelFrame(root, text="Output")
        frame_out.pack(fill="x", padx=10, pady=5)

        self.entry_out = tk.Entry(frame_out)
        self.entry_out.pack(side="left", fill="x", expand=True, padx=5, pady=5)

        tk.Button(frame_out, text="Browse...", command=self.browse_output).pack(side="right", padx=5)

        # --- Start Button ---
        tk.Button(root, text="Start", font=("Arial", 12, "bold"),
                  command=self.start_process).pack(pady=10)

        # --- Progress Bar ---
        self.progress = ttk.Progressbar(root, mode="indeterminate")
        self.progress.pack(fill="x", padx=10, pady=5)

        # --- Log ---
        frame_log = tk.LabelFrame(root, text="Log")
        frame_log.pack(fill="both", expand=True, padx=10, pady=5)

        self.log = tk.Text(frame_log, height=8)
        self.log.pack(fill="both", expand=True)

    def browse_input(self):
        if self.mode.get() == "extract":
            path = filedialog.askopenfilename(filetypes=[("S-zip Files", "*.sz")])
        else:
            path = filedialog.askdirectory()
        if path:
            self.entry_in.delete(0, tk.END)
            self.entry_in.insert(0, path)

    def browse_output(self):
        if self.mode.get() == "extract":
            path = filedialog.askdirectory()
        else:
            path = filedialog.asksaveasfilename(defaultextension=".sz", filetypes=[("S-zip", "*.sz")])
        if path:
            self.entry_out.delete(0, tk.END)
            self.entry_out.insert(0, path)

    def start_process(self):
        self.in_path = self.entry_in.get().strip()
        self.out_path = self.entry_out.get().strip()

        if not self.in_path or not self.out_path:
            self.log.insert("end", "⚠ Input or Output path missing!\n")
            return

        self.progress.start()
        self.log.insert("end", "▶ Starting...\n")

        # Run in background thread
        threading.Thread(target=self.run_task, args=(self.in_path, self.out_path), daemon=True).start()

    def gui_log(text):
        gui_log_textbox.append(text)     # そのまま表示
        progressbar.setValue(progressbar.value() + 1)
        compress_szip(self.path_in, self.path_out, log_callback=gui_log)


    def run_task(self, in_path, out_path):
        mode = self.mode.get()
        try:
            if mode == "extract":
                self.log.insert("end", f"Extracting {in_path}...\n")
                extract_sz(in_path, out_path)
                self.log.insert("end", "✔ Extract Complete!\n")
            else:
                self.log.insert("end", f"Compressing {in_path}...\n")
                compress_szip(in_path, out_path)
                self.log.insert("end", "✔ Compression Complete!\n")
        except Exception as e:
            self.log.insert("end", f"❌ Error: {e}\n")

        self.progress.stop()


if __name__ == "__main__":
    root = tk.Tk()
    app = SZipGUI(root)
    root.mainloop()
