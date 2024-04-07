import random
from post.models import Post

data = Post.objects.all()
shu = random.shuffle(data)

print(shu)