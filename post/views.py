from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponseBadRequest, HttpResponseServerError, HttpResponseNotFound
from dotenv import load_dotenv
import re
import markdown
import os

load_dotenv()

POST_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/_post'
AUTHOR = os.getenv('AUTHOR')
SIGNATURE = os.getenv('SIGNATURE')

POSTS = []

class MarkDownFile:
    def __init__(self, path:str):
        self.path = path
        with open(path, 'r', encoding='utf-8') as md:
            self.id, self.title, self.author, self.date, self.content = self.parse(md.read())
    
    def parse(self, md_content: str):
        meta_pattern = r'^id:(\d+?)\ntitle:(.*?)\nauthor:(.*?)\ndate:(.*?)\n---\n(.*?)$'
        match = re.search(meta_pattern, md_content, re.DOTALL)
        if match:
            id = int(match.group(1).strip())
            title = match.group(2).strip()
            author = match.group(3).strip()
            date = match.group(4).strip()
            content = match.group(5).strip()
            return id, title, author, date, content
        else:
            return ValueError("Metadata not found in Markdown file")

def LoadPosts():
    global POSTS
    for file in os.listdir(POST_PATH):
        f = os.path.join(POST_PATH, file)
        mdf = MarkDownFile(f)
        POSTS.append(
            {
                "id": mdf.id,
                "title": mdf.title,
                "author": mdf.author,
                "date": mdf.date,
                "content": mdf.content,
            }
        )

LoadPosts()

posts = sorted(POSTS, key=lambda x: x['id'])

def index(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'post/index.html', {
            "author": AUTHOR,
            "sign": SIGNATURE,
            "posts": posts,
            "num": len(posts),
        })
    if request.method =='POST':
        return HttpResponseBadRequest('None')

def view(request: HttpRequest, id: int):
    if request.method == 'GET':
        post = None
        next = None
        last = None
        for i in range(0, len(posts)):
            if posts[i]['id'] == id:
                post = posts[i]
                if i + 1 < len(posts):
                    next = posts[i + 1]['id']
                if i - 1 >= 0:
                    last = posts[i - 1]['id']
                break
        return render(request, 'post/view.html', {
            "post": post,
            "last": last,
            "next": next,
        })