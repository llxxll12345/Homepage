from django.contrib.syndication.views import Feed

from .models import Post


class allRssFeed(Feed):
    title = "My blog"
    link = "/"
    description = "Blog contents"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[' + str(item.category) + '] ' + str(item.title)

    def item_description(self, item):
        return item.body