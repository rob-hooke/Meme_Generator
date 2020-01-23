
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
import pandas as pd
from typing import List

class CSVIngestor(IngestorInterface):

    allowed = ['csv']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:

        if cls.can_ingest(path):

            df = pd.read_csv(path)

            temp = []
            data = df.values.tolist()

            for row in data:
                body, author = row[0], row[1]
                new = QuoteModel(body,author)
                temp.append(new)

            return temp
        
        
    
