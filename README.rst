flask-lambda-python3.6-lb
=========================

**Python 3.6+ Only**
--------------------


Installation
------------
pip install flask-lambda-python3.6-lb

Usage
-----

Here is an example of what ``my_python_file.py`` would look like::

    from flask_lambda import FlaskLambda

    app = FlaskLambda(__name__)


    @app.route('/foo', methods=['GET', 'POST'])
    def foo():
        data = {
            'form': request.form.copy(),
            'args': request.args.copy(),
            'json': request.json
        }
        return (
            json.dumps(data, indent=4, sort_keys=True),
            200,
            {'Content-Type': 'application/json'}
        )


    if __name__ == '__main__':
        app.run(debug=True)
