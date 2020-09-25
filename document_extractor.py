# import time
# st_time = time.time()
import PyPDF2
import re
import sys
import os
# import docx
import docx2txt
import argparse 



valid_file_extensions = [".pdf",".doc",".docx"]

class DocumentExtractor():
    def __init__(self):
        self.stopwords = self.load_stopwords("stopwords.txt")
        self.cleaning_regex = r"[-()\"#/;:<>{}=~|?,\n]"
        return
    
    def extract_document(self,file_path, raw=False):
        filename, file_extension = os.path.splitext(file_path)
        if file_extension not in valid_file_extensions:
            return 0
        extractor = self.fetch_extractor(file_extension)
        raw_text = extractor(file_path)
        if raw:
            return raw_text
        raw_text = self.regex_clean(raw_text)
        stopwords_removed = self.remove_stopwods(raw_text)
        return stopwords_removed

    def fetch_extractor(self,ext):
        if ext == ".pdf":
            return self.extract_pdf
        if  ext == ".docx":
            return self.extract_docx
        if ext == ".doc":
            return self.extract_doc

    def load_stopwords(self,stopwords_path):
        f = open(stopwords_path,'r')
        stopwords = []
        for l in f:
            stopwords.append(l.replace("\n",""))
        return stopwords

    def remove_stopwods(self,text):
        text = ' '.join([word for word in text.split() if word not in self.stopwords])
        return text

    def regex_clean(self,text):
        return re.sub(self.cleaning_regex, "", text).strip()

    def extract_pdf(self,file_path):

        pdfFileObj = open(file_path, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)  
        text = ""
        for i in range(pdfReader.numPages):
            pageObj = pdfReader.getPage(0)  
            text = text + pageObj.extractText()
        return text

    # def extract_docx_v0(self,file_path):
    #     doc = docx.Document(file_path)
    #     all_paras = doc.paragraphs
    #     text = ""
    #     for para in all_paras:
    #         text = text + para.text

    #     # text = self.regex_clean(text)
    #     return text

    def extract_docx(self,file_path):
        text =  docx2txt.process(file_path)
        return text

    def extract_doc(self,file_path):
        return 0
        # import textract

        # text = textract.process(file_path)
        # text = text.decode("utf-8") 
        # return tmpText

        
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--Path", help = "File Path")
    parser.add_argument("-r", "--Raw", type=int, choices=[0, 1], default=0, 
                        help = "Return Clean Text")
    args = parser.parse_args()
    file_path = args.Path
    DE = DocumentExtractor()
    # print(args.Clean)
    print(DE.extract_document(file_path,args.Raw))
    # print(time.time()-st_time)
    