

def auth_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('auth_token')
        if not token:
            return abort(401, 'Cannot find auth_token in request params')
        user_uuid = redis_store.get(token)
        if not user_uuid:
            return abort(403, 'Cannot find token')
        user = db.session.query(User).filter_by(uuid=user_uuid).first()
        if not user:
            return abort(403, 'Cannot find user from token')
        g.user = user
        return f(*args, **kwargs)
    return decorated