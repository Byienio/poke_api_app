from flask import Blueprint, jsonify, render_template, request, Response
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import db, User
from app.services.data_fetcher import fetch_pokemon_data, save_pokemon_data
from app.services.analysis import *
from dicttoxml import dicttoxml

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    hashed_pw = generate_password_hash(data['password'])
    user = User(username=data['username'], password=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return jsonify(message="User registered")

@main_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity=user.username)
        return jsonify(access_token=access_token)
    return jsonify(message="Invalid credentials"), 401

@main_bp.route('/fetch-pokemon', methods=['GET'])
@jwt_required()
def fetch_and_store():
    data = fetch_pokemon_data()
    save_pokemon_data(data)
    return jsonify({"status": "success"})

@main_bp.route('/analysis/<analysis_type>', methods=['GET'])
def analysis(analysis_type):
    data = get_analysis_data(analysis_type)
    if data is None:
        return jsonify(message="Invalid analysis type"), 400
    return render_template('analysis.html', analysis_type=analysis_type, data=data)

@main_bp.route('/export/<analysis_type>/<format>', methods=['GET'])

def export_analysis(analysis_type, format):
    data = get_analysis_data(analysis_type)
    if data is None:
        return jsonify(message="Invalid analysis type"), 400

    if format == 'json':
        return jsonify(data)
    elif format == 'xml':
        xml = dicttoxml(data, custom_root='analysis', attr_type=False)
        return Response(xml, mimetype='application/xml')
    else:
        return jsonify(message="Invalid format"), 400

def get_analysis_data(analysis_type):
    if analysis_type == 'avg_stats_by_type':
        return analyze_types()
    elif analysis_type == 'top_overall_stats':
        return top_overall_stat()
    elif analysis_type == 'avg_experience_by_type':
        return average_experience_by_type()
    elif analysis_type == 'tallest_heaviest_by_type':
        return tallest_and_heaviest_by_type()
    elif analysis_type == 'type_distribution':
        return type_distribution()
    elif analysis_type == 'stat_range_by_type':
        return stat_range_by_type()
    return None

@main_bp.route('/charts')
def charts():
    data = type_distribution()  # lub inna funkcja analizy
    chart_data = {
        "labels": list(data.keys()),
        "data": list(data.values()),
        "label": "Rozkład typów"
    }
    return render_template('charts.html', chart_data=chart_data)

@main_bp.route('/export/json')
def export_json():
    pokemons = Pokemon.query.all()
    data = [p.__dict__ for p in pokemons]
    for d in data:
        d.pop('_sa_instance_state', None)
    return jsonify(data)

@main_bp.route('/export/xml')
def export_xml():
    pokemons = Pokemon.query.all()
    data = [p.__dict__ for p in pokemons]
    for d in data:
        d.pop('_sa_instance_state', None)
    xml = dicttoxml(data)
    return Response(xml, mimetype='application/xml')


