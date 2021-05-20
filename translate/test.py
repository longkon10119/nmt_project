import requests
import json


def get_transalte(text):
  x = requests.get(
    u"https://translate.googleapis.com/translate_a/single?dt=t&client=gtx&sl=en&tl=vi&q={}&ie=UTF-8&oe=UTF-8".format(
      text))
  result = x.text
  data = json.loads(result)
  return data[0][0][0]