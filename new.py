import argparse
from dotenv import load_dotenv
import os
from datetime import datetime

load_dotenv()
POST_PATH = os.path.dirname(os.path.abspath(__file__)) + '/_post'
AUTHOR = os.getenv('AUTHOR')

parser = argparse.ArgumentParser(description='New Post')

parser.add_argument('title', help='Title for the post')

args = parser.parse_args()

id = len(os.listdir(POST_PATH)) + 1

with open(POST_PATH + '/' + args.title + '.md', 'w', encoding='utf-8') as f:
    f.write(f'id:{id}\ntitle:{args.title}\nauthor:{AUTHOR}\ndate:{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n---')