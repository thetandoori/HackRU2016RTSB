from flask import Flask, request, redirect
import twilio.twiml
from google import VisionApi

app = Flask(__name__)

class SMSRequest:
    def __init__(self):
        pass
    '''def __init__(self, mediaUrl,analysisType):
        self.mediaUrl = mediaUrl
        self.analysisType = analysisType
    '''
    def getMediaUrl(self):
        return self.mediaUrl

    def getAnalysisType(self):
        return self.analysisType

@app.route("/", methods=['GET','POST'])
def recieveSMSImageAndRespond():
    """Analyze an image sent by a user."""
    # analysisType = request.form['Body']   # Body will contain the analysis the user wants to be done on the image.
    # incoming_number = request.form['From'] 
    # image_url= request.form['MediaUrl0']   # Contains the URL to image which is located on twilio.

    vision = VisionApi()
    filename = vision.writeFile(url=request.form['MediaUrl0'])
    print filename
    responseMessage = vision.detectText(input_filenames=[filename])

    # Call a functon to analyze the image. It returns a string which contains the analysis.
    analysisResult=responseMessage[filename][0]['description']
    print "Analysis result:"
    print analysisResult

    # return the analysis back to the sender.
    resp = twilio.twiml.Response()
    resp.message(analysisResult)

    # print image_url
    # print analysisType
    # print incoming_number

    return str(resp)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
