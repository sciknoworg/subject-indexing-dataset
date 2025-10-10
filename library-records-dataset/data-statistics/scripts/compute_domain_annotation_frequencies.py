import os
import sys
import json
import math
import pandas as pd
from statistics import mean

# ---------- CONFIG ----------
DOC_TYPES = ["Article", "Book", "Conference", "Report", "Thesis"]
LANGS = ["en", "de"]
DOMAIN_PREFIX = "(classificationName=linsearch:mapping)"
DEFAULT_CSV_NAME = "domain_annotation_frequencies.csv"
DEFAULT_XLSX_NAME = "domain_annotation_frequencies.xlsx"
WRITE_EXCEL_TOO = False  # change to True if you also want XLSX
# ---------------------------


def get_folder_input(prompt_text, default=None):
    """Prompt user for a folder path with optional default fallback."""
    if len(sys.argv) > 1 and prompt_text.startswith("Enter the path to your data"):
        # first argument used for data folder if provided
        path = sys.argv[1]
        print(f"Using data folder from argument: {path}")
        return path
    path = input(prompt_text).strip()
    if not path and default:
        return default
    return path


# --- Ask for user inputs ---
ROOT = get_folder_input("Enter the path to your data folder (e.g., ./library-records-dataset/data): ")
if not os.path.isdir(ROOT):
    raise ValueError(f"❌ The provided data folder does not exist: {ROOT}")

OUTPUT_DIR = get_folder_input("Enter output directory (press Enter to use current working directory): ",
                              os.getcwd())
if not os.path.isdir(OUTPUT_DIR):
    raise ValueError(f"❌ The provided output directory does not exist: {OUTPUT_DIR}")

# Map split names to physical paths
SPLIT_DIRS = {
    "train": [os.path.join(ROOT, "train")],
    "dev": [os.path.join(ROOT, "dev")],
    "test": [os.path.join(ROOT, "test", "gold-standard-testset"),
             os.path.join(ROOT, "test")],
}


def count_domain_subjects_in_file(path: str) -> int | None:
    """Count how many 'subject' entries begin with the domain prefix."""
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return None

    total = 0
    graph = data.get("@graph", [])
    if not isinstance(graph, list):
        return 0

    for item in graph:
        subj = item.get("subject")
        if subj is None:
            continue
        if isinstance(subj, list):
            total += sum(1 for s in subj if isinstance(s, str) and s.startswith(DOMAIN_PREFIX))
        elif isinstance(subj, str) and subj.startswith(DOMAIN_PREFIX):
            total += 1
    return total


rows = []

for split, base_dirs in SPLIT_DIRS.items():
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
                cnt = count_domain_subjects_in_file(fpath)
                if cnt is None:
                    continue
                counts.append(cnt)
                if cnt > max_count:
                    max_count = cnt
                    max_file = fname

            if counts:
                non_zero_counts = [c for c in counts if c > 0]
                min_value = min(non_zero_counts) if non_zero_counts else 0
                mean_rounded = round(mean(counts), 1) if counts else 0.0

                rows.append({
                    "Split": split,
                    "Type": doc_type,
                    "Lang": lang,
                    "Min": min_value,
                    "Max": max(counts),
                    "Mean": mean_rounded,
                    "MaxFile": max_file
                })

# Create output DataFrame
df = pd.DataFrame(rows).sort_values(["Split", "Type", "Lang"]).reset_index(drop=True)

# Build output paths
csv_path = os.path.join(OUTPUT_DIR, DEFAULT_CSV_NAME)
xlsx_path = os.path.join(OUTPUT_DIR, DEFAULT_XLSX_NAME)

# Save files
df.to_csv(csv_path, index=False)
if WRITE_EXCEL_TOO:
    df.to_excel(xlsx_path, index=False)

print(f"\n✅ Saved CSV: {csv_path}")
if WRITE_EXCEL_TOO:
    print(f"✅ Saved Excel: {xlsx_path}")
