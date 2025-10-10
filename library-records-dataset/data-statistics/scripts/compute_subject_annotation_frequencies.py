import os
import json
import math
import pandas as pd
from statistics import mean
import sys

# --------- CONFIG ----------
DOC_TYPES = ["Article", "Book", "Conference", "Report", "Thesis"]
LANGS = ["en", "de"]

# --- Get input data folder from user or CLI argument ---
if len(sys.argv) > 1:
    ROOT = sys.argv[1]
else:
    ROOT = input("Enter the path to your data folder (e.g., ./library-records-dataset/data): ").strip()

if not os.path.isdir(ROOT):
    raise ValueError(f"❌ The provided path does not exist or is not a directory: {ROOT}")

# Map the logical split name -> list of physical directories to search
SPLIT_DIRS = {
    "train": [os.path.join(ROOT, "train")],
    "dev": [os.path.join(ROOT, "dev")],
    "test": [
        os.path.join(ROOT, "test", "gold-standard-testset"),
        os.path.join(ROOT, "test"),
    ],
}

WRITE_EXCEL_TOO = True
CSV_PATH = "subject_stats.csv"
XLSX_PATH = "subject_stats.xlsx"
# --------------------------


def count_subjects_in_file(path):
    """Return total number of dcterms:subject entries across all @graph items."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return None  # unreadable file -> skip

    total = 0
    graph = data.get("@graph", [])
    if not isinstance(graph, list):
        return 0

    for item in graph:
        subj = item.get("dcterms:subject")
        if subj is None:
            continue
        if isinstance(subj, list):
            total += len(subj)
        else:
            total += 1  # single object or string counts as 1
    return total


rows = []

for split, base_dirs in SPLIT_DIRS.items():
    # choose first existing base dir (allows both test layouts)
    base_dir = next((d for d in base_dirs if os.path.isdir(d)), None)
    if not base_dir:
        print(f"⚠️  Skipping split '{split}' — folder not found.")
        continue

    for doc_type in DOC_TYPES:
        for lang in LANGS:
            lang_dir = os.path.join(base_dir, doc_type, lang)
            if not os.path.isdir(lang_dir):
                continue

            counts = []
            max_file = None
            max_count = -1

            for fname in os.listdir(lang_dir):
                if not fname.endswith(".jsonld"):
                    continue
                fpath = os.path.join(lang_dir, fname)
                cnt = count_subjects_in_file(fpath)
                if cnt is None:
                    continue
                counts.append(cnt)
                if cnt > max_count:
                    max_count = cnt
                    max_file = fname

            if counts:
                mean_rounded = round(mean(counts), 1) if counts else 0.0
                rows.append({
                    "Split": split,
                    "Type": doc_type,
                    "Lang": lang,
                    "Min": min(counts),
                    "Max": max(counts),
                    "Mean": mean_rounded,
                    "MaxFile": max_file
                })

# Save outputs
df = pd.DataFrame(rows).sort_values(["Split", "Type", "Lang"]).reset_index(drop=True)
df.to_csv(CSV_PATH, index=False)
if WRITE_EXCEL_TOO:
    df.to_excel(XLSX_PATH, index=False)

print(f"\n✅ Saved: {CSV_PATH}")
if WRITE_EXCEL_TOO:
    print(f"✅ Saved: {XLSX_PATH}")
