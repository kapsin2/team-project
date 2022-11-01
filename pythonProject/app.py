from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://kalcox:qwer1234@cluster0.zdivsa4.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/bang1.html')
def bang1():
   return render_template('bang1.html')

@app.route('/bang2.html')
def bang2():
   return render_template('bang2.html')

@app.route('/bang3.html')
def bang3():
   return render_template('bang3.html')

@app.route('/bang4.html')
def bang4():
   return render_template('bang4.html')

@app.route('/bang5.html')
def bang5():
   return render_template('bang5.html')

@app.route("/comment", methods=["POST"])
def web_mars_post():
   name_receive = request.form['name_give']
   com_receive = request.form['com_give']
   doc= {
       'name':name_receive,
       'com' : com_receive
   }
   db.comment.insert_one(doc)

   return jsonify({'msg':'입력 완료!'})from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb+srv://kalcox:qwer1234@cluster0.zdivsa4.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/bang1.html')
def bang1():
    return render_template('bang1.html')


@app.route('/bang2.html')
def bang2():
    return render_template('bang2.html')


@app.route('/bang3.html')
def bang3():
    return render_template('bang3.html')


@app.route('/bang4.html')
def bang4():
    return render_template('bang4.html')


@app.route('/bang5.html')
def bang5():
    return render_template('bang5.html')


@app.route("/comment1", methods=["POST"])
def web_mars_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.comment1.insert_one(doc)

    return jsonify({'msg': '입력 완료!'})


@app.route("/comment1", methods=["GET"])
def web_mars_get():
    order_list = list(db.comment1.find({}, {'_id': False}))
    return jsonify({'orders': order_list})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)




@app.route("/comment", methods=["GET"])
def web_mars_get():
    order_list = list(db.comment.find({}, {'_id': False}))
    return jsonify({'orders': order_list})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
