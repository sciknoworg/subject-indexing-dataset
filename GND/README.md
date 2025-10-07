## 🔍 About

The [GND](https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html) (Gemeinsame Normdatei in German or Integrated Authority File in English) is an international authority file primarily used by German-speaking libraries to catalog and link information about people, organizations, topics, and works. As a part of Germany's national library network, TIB also relies on the GND for its subject indexing tasks.

Among the various authority files available in the GND, the only one relevant to subject indexing is the `GND Sachbegriff` file. In English, "Sachbegriff" translates to "subject terms."


## 📂 Repositories Included

- [**how-to**](./how-to): Provides detailed, step-by-step instructions on how to access and download the raw data for the GND *Sachbegriff* (subject term) file from the original source. This guide helps users understand the provenance and structure of the underlying authority data.

- 🌟 [**subjects-taxonomy**](./subjects-taxonomy): **This is the main repository of interest for most researchers.** It contains the fully decoded, human-readable version of the GND subjects taxonomy. These files provide a comprehensive mapping of subject identifiers to their corresponding labels and hierarchical relations, enabling straightforward use in machine learning or knowledge graph applications. *The interested researcher can ignore the other repositories and directly download the GND taxonomy released here.*


- [**scripts**](./scripts): Includes the Python script used to recreate the human-readable GND taxonomy files from the raw *Sachbegriff* data. This script is provided for participants who wish to reproduce the preprocessing workflow, verify the data transformation, or gain a deeper understanding of how the GND taxonomy was converted into its final usable format.
