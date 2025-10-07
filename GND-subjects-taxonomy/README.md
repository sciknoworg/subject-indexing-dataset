## 🔍 About

The [GND](https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html) (Gemeinsame Normdatei in German or Integrated Authority File in English) is an international authority file primarily used by German-speaking libraries to catalog and link information about people, organizations, topics, and works. As a part of Germany's national library network, TIB also relies on the GND for its subject indexing tasks.

Among the various authority files available in the GND, the only one relevant to subject indexing is the `GND Sachbegriff` file. In English, "Sachbegriff" translates to "subject terms."

In addition to the json-Exports of the GND, the German National Library (DNB) has created an **unofficial** Export of the GND from its native raw format into SKOS for the use within this shared Task. These exports are aligned to the other files as a full version with all subject terms (`GND Sachbegriff`) in the file `GND-Subjects-all_dnb-skos.ttl`.

Remarks on the SKOS-Mapping:

  * All Labels are tagged with language code @de, which is not generally true for all entities. There is simply no language tag on record-level in the gnd-native format. 
  * the SKOS-relations broader/ narrower simplfy a system of more then a dozen relation types in the original PICA+ format
  * what information is used to define a SKOS-Collection is disputable. In this export the gnd subject categories, also exported in the JSON-Files in the field `Classification Number`, are used to create the SKOS-Collections. See [the official releases](https://d-nb.info/standards/vocab/gnd/gnd-sc.html) for more information on GND subject categories. 


## 📂 Repositories Included

- [**gnd-how-to**](https://github.com/sciknoworg/subject-indexing-dataset/tree/main/GND-subjects-taxonomy/gnd-how-to): Provides detailed, step-by-step instructions on how to access and download the raw data for the GND *Sachbegriff* (subject term) file from the original source. This guide helps users understand the provenance and structure of the underlying authority data.

- 🌟 [**subjects-taxonomy**](https://github.com/sciknoworg/subject-indexing-dataset/tree/main/GND-subjects-taxonomy/subjects-taxonomy): **This is the main repository of interest for most researchers.** It contains the fully decoded, human-readable version of the GND subjects taxonomy. These files provide a comprehensive mapping of subject identifiers to their corresponding labels and hierarchical relations, enabling straightforward use in machine learning or knowledge graph applications. *The interested researcher can ignore the other repositories and directly download the GND taxonomy released here.*


- [**scripts**](https://github.com/sciknoworg/subject-indexing-dataset/tree/main/GND-subjects-taxonomy/scripts): Includes the Python script used to recreate the human-readable GND taxonomy files from the raw *Sachbegriff* data. This script is provided for participants who wish to reproduce the preprocessing workflow, verify the data transformation, or gain a deeper understanding of how the GND taxonomy was converted into its final usable format.
