# Document Extractor
Extract text from pdf or word documents

## Usage
Install the required libraries using "pip install -r requirements.txt"  

Execution :  
python document_extractor.py -p "/Path/to/File" -r 1

## Abilities
Extracts text content from PDF, DOCX and DOC files.  
Raw Flag:  
0 - returns cleaned text by removing stopwords and applying cleaning regex  
1 - return raw extracted content  
