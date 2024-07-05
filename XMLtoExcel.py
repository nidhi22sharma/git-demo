from lxml import etree
import openpyxl
from openpyxl.styles import PatternFill
import os
import pandas as pd

def parse_xml_to_excel_no_ns(xml_file, tag_names):
    try:
        parser = etree.XMLParser(ns_clean=True, recover=True)
        tree = etree.parse(xml_file, parser)
    except etree.XMLSyntaxError as e:
        print(f"Failed to parse XML: {e}")
        return

    root = tree.getroot()
    print(f"Root tag: {root.tag}")

    def strip_prefix(tag):
        return tag.split('}', 1)[-1] if '}' in tag else tag.split(':')[-1]

    stripped_tag_names = [strip_prefix(tag) for tag in tag_names]

    for stripped_tag_name in stripped_tag_names:
        elements = [elem for elem in root.iter() if strip_prefix(elem.tag) == stripped_tag_name]
        print(f"Found {len(elements)} elements for tag: {stripped_tag_name}")

        if not elements:
            print(f"No elements found for tag: {stripped_tag_name}")
            continue

        for element in elements:
            obs_elements = [elem for elem in element.iter() if strip_prefix(elem.tag) == 'obs']
            print(f"Found {len(obs_elements)} obs elements in {stripped_tag_name}")

            if not obs_elements:
                print(f"No obs elements found in {stripped_tag_name}")
                continue

            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = stripped_tag_name

            headers = set()
            rows = []

            for obs in obs_elements:
                row = {}
                for attr, value in obs.attrib.items():
                    headers.add(attr)
                    if value == 'null':
                        row[attr] = None
                    else:
                        try:
                            row[attr] = int(value)
                        except ValueError:
                            try:
                                row[attr] = float(value)
                            except ValueError:
                                row[attr] = value

                rows.append(row)

            headers = list(headers)
            ws.append(headers)

            for row in rows:
                row_data = [row.get(header, '') for header in headers]
                ws.append(row_data)

            for col in ws.columns:
                max_length = 0
                column = col[0].column_letter
                for cell in col:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = len(cell.value)
                    except:
                        pass
                adjusted_width = (max_length + 2)
                ws.column_dimensions[column].width = adjusted_width

            for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=len(headers)):
                for cell in row:
                    if cell.value is None:
                        cell.fill = PatternFill(start_color="FFFF0000", end_color="FFFF0000", fill_type="solid")

            file_name = f'/mnt/data/{stripped_tag_name}.xlsx'
            if os.path.exists(file_name):
                print(f"File {file_name} already exists and will be overwritten.")
            try:
                wb.save(file_name)
                print(f"Excel file saved: {file_name}")
            except Exception as e:
                print(f"Failed to save Excel file for {stripped_tag_name}: {e}")

# New XML data without namespaces
xml_data_finan_no_ns = '''<t2:finan>
    <t2:obs empid="111" sty="T2m" value1="123.88" value2="null" />
    <t2:obs empid="112" sty="T4Y" value1="4333" value2="789" />
</t2:finan>'''

# Write the new XML data to a file for parsing
xml_file_path_finan_no_ns = '/mnt/data/sample_finan_no_ns.xml'
with open(xml_file_path_finan_no_ns, 'w') as file:
    file.write(xml_data_finan_no_ns)

# Usage example with the new XML data and different tag
xml_file = xml_file_path_finan_no_ns  # Path to the new XML file
tag_names = ['t2:finan']  # Tag to search for

parse_xml_to_excel_no_ns(xml_file, tag_names)

# Reading the generated Excel files into DataFrames
try:
    finan_df = pd.read_excel('/mnt/data/finan.xlsx')
    finan_df
except FileNotFoundError:
    print("The Excel file was not created.")
