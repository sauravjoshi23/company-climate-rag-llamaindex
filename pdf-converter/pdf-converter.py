from flask import Flask, render_template_string

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Company Newsletter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
        }
        .newsletter {
            width: 60%;
            background-color: white;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .header {
            background-color: #7B4B94; /* Purple color for header */
            color: white; /* White text color */
            padding: 10px;
            text-align: center;
        }
        .section {
            margin-top: 20px;
            border-left: 5px solid #7B4B94; /* Purple border for sections */
            padding-left: 10px;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            background-color: #7B4B94; /* Purple background for footer */
            color: white; /* White text color */
            padding: 10px;
        }
        h1, h2 {
            color: #7B4B94; /* Purple text color for headings */
        }
        ul {
            padding: 0;
            list-style-position: inside;
        }
        li {
            padding: 2px 0;
        }
    </style>
</head>
<body>
    <div class="newsletter">
        <div class="header">
            <h1>COMPANY</h1>
            <p>The most extroverted news you'll find.</p>
        </div>
        <div class="section">
            <h2>Summary</h2>
            <p>{{ summary }}</p>
        </div>
        <div class="section">
            <h2>Good for Climate</h2>
            <p>{{ good_for_climate }}</p>
        </div>
        <div class="section">
            <h2>Bad for Climate</h2>
            <ul>
                {% for item in bad_for_climate %}
                    <li>{{ item }}</li>
                {% endfor %}
            </ul>
        </div>
        <div class="footer">
            <p>Follow us for more @social_news</p>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def newsletter():
    # These would be your dynamic strings you want to inject into the HTML
    summary = "Today we're discussing the best vegan recipes..."
    good_for_climate = "Ever feel bad for turning down invites?..."
    bad_for_climate = [
        "go on a walk",
        "remember that challenging times will pass",
        "listen carefully",
        "identify points of agreement and disagreement",
        "create a culture of positivity"
    ]
    
    return render_template_string(
        TEMPLATE,
        summary=summary,
        good_for_climate=good_for_climate,
        bad_for_climate=bad_for_climate
    )

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change the port if needed
