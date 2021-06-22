# Standard imports
import jwt
from functools import wraps

# Third party imports
from flask import jsonify, request

# Custom imports
from src.main import app
from src.models import User


def token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        """Checks if user has a valid token to access protected routes"""
        token = None

        if 'Authorization' in request.headers:
            bearer = request.headers['Authorization']
            token = bearer.split()[1]
        
        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(public_id = data['public_id']).first()
        except:
            return jsonify({'message': 'Token is invalid'}), 401
        
        return func(current_user, *args, **kwargs)
    
    return decorated
