# S-Zip (Sakuzyo Zip)
独自形式「.sz」を使った、シンプルでネタ寄りだけど実用もできる圧縮＆解凍ツールです。  
GUI と CLI の両方に対応していて、Python だけで動きます。

---

## 🚀 Features
- 独自拡張子 **.sz** 形式に対応
- 中身は **gzip + Base64** のシンプル構造
- GUI で進捗バー表示
- CLI でファイルごとのログを出力
- Windows / Linux / macOS（多分）で動作

---

## 📦 Installation
Python が入っていれば OK。

```

git clone [https://github.com/USER/s-zip.git](https://github.com/USER/s-zip.git)
cd s-zip

```

必要なら tqdm をインストール：

```

pip install tqdm

```

pip が無いと言われた場合:

```

python -m pip install tqdm

```

---

## 🖥️ GUI Version
GUI を起動するには：

```

python S-Zip_GUI.py

```

ドラッグ＆ドロップでフォルダ指定 → 圧縮 or 解凍 ができます。

---

## 🧰 CLI Usage

### ▶ 圧縮
```

python SZip_Compress.py <input_folder> <output_name>

```


### ▶ 解凍
```

python SZip_Extract.py <input.sz> <output_folder_name>

```

---

## 📁 S-Zip Format (簡易仕様)
```

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

## 📝 Requirements
- Python 3.9+
- tqdm（進捗表示用）

---

## 🛠 Folder Structure
```

s-zip/
├─ SZip_Compress.py
├─ SZip_Extract.py
├─ S-Zip_GUI.py
├─ README.md
└─ LICENSE

```

---

## 📜 License
削除くんライセンス で使えます。

---

## ✨ Author
削除くん (Sakuzyokun)
