# import requirements needed
from flask import Flask, Response, render_template, request, send_file

from utils import get_base_url
from data_retriever import *

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
        company_name = request.form.get('company_input')
        if not company_name:
            return Response("No input")
        sc_data = data_retriever(company_name)
        print(sc_data)
        # sc_data = {
        #     'summary': "Today we're discussing the best vegan recipes...Ian",
        #     'good_for_climate': "Ever feel bad for turning down invites?...",
        #     'bad_for_climate': [
        #         "go on a walk",
        #         "remember that challenging times will pass",
        #         "listen carefully",
        #         "identify points of agreement and disagreement",
        #         "create a culture of positivity"
        #     ]
        # }
        if sc_data is None:
            return Response("Company not found")

        return render_template(
            'report.html',
            company_name=request.form.get('company_input'),
            summary=sc_data['summary'],
            good_for_climate=sc_data['good_for_climate'],
            bad_for_climate=sc_data['bad_for_climate']
        )
    else:
        return Response("INVALID REQUEST")

if __name__ == '__main__':
    # IMPORTANT: change url to the site where you are editing this file.
    # website_url = 'cocalc4.ai-camp.org'
    website_url = f'http://localhost:{port}'
    
    print(f'Try to open\n\n    {website_url}' + base_url + '\n\n')
    app.run(host = '0.0.0.0', port=port, debug=True)