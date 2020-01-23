import textract
text = textract.process('DogQuotesPDF1.pdf', method='pdfminer')
print(text)
