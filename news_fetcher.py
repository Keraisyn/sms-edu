import requests

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
                res = res + str(i+1) + a["title"] + '\n'
                i += 1
        return res


api = News()
print(api.fetch(input()))
print(api.data)
