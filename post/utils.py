from post.models import Post


def create_100_posts():
    for i in range(100):
        Post.objects.create(
            title=f'Post №{i}',
            text=f'Text of post #{i}',
        )
