# posts.py
posts = []

def get_posts():
    return posts

def add_post(title, content):
    post = {"title": title, "content": content}
    posts.append(post)
    