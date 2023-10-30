from flask import Flask, request, render_template
import requests

map = Flask(__name__)


@map.route('/main',methods=["GET","POST"])
def get_location():
    # get ip
    if request.method == "GET":
        key = request.form.get('IP')
        response = requests.get('http://ip-api.com/json/?fields={key}')

        data = response.json()

        lat = data['lat']
        lon = data['lon']
        return "hello"+data['lat']+","+data['lon']
    
    return render_template('main.html', lat=lat, lon=lon)




