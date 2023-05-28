# Designed by Prakash Srinivasan ( prarvy@gmail.com )
# Project Name: XML Reader
# Version: 1.0: Base version by author
import xml.etree.ElementTree

key_names = ["company", "last", "change", "min", "max"]
key_widths = [40, 10, 8, 10, 10]


class XMLReader:
    def __init__(self, nyse_xml_data):
        self.nyse_xml_data = nyse_xml_data

    # Read XML Data
    def read_xml(self):
        self.show_header()
        for item in self.nyse_xml_data.findall('quote'):
            if item.tag == 'quote':
                item.attrib['company'] = item.text
                self.show_data(item.attrib)

    # Display Header
    @staticmethod
    def show_header():
        for (n, w) in zip(key_names, key_widths):
            if n == 'company':
                print(n.ljust(w).upper(), end='| ')
            else:
                print(n.rjust(w).upper(), end='| ')
        print()
        print('-' * 87)

    # Display Records
    @staticmethod
    def show_data(car):
        for (n, w) in zip(key_names, key_widths):
            if n == 'company':
                print(str(car[n]).ljust(w), end='| ')
            else:
                print(str(car[n]).rjust(w), end='| ')
        print()


if __name__ == '__main__':
    nyse_data = None
    try:
        nyse_data = xml.etree.ElementTree.parse('nyse.xml').getroot()
        xml_data = XMLReader(nyse_data)
        XMLReader.read_xml(xml_data)
    except FileNotFoundError:
        print('Error: XML File not found.')
    except xml.etree.ElementTree.ParseError:
        print('Error: Parsing error in XML file.')
