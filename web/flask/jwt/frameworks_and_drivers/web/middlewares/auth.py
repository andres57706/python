from flask_jwt import JWT

_users_repo = None
jwt = None


def setup(app,
          users_repository=None,
          authentication_handler=None,
          identity_handler=None):
    global _users_repo, jwt
    authentication_handler = authentication_handler \
        if authentication_handler != None else _auth_handler
    identity_handler = identity_handler if identity_handler != None \
        else _identity_handler
    _users_repo = users_repository
    jwt = JWT(app, authentication_handler, identity_handler)


def _auth_handler(username, password):
    """
    default authentication handler
    """
    pass


def _identity_handler(payload):
    """
    default identity handler 
    """
    pass
