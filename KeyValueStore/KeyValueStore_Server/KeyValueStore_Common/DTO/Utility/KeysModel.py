from flask_restplus import Namespace, fields


class KeyModel:
    api = Namespace('keys', description='Key Metadata')
    user = api.model('keys', {
        'keyId': fields.String(required=True, description='key id'),
        'data': fields.Raw(required=True, description='data')
    })