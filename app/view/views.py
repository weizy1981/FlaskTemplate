'''
Created on Mar 20, 2017

@author: wzy
'''
from app import app
@app.route('/')
def index():
    return 'Index page'
