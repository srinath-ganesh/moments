from dotenv import load_dotenv
import os
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials

load_dotenv()

endpoint = os.getenv('endpoint')
key = os.getenv('key')
computervision_client = ComputerVisionClient(endpoint, CognitiveServicesCredentials(key))
def alt_text_generate(filename):
    image = open(filename, "rb")
    results = computervision_client.describe_image_in_stream(image, visual_features=[VisualFeatureTypes.description])
    return results.captions[0].text if results else ""
    
def analyze_image_objects(filename):
    with open(filename, "rb") as image_stream:
        image_analysis = computervision_client.analyze_image_in_stream(image_stream, visual_features=[VisualFeatureTypes.objects])
    detected_objects = image_analysis.objects
    tags = [obj.object_property for obj in detected_objects]
    return tags if tags else []