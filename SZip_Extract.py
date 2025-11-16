import os
import gzip
import base64
import re
import sys
from tqdm import tqdm

def extract_sz(path, out_dir):
    print(f"📦 Loading archive: {path}")

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Files list parsing
    m = re.search(r"\[Files\](.*?)(?:\n\[|$)", text, re.DOTALL)
    if not m:
        raise ValueError("Files section not found.")
    files_raw_block = m.group(1).strip().splitlines()

    file_list = []
    current_dir = None

    for raw in files_raw_block:
        line = raw.strip()
        if not line:
            continue

        if line.startswith("{") and line.endswith("/"):
            current_dir = line[1:]  # Director name with "/"
        elif line == "}":
            current_dir = None
        else:
            archive_name = (current_dir or "") + line
            archive_name = archive_name.replace("\\", "/")
            file_list.append(archive_name)

    if not file_list:
        print("⚠ No files listed in the archive.")
        return

    print(f"🔍 Found {len(file_list)} file(s).")
    print("⬇ Extracting files...\n")

    # Progress bar with tqdm
    for archive_name in tqdm(file_list, desc="Extracting", unit="file"):
        # Human-friendly "Now extracting" message
        print(f"{archive_name} ... ", end="", flush=True)

        # Find block
        pattern = rf"\[{re.escape(archive_name)}\]\s*(.*?)(?=\n\[|$)"
        match = re.search(pattern, text, re.DOTALL)
        if not match:
            raise ValueError(f"Data block for {archive_name} not found.")

        b64data = match.group(1).strip()

        gzip_data = base64.b64decode(b64data)
        raw = gzip.decompress(gzip_data)

        # Real filesystem path
        parts = archive_name.split("/")
        out_path = os.path.join(out_dir, *parts)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)

        with open(out_path, "wb") as f:
            f.write(raw)

        print("Done")  # Finish text

    print("\n🎉 Done! All files extracted successfully.\n")


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        szfile = sys.argv[1]
    else:
        print("Usage: python S-Zip_Extract.py <Input .sz File> <OutputFolder Name>")
        sys.exit(1)

    outdir = sys.argv[2] if len(sys.argv) >= 3 else "output"

    print(f"▶ Starting extraction...")
    extract_sz(szfile, outdir)
