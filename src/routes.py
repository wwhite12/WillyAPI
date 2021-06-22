# Standard imports
import jwt
import uuid
from datetime import datetime, timedelta
from werkzeug.security import generate_password_hash, check_password_hash

# Third party imports
from flask import jsonify, make_response, request

# Custom imports
from src.main import app, db
from src.auth import token_required
from src.models import User, Insults, Funfacts


@app.route('/', methods=['GET'])
def welcome_message():

    return jsonify({
        'message': 'Welcome to WillyAPI!',
        'instructions': 'If you are new to this API please read the documentation'
    }), 200


@app.route('/signup', methods=['POST'])
def signup_for_api():
    """add credentials to DB"""
    data = request.form

    name, email = data.get('name'), data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()

    if not user:
        user = User(
            public_id = str(uuid.uuid4()),
            name = name,
            email = email,
            password = generate_password_hash(password)
        )

        db.session.add(user)
        db.session.commit()

        return make_response('Successfully Registered', 200)

    else:
        return make_response('User already exists, please sign in', 200)


@app.route('/login', methods=['POST'])
def get_token():
    """get token"""
    auth = request.form

    if not auth or not auth.get('email') or not auth.get('password'):
        return make_response(jsonify({'error': 'Could not verify. Missing email or password'}), 400)

    user = User.query.filter_by(email=auth.get('email')).first()

    if not user:
        return jsonify({
            'error': 'Could not find user email address'
        }), 400

    if check_password_hash(user.password, auth.get('password')):
        token = jwt.encode({
            'public_id': user.public_id,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])

        return make_response(jsonify({
            'token': token.decode('UTF-8'),
            'message': f'Welcome {user.name}, this token expires in 30 minutes!'
            }), 200)

    return make_response('Incorrect Password', 401)


@app.route('/insults', methods=['GET', 'POST'])
@token_required
def insults(current_user):
    """Show insults or post a new one"""
    if request.method == 'GET':
        insults = Insults.query.all()

        output = []

        for insult in insults:
            output.append({
                'insult': insult.insult,
                'submitted_by': insult.user
            })
        
        return jsonify({
            'insults': output
        }), 200

    if request.method == 'POST':
        data = request.data

        insult = Insults(
            insult = data,
            user = current_user.name
        )

        db.session.add(insult)
        db.session.commit()

        return make_response(f'Thanks {current_user.name}! Your insult has been submitted!')


@app.route('/fun_facts', methods=['GET', 'POST'])
@token_required
def show_gym_stats(current_user):
    """Show fun facts"""
    if request.method == 'GET':
        facts = Funfacts.query.all()

        output = []

        for fact in facts:
            output.append({
                f'Fun Fact#{fact.id}': fact.fact
            })

        return jsonify({
            'Fun Facts': output
        }), 200
