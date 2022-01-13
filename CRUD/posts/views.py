from django.shortcuts import redirect, render
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    ctx = {'posts' : posts}

    return render(request, template_name= 'list.html', context = ctx)

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    ctx = {'post' : post}

    return render(request, template_name = 'detail.html', context=ctx)

# def post_create(request):
#     if request.method == 'POST': #우리가 게시판에서 글을 다 작성을 하고 save 버튼을 눌렀을 때(DB변동)
#         post = Post()
#         post.title = request.POST['title']
#         post.writer = request.POST['writer']
#         post.content = request.POST['content']
#         post.save()

#         return redirect('/posts')

#     else: #request.method == 'GET' => 우리가 게시판에 처음 들어가서 빈 form만 바라볼 때
#         # post = Post()
#         # ctx = {'post' : post}

#         return render(request, template_name='create.html')

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('posts:list')
    else:
        form = PostForm()
        ctx = {'form' : form}

        return render(request, template_name='post_form.html', context=ctx)