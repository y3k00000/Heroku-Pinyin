from flask import *
from pypinyin import pinyin, lazy_pinyin, Style
import urllib.parse

app = Flask(__name__)

@app.route('/pinyin')
def index():
    strToConvert = request.args.get("str")
    strToConvert = urllib.parse.unquote_plus(strToConvert)
    print(strToConvert)
    strToConvert = pinyin(strToConvert,style=Style.BOPOMOFO)
    print(strToConvert)
    stringToConvert = [item[0] for item in stringToConvert]
    strToConvert = " ".join(strToConvert)
    print(strToConvert)
    return strToConvert

if __name__ == '__main__':
    app.run(debug=True)
