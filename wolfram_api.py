import requests
import wolframalpha

# def wolfram_short_api(q, units="metric"):
#     url = "http://api.wolframalpha.com/v1/result"
#     app_id = "7GLJR5-P9U75R5EH2"
#     query = q
#     units = units
#
#     p = {
#         'appid':app_id,
#         'i':query,
#         'units':units
#     }
#
#     r = requests.get(url = url, params = p)
#     print(r)
#     data = r.json()
#
#     return str(data)

def alphaq(q):
    app_id = "7GLJR5-P9U75R5EH2"
    client = wolframalpha.Client(app_id)

    res = client.query(q)
    answer = next(res.results).text

    return answer


print(alphaq("2agawerag"))