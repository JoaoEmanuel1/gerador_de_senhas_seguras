from flask import Flask, render_template, request, jsonify
import random
import string

app = Flask(__name__)

def generate_password(length= 12, uppercase= True, lowercase= True, digits= True, special_chars= True):
    characters = ''

    if uppercase:
        characters += string.ascii_uppercase
    
    if lowercase:
        characters += string.ascii_lowercase
    
    if digits:
        characters += string.digits

    if special_chars:
        characters += string.punctuation
    
    if not characters:
        return 'Selecione pelo menos um tipo de caractere!'
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    length = int(data.get('length', 12))
    uppercase = data.get('uppercase', True)
    lowecase = data.get('lowercase', True)
    digits = data.get('digits', True)
    special_chars = data.get('special_chars', True)

    password = generate_password(
        length=length,
        uppercase=uppercase,
        lowercase=lowecase,
        digits=digits,
        special_chars=special_chars
    )

    return jsonify({'password': password})

if __name__ == '__main__':
    app.run(debug=True)