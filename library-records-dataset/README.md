# 📑 The **LLMs4Subjects** Shared Task TIBKAT Dataset

## 🔍 About

TIB subject matter experts index the library’s technical records based on the GND subjects taxonomy. Early in the development of TIB's record annotation guidelines, certain GND subject classes were identified as core to TIB’s focus. However, as technical sciences have advanced, TIB records are now annotated with GND subjects that go beyond those original core subject classes.

## 📂 Repositories Included

- [**all-subjects**](https://github.com/sciknoworg/llms4subjects/tree/main/shared-task-datasets/TIBKAT/all-subjects) **dataset:** The `train dataset` contains 90,452 records, `dev dataset` contains 19,949 records and the `test dataset` contains 27,998 records. This dataset is a superset of the dataset linked below and includes all annotated records without restrictions.

For Subtask 1 - Multi-domain Classification, participants are required to use all-subjects dataset, as it encompasses all 28 predefined domains, providing systems with a broader distribution of data records. However, there are some exceptions. Specifically, a small subset of records does not include domain information in its metadata. Out of the 110,401 records in the train and development splits, only 314 records lack domain details. The list of these records can be found [here](all-subjects/data-statistics/Records_without_Domains.json).

For Subtask 2 - Subject Indexing, participants are required to use all-subject dataset for subject indexing.

The dataset folder is organized into two directories: `data`, which contains the actual dataset files, and `data-statistics`, which provides detailed statistical analyses on various aspects of the dataset.

## 🧐 A Guide to Reading TIBKAT Records

Each TIBKAT technical record in the repositories is provided in `json-ld` format. You can view an example English record [here](https://github.com/sciknoworg/llms4subjects/blob/main/shared-task-datasets/TIBKAT/all-subjects/data/train/Article/en/3A1499846525.jsonld) and an example German record [here](https://github.com/sciknoworg/llms4subjects/blob/main/shared-task-datasets/TIBKAT/all-subjects/data/train/Article/de/3A168396733X.jsonld). These files contain various property annotations, with the four most relevant to **LLMs4Subjects** being `title`, `abstract`, `dcterms:subject` and `subject`. Participants are free to use other properties as needed. This guide provides an overview of how to interpret a TIBKAT record, focusing on the `dcterms:subject` and `subject` properties.

### Understanding the Subject Properties

Each TIBKAT technical record contains the properties `subject` and `dcterms:subject`, which describes the domains and topics covered by a given resource. These properties are essential for ensuring that systems perform effectively in both Subtask 1 and Subtask 2.

#### [The TIBKAT Domain Property for Subtask 1 - Multi-domain Classification](#how-to-domains)

The `subject` property includes keywords, phrases, or classification codes that reflect the content. Subject annotations in TIBKAT records are provided by a team of 17 expert subject specialists, covering 28 different subjects, including:

- Architecture, Civil Engineering, Biochemistry, Biology, Chemistry, Chemical Engineering, Electrical Engineering, Energy Technology, Educational Science, Earth Sciences, History, Information Technology, Literary Studies and Linguistics, Mechanical Engineering, Mathematics, Medical Technology, Plant Sciences, Philosophy, Physics, Law, Study of Religions, Social Sciences, Sports Sciences, Theology, Environmental Engineering, Traffic Engineering, Materials Science, and Economics.

For this edition of the shared task and specifically for Subtask 1, only domains related to Fachsystematik LinSearch should be considered. More information about Fachsystematik LinSearch can be found [here](https://terminology.tib.eu/ts/ontologies/linsearch).

#### [The `dcterms:subject` Property for Subtask 2 - Subject Indexing](#how-to-subjects)

The `dcterms:subject` property (often represented as `<dc:subject>` in XML or similar formats) describes the subjects or topics covered by the resource. 

#### How to Read the `dcterms:subject` Property

1. **Access the TIBKAT Record:** Start by accessing the JSON-LD TIBKAT records in the dataset or supplementary dataset folders.

2. **Locate the `dcterms:subject` Property:** Find the `dcterms:subject` property in the record. This property may contain one or more subject headings, each sourced from the GND Sachbegriff (subject headings) taxonomy. More information on GND and its role in TIBKAT can be found in the GND shared task dataset subfolder.

3. **Interpret the Subject Entries:** Each entry under the `dcterms:subject` property represents a subject or topic relevant to the resource. These are typically classification codes from the GND subject headings.

4. **Use the Subjects for Research:** The subject codes listed under the `dcterms:subject` property, when mapped to their corresponding labels, are useful for understanding the focus of the resource, conducting research, or finding related materials in the library catalog.

### Conclusion

Understanding the `dcterms:subject` and `subject` property within TIBKAT records is crucial for researchers, librarians, and anyone working on categorizing or finding resources by subject. By focusing on this property, users can gain insights into the content and relevance of the resources cataloged in the TIBKAT system.

# 📊 Some Statistics for the Dataset

## 🔍 Data Splits Statistics

The table below shows the number of records for each data split and record type:

| Split  | Record Type | Language | Record Count |
|--------|-------------|----------|--------------|
| Train  | Article     | en       | 1,042        |
|        |             | de       | 6            |
|        | Book        | de       | 33,401       |
|        |             | en       | 26,966       |
|        | Conference  | en       | 3,619        |
|        |             | de       | 2,210        |
|        | Report      | de       | 1,507        |
|        |             | en       | 1,275        |
|        | Thesis      | de       | 8,459        |
|        |             | en       | 3,452        |
| Dev    | Article     | en       | 173          |
|        |             | de       | 1            |
|        | Book        | de       | 5,589        |
|        |             | en       | 4,482        |
|        | Conference  | en       | 601          |
|        |             | de       | 371          |
|        | Report      | de       | 256          |
|        |             | en       | 215          |
|        | Thesis      | de       | 1,404        |
|        |             | en       | 574          |
| Test   | Article     | en       | 423          |
|        |             | de       | 1            |
|        | Book        | de       | 13,559       |
|        |             | en       | 7,597        |
|        | Conference  | en       | 808          |
|        |             | de       | 908          |
|        | Report      | de       | 525          |
|        |             | en       | 334          |
|        | Thesis      | de       | 3,006        |
|        |             | en       | 837          |


## 📝 Abstract Statistics

The table below shows the minimum, maximum, and mean length of abstracts in different data splits:

| Split  | Record Type | Language | Min | Max  | Mean  |
|--------|-------------|----------|-----|------|-------|
| Train  | Article     | de       | 22  | 237  | 91.7  |
|        |             | en       | 11  | 626  | 155.8 |
|        | Book        | de       | 8   | 1,776| 143.5 |
|        |             | en       | 1   | 5,101| 174.7 |
|        | Conference  | de       | 7   | 1,217| 144.1 |
|        |             | en       | 13  | 1,617| 168.6 |
|        | Report      | de       | 8   | 884  | 122   |
|        |             | en       | 9   | 901  | 94.3  |
|        | Thesis      | de       | 6   | 2,311| 167.4 |
|        |             | en       | 7   | 1,859| 183.8 |
| Dev    | Article     | de       | 107 | 107  | 107   |
|        |             | en       | 9   | 378  | 155.7 |
|        | Book        | de       | 11  | 1,221| 143.5 |
|        |             | en       | 10  | 1,679| 170.3 |
|        | Conference  | de       | 15  | 778  | 145.3 |
|        |             | en       | 18  | 1,298| 165.4 |
|        | Report      | de       | 10  | 394  | 114.3 |
|        |             | en       | 8   | 534  | 93.7  |
|        | Thesis      | de       | 8   | 3,325| 170.5 |
|        |             | en       | 8   | 1,133| 185.9 |
| Test   | Article     | de       | 186 | 186  | 186   |
|        |             | en       | 16  | 513  | 155.8 |
|        | Book        | de       | 8   | 1,731| 137.1 |
|        |             | en       | 11  | 2,115| 172.2 |
|        | Conference  | de       | 10  | 808  | 141.9 |
|        |             | en       | 17  | 1,773| 175.0 |
|        | Report      | de       | 10  | 551  | 119.2 |
|        |             | en       | 11  | 829  | 99.4  |
|        | Thesis      | de       | 6   | 1,705| 156.4 |
|        |             | en       | 6   | 1,646| 183.4 |

## TIBKAT Record Domain's Statistics

The table below presents the minimum, maximum, and average number of domains per record in the all-subjects data collection for **Subtask 1 – TIBKAT Multi-Domain Classification**:

| Split  | Record Type | Language | Min | Max | Mean |
|--------|-------------|----------|-----|-----|------|
| Train  | Article     | de       | 1   | 3   | 1.7  |
|        |             | en       | 1   | 4   | 1.4  |
|        | Book        | de       | 1   | 6   | 1.5  |
|        |             | en       | 1   | 6   | 1.4  |
|        | Conference  | de       | 1   | 5   | 1.4  |
|        |             | en       | 1   | 4   | 1.3  |
|        | Report      | de       | 1   | 5   | 1.5  |
|        |             | en       | 1   | 6   | 1.5  |
|        | Thesis      | de       | 1   | 6   | 1.4  |
|        |             | en       | 1   | 6   | 1.4  |
| Dev    | Article     | de       | 1   | 3   | 2    |
|        |             | en       | 1   | 4   | 1.4  |
|        | Book        | de       | 1   | 5   | 1.5  |
|        |             | en       | 1   | 5   | 1.4  |
|        | Conference  | de       | 1   | 5   | 1.5  |
|        |             | en       | 1   | 4   | 1.3  |
|        | Report      | de       | 1   | 4   | 1.5  |
|        |             | en       | 1   | 4   | 1.5  |
|        | Thesis      | de       | 1   | 4   | 1.4  |
|        |             | en       | 1   | 7   | 1.4  |
| Test   | Article     | de       | 2   | 2   | 2    |
|        |             | en       | 1   | 4   | 1.5  |
|        | Book        | de       | 1   | 7   | 1.4  |
|        |             | en       | 1   | 5   | 1.4  |
|        | Conference  | de       | 1   | 5   | 1.4  |
|        |             | en       | 1   | 5   | 1.4  |
|        | Report      | de       | 1   | 4   | 1.5  |
|        |             | en       | 1   | 4   | 1.5  |
|        | Thesis      | de       | 1   | 6   | 1.4  |
|        |             | en       | 1   | 3   | 1.3  |

For more insights into dataset statistics, visit the `data-statistics` subfolder. The dataset can be downloaded from the `data` subfolder.
