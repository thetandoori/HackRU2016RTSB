from flask import Flask, request, redirect
import twilio.twiml

app = Flask(__name__)
@app.route("/", methods=['GET','POST'])

class SMSRequest:
   def __init__(self, mediaUrl,analysisType):
      self.mediaUrl = mediaUrl
      self.analysisType = analysisType

   def getMediaUrl(self):
    	return self.mediaUrl

   def getAnalysisType(self):
   		return self.analysisType

def recieveSMSImageAndRespond():
    """Analyze an image sent by a user."""
    # analysisType = request.form['Body']   # Body will contain the analysis the user wants to be done on the image.
    # incoming_number = request.form['From'] 
    # image_url= request.form['MediaUrl0']   # Contains the URL to image which is located on twilio.

    # responseMessage="You chose to analyze your image using: "+ analysisType +"\nStarting image analysis....."

    # Call a functon to analyze the image. It returns a string which contains the analysis.
    analysisResult=#myfunctioncall(Request(request.form['From'],request.form['MediaUrl0']))

    # return the analysis back to the sender.
    resp = twilio.twiml.Response()
    resp.message(analysisResult)

    # print image_url
    # print analysisType
    # print incoming_number

    return str(resp)

if __name__ == "__main__":
    app.run()
