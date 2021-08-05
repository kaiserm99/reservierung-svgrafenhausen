#!/usr/bin/python3

SERVER = True

if SERVER:
    import sys
    import logging
    logging.basicConfig(stream=sys.stderr)
    sys.path.insert(0, "/var/www/reservierung_svgrafenhausen/")


from reservierung_svgrafenhausen import create_app

application = create_app()

if not SERVER:
    application.run(debug=True)
