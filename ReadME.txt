Project Participants:
	Rahul Tandon (rtandon08@gmail.com)
	Samuel Baysting (samuelbaysting@gmail.com)

Languages:
	Python
API:
	Google Vision API -Analyzes images sent by the user.
	Twilio API - Receives the image from the user and returns the analysis.
Server:
	Linode Server-Runs the python script to handle the twilio send and recieve. Also handles the Google Vision API

Summary:
	This project uses the Twilio and Google API to process images. The code to process the twilio requests is running on a Lincode server.

	Steps:
	1) A user sends an image to the twilio phone number. Phone Number is :(845) 999-3027.
	2) Twilio stores that image to a url which is availble in the request message.
	3) Next the url to the image is passed on to the Google Vision API and a process is run to detect text in the image.
	4) Once the analysis is finished, a string is returned back.
	5) The returned string is sent back to the user using Twilio.

Future:
	Allow the user to send a message along with the image to specify what type of analysis they want done on the image since the Google Vision API can do analysis on a variety of things.