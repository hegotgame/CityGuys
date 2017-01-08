"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Welcome to City Feedback. " \
                    "Where do you live?"
    # If the user either does not reply to the welcome message or smays something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Where do you live?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
def initialResponse():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Initial"
    speech_output = "Where do you live?"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Where do you live"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


def create_favorite_color_attributes(favorite_color):
    return {"favoriteColor": favorite_color}


def set_color_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = {}
    should_end_session = False

    if 'Color' in intent['slots']:
        favorite_color = intent['slots']['Color']['value']
        session_attributes = create_favorite_color_attributes(favorite_color)
        speech_output = "I now know your favorite color is " + \
                        favorite_color + \
                        ". You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
        reprompt_text = "You can ask me your favorite color by saying, " \
                        "what's my favorite color?"
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "Please try again."
        reprompt_text = "I'm not sure what your favorite color is. " \
                        "You can tell me your favorite color by saying, " \
                        "my favorite color is red."
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_color_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None

    if session.get('attributes', {}) and "favoriteColor" in session.get('attributes', {}):
        favorite_color = session['attributes']['favoriteColor']
        speech_output = "Your favorite color is " + favorite_color + \
                        ". Goodbye."
        should_end_session = True
    else:
        speech_output = "I'm not sure what your favorite color is. " \
                        "You can say, my favorite color is red."
        should_end_session = False

    # Setting reprompt_text to None signifies that we do not want to reprompt
    # the user. If the user does not respond or says something that is not
    # understood, the session will end.
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))


# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()

def askForFeedback(intent):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    city = ""
    if 'CityName' in intent['slots']:
        city = intent['slots']['CityName']['value']
    session_attributes = {}
    session_attributes['city'] = city
    card_title = "LOL"
    speech_output = "Where are you in " + city + ""
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Where are you in" + city + ""
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def giveFeedback(intent, session):
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    feedback = ""
    if 'myFeedback' in intent['slots']:
        feedback = intent['slots']['myFeedback']['value']
    session_attributes = session['attributes'].copy()
    card_title = "LOL"
    if 'city' in session_attributes:
        city = session_attributes['city']
    else:
        city = 'Las Vegas'
    if 'state' in session_attributes:
        state = session_attributes['state']
    else:
        state = 'NV'
    feedback = feedback
    if 'formalName' in session_attributes:
        nameF = session_attributes['formalName']
    else:
        nameF = "Strip"
    import urllib
    import urllib2
    import json
    data = {

      "feedback": feedback,
      "city":city.replace(" ", ""),
      "state":state,
      "area":nameF
    }
    req = urllib2.Request('https://b7foq95o71.execute-api.us-east-1.amazonaws.com/alpha/feedback/text')
    req.add_header('Content-Type', 'application/json')
    response = urllib2.urlopen(req, json.dumps(data))
    responseString = response.read()
    info = json.loads(responseString)['Item']['Info']
    gencheck = info['department']
    dept = info['verbose']
    repname = info['name']
    email = info['email']
    number = info['number']
    session_attributes['name'] = repname
    session_attributes['email'] = email
    session_attributes['number'] = number
    #
    if gencheck == "GEN":
        speech_output = "Thanks for the general feedback. It has been entered into our system!"
    else:
        speech_output = "Okay, You're appropriate department is " + dept + ". They have been notified by email and entered into our dashboard. Would you like to contact them?" + ""
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please say your feedback"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
def getRegionName(intent, session):
    someRegion = ""
    if 'someRegion' in intent['slots']:
        someRegion = intent['slots']['someRegion']['value']
        #Get Region
    import json
    import urllib2
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + someRegion
    url = url.replace(" ", "+")
    print(url)
    response = urllib2.urlopen(url)
    html = response.read()
    data = json.loads(html.decode("utf-8") )['results'][0]['address_components']
    formalName = data[0]['short_name']
    kind = data[0]['types'][0]
    card_title = "Get Preferences"
    session_attributes = session['attributes'].copy()
    session_attributes['formalName'] = formalName
    session_attributes['state'] = data[-2]['short_name']

    card_title = "LOL"
    speech_output = "I got that you're in " + formalName + " which is a " + kind + ". If this is correct please say your feedback! "
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please say your feedback"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
def getContact(session):
    session_attributes = session['attributes'].copy()
    speech_output = "Okay, your representative is " + session_attributes['name'] + ". His number is " + str(session_attributes['number']) + "and email is" + session_attributes['email']
    card_title = "Raviteja Lingineni"
    reprompt_text = "Do you want contact info?"
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
            card_title, speech_output, reprompt_text, should_end_session))
def postToMap(intent):
    someRegion = ""
    if 'somePlace' in intent['slots']:
        someRegion = intent['slots']['somePlace']['value']
        #Get Region
    import json
    import urllib2
    url = 'http://maps.googleapis.com/maps/api/geocode/json?address=' + someRegion
    url = url.replace(" ", "+")
    print(url)
    response = urllib2.urlopen(url)
    html = response.read()
    data = json.loads(html.decode("utf-8") )['results'][0]['address_components']
    loc = json.loads(html.decode("utf-8") )['results'][0]['geometry']['location']
    import boto3
    client = boto3.client('iot-data')
    print("HIIIII: Client Created")
    # Change topic, qos and payload
    import json
    lat = loc['lat']
    lon = loc['lng']
    response = client.publish(
            topic='$aws/things/gothamShadow/shadow/update',
            qos=1,
            payload=json.dumps({"state": {"desired": {"lat":lat, "lon": lon}}})
        )
#     response = client.update_thing(
#     thingName='gothamShadow',
#     attributePayload={
#         'attributes': {
#             'lat': '50'
#         },
#         'merge': False
#     },
#     expectedVersion=123,
#     removeThingType=False
# )
    print(response)

    print(lat)
    print(lon)
    formalName = data[0]['short_name']
    kind = data[0]['types'][0]
    card_title = "Get Preferences"
    session_attributes = {}
    card_title = "Gotham"
    speech_output = "Pulling up " + formalName + " on your monitor"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please say your feedback"
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))
def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "fileFeedback":
        return initialResponse()
    elif intent_name == "giveCityName":
        return askForFeedback(intent)
    elif intent_name == "tellFeedback":
        return giveFeedback(intent, session)
    elif intent_name == "giveRegionName":
        return getRegionName(intent, session)
    elif intent_name == "getSafetyIndex":
        return postToMap(intent)
    elif intent_name == "getContact":
        return getContact(session)
    else:
        return initialResponse()


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
