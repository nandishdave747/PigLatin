
from flask import Flask, render_template, request, url_for

# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return "Flask is running"

# Define a POST request to accept paragraph and return Pig Latin.

@app.route('/piglatin/', methods=['POST'])
def hello():
    paragraph=request.form['data']
    print paragraph
    words = paragraph.split(" ")
    vowels = ["a","i","e","o","u"]
    output = []
    for word in words:
        for i in range(len(word)):
            if word[0] in vowels or word[0].lower() in vowels:
                print word + "yay"
                output.append(word + "yay")
                break
            chr = word[i]
            if chr in vowels:
                print word[i:]+word[:i]+"ay"
                output.append(word[i:]+word[:i]+"ay")
                break
    print output
    return " ".join(output)

# Run the app
if __name__ == '__main__':
    app.run(
            host="0.0.0.0",
            port=int("80")
            )





