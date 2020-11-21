
from bottle import route,run,request
temparature = input("Enter temperature value:")
humidity = input("Enter humidity:")
windspeed = input("Enter windspeed:")
rain = input("Enter rainy or not:")
 
@route('/')
 
def getsens():
    sensor_log = [{'sensor':'Temperature','value':temparature},
                  {'sensor':'Humidity','value':humidity},
                  {'sensor':'Windspeed','value':windspeed},
                  {'sensor':'Rain','value':rain}]
    return dict(data=sensor_log)
run(host='localhost',port=7000,debug=True)
