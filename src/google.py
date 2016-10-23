import os
import base64
from googleapiclient import discovery
from googleapiclient import errors
from oauth2client.service_account import ServiceAccountCredentials
from httplib2 import Http
import json
import subprocess

SERVICE_URL = ['https://www.googleapis.com/auth/cloud-platform']
CREDENTIALS = os.environ['GOOGLE_APPLICATION_CREDENTIALS']


class VisionApi:
    """Construct and use the Google Vision API service."""

    credentials = None
    http_auth = None
    service = None

    def __init__(self):
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS, scopes=SERVICE_URL)
        self.http_auth = self.credentials.authorize(Http())
        self.service = discovery.build('vision', 'v1', http=self.http_auth)

    def detectText(self, input_filenames, num_retries=3, max_results=6):
        response = self.httpRequest(input_filenames=input_filenames, feature_type='TEXT_DETECTION', num_retries=3, max_results=6)
        return response

    def httpRequest(self, input_filenames, feature_type, num_retries=3, max_results=6):
        """Uses the Vision API to detect text in the given file.
        """
        print "Calling OCR API!"
        images = {}
        for filename in input_filenames:
            with open(filename, 'rb') as image_file:
                images[filename] = image_file.read()

        batch_request = []
        for filename in images:
            batch_request.append({
                'image': {
                    'content': base64.b64encode(
                            images[filename]).decode('UTF-8')
                },
                'features': [{
                    'type': feature_type,
                    'maxResults': max_results,
                }]
            })
        request = self.service.images().annotate(
            body={'requests': batch_request})

        try:
            responses = request.execute(num_retries=num_retries)
            if 'responses' not in responses:
                return {}
            text_response = {}
            for filename, response in zip(images, responses['responses']):
                if 'error' in response:
                    print("API Error for %s: %s" % (
                            filename,
                            response['error']['message']
                            if 'message' in response['error']
                            else ''))
                    continue
                if 'textAnnotations' in response:
                    text_response[filename] = response['textAnnotations']
                else:
                    text_response[filename] = []
            return text_response
        except errors.HttpError as e:
            print("Http Error for %s: %s" % (filename, e))
        except KeyError as e2:
            print("Key error: %s" % e2)

    def writeFile(self, url):
        subprocess.call("wget "+url+" -O tmp",shell=True)
        return "tmp"
