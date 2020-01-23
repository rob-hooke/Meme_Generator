from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List
import subprocess
import random
import os
import PyPDF2



class PDFIngestor(IngestorInterface):

    allowed = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:

        if cls.can_ingest(path):

            temp = []          
            pdfFileObj = open(path, 'rb') 
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj) 
            pageObj = pdfReader.getPage(0) 
            texts = pageObj.extractText().split('\n')
            final = [x for x in texts if '-' in x]
            for val in final:
                parsed = val.split('-')
                new = QuoteModel(parsed[0],parsed[1])
                temp.append(new) 
              
            
            pdfFileObj.close()
            return temp

            '''
            try:
                os.mkdir('/tmp')
            except:
                pass

            tmp = f'/tmp/{random.randint(0,10000000)}.txt'
            #print(f'*****{path}')
            #path = 'DogQuotesPDF.pdf'
            call = subprocess.call(['pdftotext',path,tmp],shell=True)
            call_status = call.wait()
            
            file_ref = open(tmp, "r")
            temp = []
            for line in file_ref.readlines():
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    parsed = line.split('-')
                    new = QuoteModel(parsed[0],parsed[1])
                    temp.append(new)

            file_ref.close()
            #os.remove(tmp)
            return temp

            '''
