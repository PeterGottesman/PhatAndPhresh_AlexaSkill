from urllib import request, parse
import json

def build_response(text):
    response_obj = {
        'outputSpeech': {
            'type': 'SSML',
            'ssml': "<speak>" + text + "</speak>"
        },
        'shouldEndSession': True
    }

    resp = {
        'version': '1.0',
        'response': response_obj
    }

    return resp

def format_text(verses):
    text_fmt = ""
    for verse in verses:
        text_fmt += verse
        text_fmt += "<break time=\"0.2s\"/>"
    return text_fmt

def text_fetch(num_verses):
    api_url = "http://phatandphresh.azurewebsites.net/api/phresh"
    api_params = parse.urlencode({'verses' : num_verses})
    req = request.urlopen(api_url + "?" + api_params) 
    if req.getcode() != 200:
        return None
    response = json.load(req)
    print(response)
    verses = [verse for verse in response['verses']]
    return verses


def phire_handler(intent):
    formatted = ""
    if 'value' in intent['slots']['num_verses']:
        num_verses = intent['slots']['num_verses']['value']
    else:
        num_verses = 1
    text = text_fetch(num_verses)
    if text is None:
        build_response("Error communicating with phat and phresh")
    else:
        formatted += format_text(text)
        return build_response(formatted)

def phat_handler(event, context):
    if (event['session']['application']['applicationId'] !=
        "amzn1.ask.skill.0a11af58-1379-4432-a382-8dd19e779029"):
        raise ValueError("Invalid App ID")
    
    if event['request']['intent']['name'] == "PhireIntent":
        return phire_handler(event['request']['intent'])
    else:
        return build_response("Something went wrong!")



