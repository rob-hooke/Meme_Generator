from .DocxIngestor import DocxIngestor
from .PDFIngestor import PDFIngestor
from .TextIngestor import TextIngestor
from .CSVIngestor import CSVIngestor
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List



class Ingestor(IngestorInterface):
    

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        ingestors = [DocxIngestor,TextIngestor,CSVIngestor,PDFIngestor]

        for ingest in ingestors:
            if ingest.can_ingest(path):
                return ingest.parse(path)
                
        
    
               
