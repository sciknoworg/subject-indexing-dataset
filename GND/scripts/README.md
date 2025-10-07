## 📘 Formatted Human-Readable GND Subject Terms (Sachbegriff)

This folder contains scripts and files for converting the GND *Sachbegriff* (subject terms) from the MARC 21 XML format into a structured, human-readable JSON format.

### 🔖 GND Subject Classification

All GND subjects are categorized by concept type. The official classification list is available in this [PDF](https://wiki.dnb.de/download/attachments/90411323/gndSyst.pdf).  
A preprocessed [JSON file](../subjects-taxonomy/GND-subjects-classification.json) provides these categories with their names and indicators for whether each subject is part of the TIB Core list.

### ⚙️ Workflow

Use [`subject_gnd_formatting.py`](subject_gnd_formatting.py) to generate the human-readable formatted JSON taxonomy.

1. **Schema definition**  
   The [schema.json](../subjects-taxonomy/schema.json) file specifies the structure of each subject entry. Not all attributes appear in every record; missing fields are simply omitted.

2. **Set input paths**  
   Update the script to point to your local MARC 21 XML source and the GND classification JSON:
   ```python
   subject_gnd_filepath = '../authorities-gnd-sachbegriff_dnbmarc_yyyymmdd.mrc.xml'
   gnd_subjects = read_json_file('../subjects-taxonomy/GND-subjects-classification.json')
   ```

3. **Run the conversion**
   ```bash
   python subject_gnd_formatting.py
   ```
   This will produce a human-readable JSON file of GND subjects ready for machine learning or semantic processing.