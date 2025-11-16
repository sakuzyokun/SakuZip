import os
import gzip
import base64
import sys
import time
from tqdm import tqdm

def gzip_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    compressed = gzip.compress(data)
    return base64.b64encode(compressed).decode("utf-8")

def compress_szip(input_folder, output_name):

    if not output_name.lower().endswith(".sz"):
        output_name += ".sz"

    # ファイル一覧
    file_list = []
    for root, dirs, files in os.walk(input_folder):
        for f in files:
            full = os.path.join(root, f)
            relative = os.path.relpath(full, input_folder)
            file_list.append((full, relative))

    if not file_list:
        print("❌ No files found.")
        return

    print("🗜️ Compressing...\n")

    start = time.time()

    lines = []

    # ----- [Files] ヘッダ -----
    lines.append("[Files]")
    for full, rel in file_list:
        if "/" in rel or "\\" in rel:
            folder = os.path.dirname(rel).replace("\\", "/")
            filename = os.path.basename(rel)
            lines.append(f"{{{folder}/")
            lines.append(f"{filename}\n}}")
        else:
            lines.append(rel)
    lines.append("")  # 改行

    # ----- 各ファイルの中身 -----
    for i, (full, rel) in enumerate(tqdm(file_list, desc="Progress", unit="file")):
        print(f"{rel} ... ", end="", flush=True)

        content = gzip_base64(full)

        rel_norm = rel.replace("\\", "/")

        lines.append(f"[{rel_norm}]")
        lines.append(content)
        lines.append("")  # 区切り

        print("Done")

        elapsed = time.time() - start
        progress = (i + 1) / len(file_list)
        remain = elapsed * (1 / progress - 1)
        print(f"⏳ Remaining: {int(remain//60)}m {int(remain%60)}s\n")

    # ----- ファイル保存 -----
    with open(output_name, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("🎉 Compression completed!")
    print(f"📦 Output: {output_name}")
    print("✔ S-zip format OK")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python S-Zip_Compress.py <InputFolder> <OutputFile Name>")
        sys.exit(1)

    compress_szip(sys.argv[1], sys.argv[2])
