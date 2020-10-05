from domain.app_rules.use_cases import pets as pets_svc
from flask_restful import Resource, marshal, reqparse
from ..models.pet import pet


class Pets(Resource):
    """
    Pet Web Resource
    """

    def __init__(self):
        self. _postparser = reqparse.RequestParser()
        self._postparser.add_argument(
            name='name',
            type=str,
            help='pet\'s name',
            trim=True,
            location='json',
            required=True)
        self._postparser.add_argument(
            name='age',
            type=float,
            help='pet\'s age must be a float number',
            trim=True,
            location='json',
            required=True)
        self._postparser.add_argument(
            name='kind',
            type=str,
            help='pet kind, choices: dog | cat',
            choices=('dog', 'cat'),
            trim=True,
            location='json',
            required=True)

    def get(self):
        """
        get pets list
        """
        items, count = pets_svc.get_all()
        return {
            'data':  marshal(items, pet),
            'total': count
        }

    def post(self):
        """
        add a pet
        """
        args: dict = self._postparser.parse_args()
        res = pets_svc.add_one(args)
        return res, 201
