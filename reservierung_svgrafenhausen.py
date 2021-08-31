#!/usr/bin/python3

SERVER = True

SECRET_PATH = "secret.txt"

if SERVER:
    import sys
    import logging
    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0, "/var/www/reservierung_svgrafenhausen/")

    SECRET_PATH = "/home/secret.txt"


from reservierung_svgrafenhausen import create_app


application = create_app()

@application.before_first_request
def setup():
    from werkzeug.security import generate_password_hash
    from reservierung_svgrafenhausen.models import User
    from reservierung_svgrafenhausen import db

    f = open(SECRET_PATH, "r")
    first_name = f.readline().replace("\n", "")
    last_name = f.readline().replace("\n", "")
    email = f.readline().replace("\n", "")
    password = f.readline().replace("\n", "")

    admin1 = User(first_name=first_name, 
                  last_name=last_name,
                  email=email,
                  password=generate_password_hash(password, method='sha256'),
                  admin=True)

    user1 = User.query.filter_by(email=admin1.email).first()

    if user1 is None:    
        db.session.add(admin1)
        db.session.commit()

    f.close()


if not SERVER:
    application.run(debug=True)
