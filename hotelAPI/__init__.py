from flask import Flask

def create_app():

    application = Flask(__name__,template_folder='templates')
    application.config['SECRET_KEY'] = 'hotelAPI'
    return application 