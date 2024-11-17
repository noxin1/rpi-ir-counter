# rpi-ir-counter
A object counter using an IR sensor, a DIY Ramp and some 3d printed parts

Counter Hardware Requirements
* Raspberry PI - 3b+, 4, 5 preferred due to the GPIO header being present, Pi Zero or better will work, but you will have to figure out how to connect the IR sensor
* IR Sensor - something like this https://www.amazon.com/dp/B0CD7JZS4P
* Jumper wires - to connect the IR Sensor to the RPI

Software Requirements
* Raspberry PI OS
* Python3
* python3-pyfiglet

Ramp Components
1 x 12 inch x 36 inch shelf https://www.homedepot.com/p/Everbilt-12-in-W-x-36-in-D-White-Laminate-Decorative-Wall-Shelf-3967015HDS/328395739 Make sure it's smooth and the objects will slide well
2 x 36 inch Angle iron https://www.homedepot.com/p/Everbilt-1-1-2-in-x-36-in-Aluminum-Angle-with-1-8-in-Thick-801407/204273991 You can maybe use 1", but some objects may tumble over the edge
Wood or some other material to make the legs for the ramp
3 clamps or some other attachment to secure the 3d printed components

3D Printed components
* 2 x Ramp Feet
* 1 x Large Triangle
* 1 x Medium Triangle
* 1 x Medium Rectangle
* 1 x IR Sensor Carrier

Installation
- Setup your Rapsberry PI with the operating system of choice, make sure it has Python3, as that is what I tested on
- sudo apt install python3-pyfiglet
- Download ircounter.py

Setup 
- Build your Ramp (Shelf, Angle Iron, Ramp Feet, Legs.   I like the ramp to be at 30 to 40 Degrees to give the objects some good momentum.
- Attach your IR Sensor to the Raspberry PI (do this with the PI Powered off initially
  * Connect VCC pin to Pin2
  * Connect GND pin to Pin14
  * Connect OUT pin to Pin11
  * * If you use a different pin for OUT, you'll have to change the value in ircounter.py
    * https://toptechboy.com/understanding-raspberry-pi-4-gpio-pinouts/pinout-corrected-2/
- Attach your IR Sensor the IR Carrier
- Attach the Triangles and Rectangle to the ramp (See Ramp Picture for an example).   You want to have them arranged so the objects slide from triangle 1 (Large in picture) to triangle 2 (Medium in Picture) and then slides along the Rectangle
- The IR sensor has an adjustment screw to set the range for detection.   You'll have to tune this for your setup.   You want the light off when no object is present, and ... the light on when there is an object.   You can do this without the counter program running.

Running the counter
* The counter makes a beep when it detects.   If you want to use it, but don't have speakers on your PI, ssh in from a laptop or computer with sound/speakers.
* Log in to the PI
* Go to where ircounter.py is
* run : python3 ./ircounter.py
* pass your hand in front of the IR Sensor, it should increment the count and beep
* If necessary, tune the IR sensor again
* Start sending objects down the ramp.  It may take some adjustments and practice to get them to trigger the IR Counter consisently.
* To exit, Press Control C on your ircounter.py execution
