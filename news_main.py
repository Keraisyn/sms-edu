# /usr/bin/env python
from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
import requests
import wolframalpha

app = Flask(__name__)
app.config["SECRET_KEY"] = "W2hdvq3Rzdf6GYlQPq-6mg"


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


class News:
    data = []

    def fetch(self, incoming):
        url = ('http://newsapi.org/v2/everything?'
               'apiKey=fdf0bc884d9342b99eeca651362acda5')
        keywords = "+".join(incoming.split())
        url = url + "&q=" + keywords
        r = requests.get(url)
        d = r.json()
        res = ""
        i = 0
        for a in d['articles']:
            if i >= 10: break
            if a["title"] != None:
                self.data.append(a["content"])
                res = "{}[{}] {}\n".format(res, i+1, a["title"])
                # res = res + str(i+1) + a["title"] + '\n'
                i += 1
        return res


@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    print("REQUEST STARTED")
    """Respond to incoming messages."""
    body = request.values.get('Body', None)
    print(body)

    # Check if user would like to receive news
    if body.split()[0].lower() == "news":
        news_state = session.get("news_state")

        if not news_state:
            session["news_state"] = "query"
            news_state = session.get("news_state")

        if news_state == "query":
            news_api = News()
            ans = news_api.fetch("".join(body.split()[1:]))
            session["news_api"] = news_api.data
            session["news_state"] = "selection"
        elif news_state == "selection":
            print(session["news_api"])
            ans = session["news_api"][int(body.split()[1])]
            session["news_state"] = "query"
    else:
        ans = wolfram_text_api(str(body))
        session["news_state"] = "query"

    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message(ans)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)