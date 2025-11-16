# **README (English Version)**

# **S-Zip (Sakuzyo Zip)**

A simple, slightly joke-oriented but still functional compression/extraction tool using the custom **.sz** format.
Supports both **GUI** and **CLI**, and runs entirely on **Python**.

---

## 🚀 **Features**

* Supports the custom archive format **.sz**
* Internally uses **gzip + Base64** (human-readable)
* GUI with a clean progress bar
* CLI with detailed per-file logs
* Works on Windows / Linux / macOS (probably!)

---

## 📦 **Installation**

If you have Python installed, you're good to go.

```sh
git clone https://github.com/USER/s-zip.git
cd s-zip
```

Install tqdm if needed:

```sh
pip install tqdm
```

If `pip` is not found:

```sh
python -m pip install tqdm
```

---

## 🖥️ **GUI Version**

Run the GUI with:

```sh
python S-Zip_GUI.py
```

You can drag & drop folders and choose **Compress** or **Extract**.

---

## 🧰 **CLI Usage**

### ▶ **Compression**

```sh
python SZip_Compress.py <input_folder> <output_name>
```

### ▶ **Extraction**

```sh
python SZip_Extract.py <input.sz> <output_folder_name>
```

---

## 📁 **S-Zip Format (Simple Spec)**

```txt
[Files]
{folder1/
file.txt
}
image.png

[folder1/file.txt]
<gzip_base64>

[image.png]
<gzip_base64>
```

---

## 📝 **Requirements**

* Python 3.9+
* tqdm (for progress display)

---

## 🛠 **Folder Structure**

```txt
s-zip/
├─ SZip_Compress.py
├─ SZip_Extract.py
├─ S-Zip_GUI.py
├─ README.md
└─ LICENSE
```

---

## 📜 **License**

Released under the **Sakuzyokun License**.

---

## ✨ **Author**

**Sakuzyokun**

も作れるから言ってな！
