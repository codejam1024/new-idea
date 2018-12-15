app = []

def run():
    print('core run.')
    print('last config host : ' + app.config.host)
    print('last config port : ' + app.config.port)
    host = input('Input server host(127.0.0.1):') or '127.0.0.1'
    port = input('Input server port(8080):') or '8080'
    app.config.host = host
    app.config.port = port
    app.config.save()
    app.server.run()
