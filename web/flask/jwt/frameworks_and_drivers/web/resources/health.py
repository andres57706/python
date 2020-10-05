from threading import Thread
from flask_restful import Resource

from domain.app_rules.use_cases import system


class Health(Resource):
    """
    Health resource
    """

    def get(self):
        """
        sub process test
        """
        t = Thread(None, system.count_n_seconds, 'counter thread', (120,))
        t.start()
        return {
            'message': 'counting process started'
        }

