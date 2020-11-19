from pymongo import MongoClient
from bson.objectid import ObjectId

from flask import Flask, render_template, jsonify

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta

# HTML 화면 보여주기
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/posts', methods=['GET'])
def read_posts():
    posts = list(db.reviews.find({}))
    for post in posts:
        post['_id'] = str(post['_id'])
    return jsonify({'posts': posts})

@app.route('/posts/<post_id>')
def post_detail(post_id):
    print(f'현재 post의 아이디는 {post_id}입니다.')
    post = db.reviews.find_one({'_id': ObjectId(post_id)})
    return render_template('post-detail.html', **post)

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)