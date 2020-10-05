from blog_terminal.database import Database
from blog_terminal.blog import Blog


class Terminal(object):
    def __init__(self):
        print("☆★☆★☆★ WELCOME TO BLOG TERMINAL ★☆★☆★☆")
        print()
        self.user = input("Enter your author name: ")
        self.user_blog = None
        if self._user_has_account():
            print("Welcome back {}".format(self.user))
        else:
            self._prompt_user_for_account()

    def _user_has_account(self):
        blog = Database.find_one('blogs', {'author': self.user})
        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    def _prompt_user_for_account(self):
        print("=== Please register a new new_blog ===")
        title = input("Enter new_blog title: ")
        description = input("Enter new_blog description: ")
        new_blog = Blog(author=self.user,
                    title=title,
                    description=description)
        new_blog.save_to_mongo()
        self.user_blog = new_blog

    def run_terminal(self):
        read_or_write = input("Do you want to read [R] or write [W] blogs?\nPress [X] to quit. ")
        if read_or_write == 'R':
            self._list_blogs()
            self._view_blog()
            pass
        elif read_or_write == 'W':
            self.user_blog.write_new_post()
        elif read_or_write == 'X':
            print("Thank you for blogging!")

    def _list_blogs(self):
        blogs = Database.find(collection='blogs', query={})
        for blog in blogs:
            print("ID: {}, Author: {}, Title: {}".format(blog['id'], blog['author'], blog['title']))

    def _view_blog(self):
        print()
        blog_to_see = input("Enter the author of the blog you'd like to read: ")
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()
        print()
        for post in posts:
            print("Date: {}, Title: {}\nContent: {}\n".format(post['created_date'], post['title'], post['content']))
