from flask import *
from pypinyin import pinyin, lazy_pinyin, Style
import urllib.parse

app = Flask(__name__)

@app.route('/pinyin')
def index():
    str = request.args.get("str")
    str = urllib.parse.unquote_plus(str)+""
    str = pinyin(str,style=Style.BOPOMOFO)
    return "".join(str)


if __name__ == '__main__':
    app.run(debug=True)
