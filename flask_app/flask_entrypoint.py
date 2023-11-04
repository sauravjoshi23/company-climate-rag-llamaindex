# import requirements needed
from flask import Flask, Response, render_template, request, send_file

# TODO: PROBABLY REMOVE
import io
import requests as req_lib

from utils import get_base_url

# setup the webserver
# port may need to be changed if there are multiple flask servers running on same server
port = 12346
base_url = get_base_url(port)

# if the base url is not empty, then the server is running in development, and we need to specify the static folder so that the static files are served
if base_url == '/':
    app = Flask(__name__)

# set up the routes and logic for the webserver
@app.route(f'{base_url}')
def home():
    return render_template('index.html')

@app.route("/getScorecard", methods=["GET", "POST"])
def getScorecard():
    if request.method == 'POST':
        # TODO: GET PDF FROM COMPANY NAME WITH LLAMA INDEX HERE
        # return Response(request.form.get('company_input'))

        # TMP CODE
        r = req_lib.get('https://arxiv.org/pdf/2212.10543.pdf', allow_redirects=True)
        return send_file(
                     io.BytesIO(r.content),
                     attachment_filename='report.pdf',
                     mimetype='application/pdf')
    else:
        return Response("INVALID REQUEST")

if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    # website_url = 'cocalc4.ai-camp.org'
    website_url = f'http://localhost:{port}'
    
    print(f'Try to open\n\n    {website_url}' + base_url + '\n\n')
    app.run(host = '0.0.0.0', port=port, debug=True)