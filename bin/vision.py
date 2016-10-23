from api.google import VisionApi

vision = VisionApi()
response = vision.detectText(input_filenames=['ocr.png'])
print response['ocr.png'][0]['description']
