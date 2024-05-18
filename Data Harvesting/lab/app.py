from flask import Flask, request, render_template

app = Flask(__name__)

usuarios = [
    {
        'user': 'admin',
        'pwsd': 'admin',
        'messages': []
    }
]
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page/<int:page_id>')
def page(page_id):
    return render_template('page.html', page_id=page_id)


@app.route('/post_message', methods=['POST'])
def post_message():
    username = request.form['username']
    password = request.form['password']

    user = next((x for x in usuarios if x['user'] == username and x['pwsd'] == password), None)

    if user is None:
        return 'Usuario o contraseña incorrecta'
    
    message = request.form['message']
    user['messages'].append(message)
    
    return 'POST: ' + user + ' - ' + pwsd

@app.route('/get_message', methods=['GET'])
def get_message():
    user = request.args.get('user')
    pwsd = request.args.get('pwsd')

    user = next((x for x in usuarios if x['user'] == user and x['pwsd'] == pwsd), None)

    if user is None:
        return 'Usuario o contraseña incorrecta'
    
    messages = user['messages']

    return 'GET: ' + user + ' - ' + messages