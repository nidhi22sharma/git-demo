

import xml.etree.ElementTree as ET
import openpyxl
from openpyxl.styles import PatternFill
import os

def parse_xml_to_excel(xml_file, tag_names):
    try:
        tree = ET.parse(xml_file)
    except ET.ParseError as e:
        print(f"Failed to parse XML: {e}")
        return

    root = tree.getroot()

    def get_all_namespaces(elem):
        namespaces = dict([
            node for _, node in ET.iterparse(
                elem, events=['start-ns']
            )
        ])
        return namespaces

    with open(xml_file, 'r') as file:
        namespaces = get_all_namespaces(file)

    for tag_name in tag_names:
        elements = []
        for ns_prefix, ns_uri in namespaces.items():
            elements.extend(root.findall(f'.//{{{ns_uri}}}{tag_name}'))

        if not elements:
            print(f"No elements found for tag: {tag_name}")
            continue

        for element in elements:
            obs_elements = []
            for ns_prefix, ns_uri in namespaces.items():
                obs_elements.extend(element.findall(f'.//{{{ns_uri}}}obs'))

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

                for child in obs:
                    headers.add(child.tag)
                    if child.text == 'null':
                        row[child.tag] = None
                    else:
                        try:
                            row[child.tag] = int(child.text)
                        except ValueError:
                            try:
                                row[child.tag] = float(child.text)
                            except ValueError:
                                row[child.tag] = child.text

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

            file_name = f'{tag_name}.xlsx'
            if os.path.exists(file_name):
                print(f"File {file_name} already exists and will be overwritten.")
            try:
                wb.save(file_name)
                print(f"Excel file saved: {file_name}")
            except Exception as e:
                print(f"Failed to save Excel file for {tag_name}: {e}")


xml_file = 'path_to_your_xml_file.xml'  # Provide xml path
tag_names = ['inst', 'finan', 'emp']  # Provide list of tags here

parse_xml_to_excel(xml_file, tag_names)
