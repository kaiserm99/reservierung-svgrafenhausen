#!/usr/bin/python3

SERVER = True

if SERVER:
    import sys
    import logging
    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0, "/var/www/reservierung_svgrafenhausen/")


from reservierung_svgrafenhausen import create_app


application = create_app()

@application.before_first_request
def setup():
    from werkzeug.security import generate_password_hash
    from reservierung_svgrafenhausen.models import User
    from reservierung_svgrafenhausen import db

    admin1 = User(first_name="SV", 
                  last_name="Grafenhausen",
                  email="549829493@svgrafenhausen.de",
                  password=generate_password_hash("Svg1921$", method='sha256'),
                  admin=True)

    user1 = User.query.filter_by(email=admin1.email).first()

    if user1 is None:    
        db.session.add(admin1)
        db.session.commit()

if not SERVER:
    application.run(debug=True)
