from abc import ABC,abstractmethod
from .QuoteModel import QuoteModel
from typing import List

class IngestorInterface(ABC):

    allowed = []
    
    @classmethod
    def can_ingest(cls, path):

        ext = path.split('.')[-1]

        return ext in cls.allowed

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
        
    
