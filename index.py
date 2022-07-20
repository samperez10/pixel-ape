import requests as req,json

from flask import Flask , jsonify ,request, send_file , render_template

  
app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    
    return "Pixel Ape Not Found", 404
    
@app.route("/metadata/<id>")
def metadata(id):
  
  url = f"https://bafybeiebbjeolsgnoodqokcvwtlgzxly25jqpdn533m4dyzy7szgrdnfka.ipfs.nftstorage.link/{id}.json"
  
  js = req.get(url).json()

  js['description'] = f'A collection of 2,222 NFTs living in chaos under Polygon Blockchain.'
  
  return jsonify(js)


@app.route("/")
def home():
  
  return 'Pixel Apes Homepage'


  