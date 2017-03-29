#!/usr/bin/python
""" Script baseado em weblamp.py
Vietnamese-German University
Richard Bradley
Control LEDs from a webpage and
display system information on the web page
Based on a program for the Raspberry pi by
Matt Richardson
http://mattrichardson.com/Raspberry-Pi-Flask/
Connections
     LEDs : pins 7 & 13
"""
################################################
#                  Import Libraries            #
################################################
from wiringx86 import GPIOGalileoGen2 as GPIO
from flask import Flask, render_template, request
import datetime
import socket

################################################
#                Global Variables              #
################################################
gpio = GPIO(debug=False)
state = gpio.HIGH
app = Flask(__name__)

# Create a dictionary called pins to store the pin number, name, and pin state:
pins = {
   13 : {'id' : 'Quarto', 'state' : gpio.LOW},
   7 : {'id' : 'Sala', 'state' : gpio.LOW},
   9 : {'id' : 'Cozinha', 'state' : gpio.LOW}
   }


# Set each pin as an output and make it low:
for pin in pins:
   gpio.pinMode(pin, gpio.OUTPUT)
   gpio.digitalWrite(pin, gpio.LOW)

################################################
#                Home  Page                    #
################################################


@app.route("/")
def main():
   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = gpio.digitalRead(pin) #aqui deveria buscar no banco de dados o estado do pino
   # Put the pin dictionary into the template data dictionary:
   templateData = {
      'pins' : pins
      }
   # Pass the template data into the template main.html and return it to the user
   return render_template('index.html', **templateData)

################################################
#                Change Pin  Page              #
################################################
# The function below is executed when someone requests a URL with the pin number and action in it:
@app.route("/<changePin>/<action>")
def action(changePin, action):
   # Get Current Date and Time
   Now = datetime.datetime.now()
   DateNow = Now.ctime()

   # Get HostName
   HostName = socket.gethostname()

   # Get IP Address
   cmd = "ifconfig eth0 | grep 'inet addr:' | cut -d: -f2 | awk '{ print $1}'"
   p = Popen(cmd, shell=True,stdout=PIPE, stderr=PIPE)
   IPAddr, err = p.communicate()
   # use string command to remove new line character
   #IPAddr = IPAddr[:-1]

   # Convert the pin from the URL into an integer:
   changePin = int(changePin)

   # Get the device name for the pin being changed:
   deviceName = pins[changePin]['name']

   # If the action part of the URL is "on," execute the code indented below:
   if action == "on":
      # Set the pin high:
      gpio.digitalWrite(13, gpio.HIGH)
      # Save the status message to be passed into the template:
      message = "Turned " + deviceName + " on."
   if action == "off":
      gpio.digitalWrite(changePin, gpio.LOW)
      message = "Turned " + deviceName + " off."

   # For each pin, read the pin state and store it in the pins dictionary:
   for pin in pins:
      pins[pin]['state'] = gpio.digitalRead(pin)

   # Put variables into the template data dictionary to be passed to web page:
   templateData = {
      'message' : message,
      'pins' : pins,
      'DateNow' : DateNow,
      'HostName' : HostName,
      'IPAddr' : IPAddr
   }

   return render_template('weblamp.html', **templateData)

if __name__ == "__main__":
   app.run(host='169.254.70.110', port=8080, debug=True)
