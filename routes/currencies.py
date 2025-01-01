from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from data.models import Currency
from schemas import CurrencySchema
from applab2 import db

currencies_bp = Blueprint('currencies', __name__)
currency_schema = CurrencySchema()
currencies_schema = CurrencySchema(many=True)

@currencies_bp.route('/currency', methods=['POST'])
def create_currency():
    try:
        data = currency_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_currency = Currency(code=data['code'], name=data['name'])
    db.session.add(new_currency)
    db.session.commit()

    return currency_schema.dump(new_currency), 201

@currencies_bp.route('/currencies', methods=['GET'])
def get_currencies():
    currencies = Currency.query.all()
    return currencies_schema.dump(currencies), 200
