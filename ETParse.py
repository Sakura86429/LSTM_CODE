import xml.etree.ElementTree as ET
import os

xml_file = "F:\\e_1_1_4_7_0_4_1_5_49_60_0.xml"

with open(xml_file, mode='r', errors='ignore') as f:
    lines = f.readlines()
    f.close()

lines[2] = '    <folder>F</folder>\n'
lines[4]='   <path>none</path>\n'
lines[25] = '        <name>none</name>\n'
with open(xml_file, mode='w', errors='ignore') as f:
    for line in lines:
        f.write(line)
    f.close()

# input_dir='D:\\0.17SUO\\17所\e-两栖登陆舰\SAR\\'
input_dir='D:\\0.17SUO\\17所\\f-护卫舰\SAR\\'

filenames = os.listdir(input_dir)
for filename in filenames:
    if filename.endswith('.xml'):
        path = input_dir+filename
        file_front = filename[:-4]
        with open(path, mode='r', errors='ignore') as f:
            lines = f.readlines()
            f.close()
        lines[2] = '    <folder>F</folder>\n'
        lines[4]='   <path>'+file_front+'</path>\n'
        lines[25] = '        <name>none</name>\n'
        with open(path, mode='w', errors='ignore') as f:
            for line in lines:
                f.write(line)
            f.close()

