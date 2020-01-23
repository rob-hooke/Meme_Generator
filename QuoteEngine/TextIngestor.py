from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel
from typing import List

class TextIngestor(IngestorInterface):

    allowed = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:

        if cls.can_ingest(path):

            with open(path) as f:
                data = f.readlines()
                
            temp = []
            
            for line in data:
                parsed = line.split('-')
                if len(parsed) == 2:
                    new = QuoteModel(parsed[0],parsed[1])
                    temp.append(new)

            return temp

