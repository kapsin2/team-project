from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

from pymongo import MongoClient
import certifi

ca = certifi.where()

client = MongoClient('mongodb+srv://kalcox:qwer1234@cluster0.zdivsa4.mongodb.net/?retryWrites=true&w=majority',tlsCAFile=ca)
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


@app.route('/comment1', methods=["POST"])
def comment_post1():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.comment1.insert_one(doc)

    return jsonify({'msg': '입력 완료!'})


@app.route('/comment1', methods=["GET"])
def comment_get1():
    comment_list = list(db.comment1.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route('/comment2', methods=["POST"])
def comment_post2():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.comment2.insert_one(doc)

    return jsonify({'msg': '입력 완료!'})


@app.route('/comment2', methods=["GET"])
def comment_get2():
    comment_list = list(db.comment2.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route('/comment3', methods=["POST"])
def comment_post3():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.comment3.insert_one(doc)

    return jsonify({'msg': '입력 완료!'})


@app.route('/comment3', methods=["GET"])
def comment_get3():
    comment_list = list(db.comment3.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route('/comment4', methods=["POST"])
def comment_post4():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.comment4.insert_one(doc)

    return jsonify({'msg': '입력 완료!'})


@app.route('/comment4', methods=["GET"])
def comment_get4():
    comment_list = list(db.comment4.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

@app.route('/comment5', methods=["POST"])
def comment_post5():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    doc = {
        'name': name_receive,
        'comment': comment_receive
    }
    db.comment5.insert_one(doc)

    return jsonify({'msg': '입력 완료!'})


@app.route('/comment5', methods=["GET"])
def comment_get5():
    comment_list = list(db.comment5.find({}, {'_id': False}))
    return jsonify({'comments': comment_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
