import random
import os
import requests
from flask import Flask, render_template, abort, request

# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor,QuoteModel
from MemeGenerator import MemeEngine

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.path.join('static')

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # TODO: Use the Ingestor class to parse all files in the
    # quote_files variable
    quotes = []

    for quote_file in quote_files:
        quotes.extend(Ingestor.parse(quote_file))

    images_path = "./_data/photos/dog/"

    # TODO: Use the pythons standard library os class to find all
    # images within the images images_path directory
    imgs = []
    for root, dirs, files in os.walk(images_path):
            imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    # @TODO:
    # Use the random python standard library class to:
    # 1. select a random image from imgs array
    # 2. select a random quote from the quotes array

    img = random.choice(imgs)
    quote = random.choice(quotes)
    path1 = meme.make_meme(img, quote.body, quote.author)
    full = os.path.join(app.config['UPLOAD_FOLDER'], path1.split('/')[-1])
    path = full
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # @TODO:
    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.

    img = request.args.get('image_url')
    body = request.args.get('body')
    author = request.args.get('author')

    #print(img,body,author)

    path1 = meme.make_meme(img, body, author)
    full = os.path.join(app.config['UPLOAD_FOLDER'], path1.split('/')[-1])
    path = full

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()