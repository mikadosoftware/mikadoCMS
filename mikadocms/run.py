from gunicorn.app.pasterapp import paste_server 
#from paste.deploy import loadapp 

#app = loadapp('config:mikadocms/foobar.ini', relative_to='.')

paste_server(app, host='0.0.0.0', port=8002) 
