import xml.etree.ElementTree as ET

xml_file = "..\\..\\authorities-gnd-sachbegriff_dnbmarc_20250916.mrc.xml"
ns = "{http://www.loc.gov/MARC21/slim}"

count = 0
for _, elem in ET.iterparse(xml_file, events=("end",)):
    if elem.tag == f"{ns}record":
        count += 1
        elem.clear()

print(f"Total records found: {count}")
