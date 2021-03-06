from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import *
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
import re

# Open a PDF file.
fp = open('D:\pythonData\pdfData\\1\单\全文28篇-单\\32037ZN0401.pdf', 'rb')
# Create a PDF parser object associated with the file object.
parser = PDFParser(fp)
# Create a PDF document object that stores the document structure.
# Supply the password for initialization.
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
document = PDFDocument(parser)

# Process each page contained in the document.
text_content = []
for page in PDFPage.create_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for lt_obj in layout:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine) or isinstance(lt_obj,LTTextBoxHorizontal):
            text_content.append(lt_obj.get_text())
        else:
            pass

# text_content 中每一个元素存储了一行文字
total_text = ''.join(text_content).replace('guide.medlive.cn','').replace('Idiopathic Macular Hole PPP:','').replace('References','')

# 从字符串中解析出参考文献
# file = open("/Users/mfhj-dz-001-068/pythonData/pdf1/1.txt", "w")
m = total_text.rfind("REFERENCES")
print(total_text[m+10:])
p = re.compile(r'^\d+\..*\.$',re.DOTALL)
# p = re.compile(r'.*')
all_items = re.search(p,total_text[m+10:])
print(all_items)
# print(total_text[m:])
# for i in m:
#     # print i
#     if i.startswith("["):
#         file.write(str(i))
#         file.write("\n")
# file.close()


