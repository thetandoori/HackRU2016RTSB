Project Participants:
	Rahul Tandon (rtandon08@gmail.com)
	Samuel Baysting (samuelbaysting@gmail.com)

Final File located in api folder. Files: twilio.py and google.py
Setting up local env: https://www.twilio.com/docs/quickstart/python/devenvironment

Languages:
	Python
API:
	Google Vision API -Analyzes images sent by the user.
	Twilio API - Receives the image from the user and returns the analysis.
Server:
	Linode Server-Runs the python script to handle the Twilio send and receive. It also handles the calls Google Vision API.
Summary:
	This project uses the Twilio and Google API to process images. The code to process the twilio requests is running on a Lincode server. A user sends an image to our specified twilio number and gets back the text in that image.

	Process:
	1) A user sends an image to the Twilio phone number. Phone Number is :(845) 999-3027.
	2) Twilio stores that image to a url which is available in the request message.
	3) Next we get the MediaURL from the request message and download the actual image. 
    4) The image is then passed on to the Google Vision API and a process is run to detect text in the image.
	5) Once the analysis is finished, a string is returned.
	6) The returned string is sent back to the user using Twilio.

Future:
	Allow the user to send a message along with the image to specify what type of analysis they want done on the image since the Google Vision API can analyze an image a variety of ways.
