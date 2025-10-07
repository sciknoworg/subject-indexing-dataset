# 📚 Welcome to the Subject Indexing Dataset Repository!

## 💡 About

This dataset empowers the research community 🤝 to build advanced LLM-based semantic solutions for automated subject indexing and classification 📑 of technical records from a German national library. The records are mainly in German or English but not limited to these languages. For the subject taxonomy, we rely on the [GND](https://www.dnb.de/EN/Professionell/Standardisierung/GND/gnd_node.html) (Gemeinsame Normdatei / Integrated Authority File), an international authority file widely used by German-speaking libraries to catalog and link information on people, organizations, topics, and works.


## 📂 Repositories Included

To support the development of systems, we release two types of datasets:

- [**GND-subjects-taxonomy**](https://github.com/sciknoworg/subject-indexing-dataset/tree/main/GND-subjects-taxonomy): This subfolder includes the human-readable formatted GND subjects taxonomy. 

- [**technical-records-dataset**](https://github.com/sciknoworg/subject-indexing-dataset/tree/main/technical-records-dataset): This subfolder contains open access annotated technical records as pre-created train/dev/test splits. A large-scale dataset of technical records from a library's open-access collection, annotated with domains and GND subjects, available in both English and German. While the overall collection includes various types of technical records, this dataset is restricted to the most representative five types as follows: `article`, `book`, `conference`, `report`, and `thesis`. 

Both the GND and the open-access records have been reorganized, formatted with human-readable tags, and released as a community dataset for machine learning development. Standardized library taxonomies often rely on age-old identifier codes that are difficult to interpret ⏳. In consultation with subject specialists, we have therefore preprocessed both the taxonomy and the records, converting their fine-grained coding into clear, human-readable formats. This enables researchers to focus on the core machine learning challenge—downloading the data and getting started right away—rather than spending weeks decoding complex formats.

- [**evaluation**](https://github.com/sciknoworg/subject-indexing-dataset/tree/main/evaluation): This subfolder contains the evaluation script with quantitative metrics viz. precision@k, recall@k, f1@k, recall_precision@k, and ndcg@k which are relevant to information retrieval systems and which can be applied to the system predictions when applied to our released gold-standard annotated dataset to get performance scores for subject indexing.

<!-- ## 📧 Contact

llms4subjects [at] gmail.com

## 💡 Citation

The recommended citation for this dataset resource is provided below. If you find this resource useful, please consider citing it.

```bibtex
@InProceedings{dsouza-EtAl:2025:SemEval2025,
author    = {D'Souza, Jennifer and Sadruddin, Sameer and Israel, Holger and Begoin, Mathias and Slawig, Diana},
title     = {SemEval-2025 Task 5: LLMs4Subjects - LLM-based Automated Subject Tagging for a National Technical Library's Open-Access Catalog},
booktitle = {Proceedings of the 19th International Workshop on Semantic Evaluation (SemEval-2025)},
month     = {August},
year      = {2025},
address   = {Vienna, Austria},
publisher = {Association for Computational Linguistics},
pages     = {1082--1095},
url       = {https://aclanthology.org/2025.semeval2025-1.139}
}
```

```bibtex
@misc{D_Souza_The_GermEval_2025_2025,
author = {D'Souza, Jennifer and Sadruddin, Sameer and Israel, Holger and Begoin, Mathias and Slawig, Diana},
doi = {10.5281/zenodo.16743609},
month = mar,
title = {{The GermEval 2025 2nd LLMs4Subjects Shared Task Dataset}},
url = {https://github.com/sciknoworg/llms4subjects},
year = {2025}
}
```

## ⭐ Acknowledgements

The **LLMs4Subjects** shared task, organized as GermEval 2025, is jointly supported by the [SCINEXT project](https://scinext-project.github.io/) (BMBF, German Federal Ministry of Education and Research, Grant ID: 01lS22070) and the [NFDI4DataScience initiative](https://www.nfdi4datascience.de/) (DFG, German Research Foundation, Grant ID: 460234259).
 -->

This work is licensed under a
[Creative Commons Attribution-ShareAlike 4.0 International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg