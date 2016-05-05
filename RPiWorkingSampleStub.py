import json
import cherrypy
from cherrypy import tools
import random

@cherrypy.tools.json_out()
def error_page_404(status, message, traceback, version):
    return {"Error":"404"}  

class RootWS():
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def index(self):
        return {'index': "Hi There"}
    
    @cherrypy.expose
    def release(self,releaseResp=None,_=None):
        """ Engage the sg99 servo and release the payload """
        try:
            import RPi.GPIO as GPIO
            import time    
            GPIO.setmode(GPIO.BOARD)
            PIN = 36
            GPIO.setup(PIN,GPIO.OUT)
            p = GPIO.PWM(PIN,50)
            p.start(0.0001)
            time.sleep(2)
            p.stop()
        except:
            pass
        return 'releaseResp({"Release": "True"});'
    
    @cherrypy.expose
    def temp(self,tempResp=None,_=None):
        """ Return the current temp as an integer between 32 and 145 """
        return 'tempResp({"Temperature": ' + str(random.randint(32,100)) +'});'
        
def start_server():
    cherrypy.tree.mount(RootWS(), '/')
    cherrypy.config.update({'server.socket_port': 9090,
                            'server.socket_host': '0.0.0.0'})
    cherrypy.engine.start()

if __name__ == '__main__':
    start_server()
