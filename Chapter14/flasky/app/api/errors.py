@main.app_errorhandler(404)
def pagee_not_found(e):
    if request.accept_mimetypes.accept_json and \
            not request.accept_mimetypes.accept_html:
        response = jsonify({'error': 'not found'})
        response.status_code = 404
        return response
    return render_template('404.html'), 404

def forbidden(message):
    response = jsonify({'error': 'forbiden', 'message': message})
    response.status_code = 403
    return response


