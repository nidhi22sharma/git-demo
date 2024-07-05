from lxml import etree
import openpyxl
from openpyxl.styles import PatternFill
import os
import pandas as pd

def parse_xml_to_excel(xml_file, tag_names):
    try:
        parser = etree.XMLParser(ns_clean=True, recover=True)
        tree = etree.parse(xml_file, parser)
    except etree.XMLSyntaxError as e:
        print(f"Failed to parse XML: {e}")
        return

    root = tree.getroot()

    for tag_name in tag_names:
        elements = root.xpath(f'//*[local-name()="{tag_name}"]')

        if not elements:
            print(f"No elements found for tag: {tag_name}")
            continue

        for element in elements:
            obs_elements = element.xpath('.//*[local-name()="obs"]')

            if not obs_elements:
                print(f"No obs elements found in {tag_name}")
                continue

            wb = openpyxl.Workbook()
            ws = wb.active
            ws.title = tag_name

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

            file_name = f'/mnt/data/{tag_name}.xlsx'
            if os.path.exists(file_name):
                print(f"File {file_name} already exists and will be overwritten.")
            try:
                wb.save(file_name)
                print(f"Excel file saved: {file_name}")
            except Exception as e:
                print(f"Failed to save Excel file for {tag_name}: {e}")

# Sample XML data
xml_data = '''<t1:main_ag xmlns:t1="some_namespace" xmlns:t2="some_other_namespace">
    <t1:structure>
        <t1:inst>
            <t1:obs id="222" typ="gg" value1="123" value2="null" />
            <t1:obs id="221" typ="gg" value1="456" value2="789" />
        </t1:inst>
        <t2:finan>
            <t1:obs empid="111" sty="T2m" value1="123.88" value2="null" />
            <t1:obs empid="112" sty="T4Y" value1="4333" value2="789" />
        </t2:finan>
        <t2:emp>
            <t1:obs empid="1" pt="G5" value1="123.88" value2="null" />
            <t1:obs empid="2" pt="44" value1="4333" value2="789" />
        </t2:emp>
    </t1:structure>
</t1:main_ag>'''

# Writing XML data to a file for parsing
with open('/mnt/data/sample.xml', 'w') as file:
    file.write(xml_data)

# Usage example
xml_file = '/mnt/data/sample.xml'  # Path to the XML file
tag_names = ['inst']  # Tags to search for

parse_xml_to_excel(xml_file, tag_names)

# Reading the generated Excel files into DataFrames
inst_df = pd.read_excel('/mnt/data/inst.xlsx')
inst_df
