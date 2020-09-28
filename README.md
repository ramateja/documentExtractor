# Document Extractor
Extract text from pdf or word documents

## Usage
Install the required libraries using "pip install -r requirements.txt"  

Execution :  
python document_extractor.py -p "/Path/to/File" -r 1 -s 1  


## Abilities
Extracts text content from PDF, DOCX and DOC files.  
Raw Flag:  
0 - returns cleaned text by removing stopwords and applying cleaning regex  
1 - return raw extracted content  

Save Text Flag:
0 - Won't save any file
1 - Will Save .txt with raw content in the same location as original file.



## Default  
Raw is set to 0 and Save is set to 1.
By executing $ python document_extractor.py -p "/Path/to/File"  
It returns cleaned text and Saves Raw to text file

## Limitations
DOC file extraction is through textract library which is only available in Linux  
It uses antiword for internal processing which needs to be installed through apt