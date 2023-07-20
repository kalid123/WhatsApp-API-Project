from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    text = request.form.get('text')
    file = request.files.get('file')
    if text:
        # Process the text submission
        print(f'Text: {text}')
    if file:
        # Process the file attachment
        file.save(file.filename)
        print(f'File: {file.filename}')
    return 'Form submitted successfully!'

if __name__ == '__main__':
    app.run(debug=True)
