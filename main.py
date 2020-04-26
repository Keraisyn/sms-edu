# /usr/bin/env python
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import wolframalpha

app = Flask(__name__)
# app.config["SECRET_KEY"] = "W2hdvq3Rzdf6GYlQPq-6mg"


def wolfram_text_api(q):
    """Query the Wolfram Short Answer API."""

    try:
        app_id = "7GLJR5-P9U75R5EH2"
        client = wolframalpha.Client(app_id)

        r = client.query(q)
        answer = next(r.results).text

        return answer
    except:
        return "error"


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    """Respond to incoming messages."""
    body = request.values.get('Body', None)
    print(body)


    ans = wolfram_text_api(str(body))
    # session["news_state"] = "query"

    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message(ans)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)