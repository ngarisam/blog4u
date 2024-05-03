from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views import View
from django.utils import timezone
from django.contrib import messages
from . forms import ReaderRegistrationForm
from django.shortcuts import render
from .forms import ContactForm
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def home(request, val=None):
    if val != None and val!="others":
        blogs=Blog.objects.filter(blog_status="published", categories__icontains=val).order_by("-pub_date")[:6]
    else:
        blogs=Blog.objects.filter(blog_status="published").order_by("-pub_date")[:6]

    for blog in blogs:
        blog.pub_date = format_pub_date(blog.pub_date)

    return render(request, "operaminiclone/home.html", locals())




def viewpost(request, year, month, val):
    formatted_url = f"{year}/{month}/{val}"
    blog = Blog.objects.get(link=formatted_url)
    comments = Comment.objects.filter(blog=blog).order_by("-pub_date")[:5]
    comments_with_replies = {}

    for comment in comments:
        # Filter all replies for each comment
        all_replies = Reply.objects.filter(comment=comment).order_by("-pub_date")[:3]

        # Create a nested structure for replies
        nested_replies = {}

        for reply in all_replies:
            # Check if the reply has a parent or not
            if reply.parent is None:
                # If it has no parent, create a list for it
                if reply not in nested_replies:
                    nested_replies[reply] = []
            else:
                # If it has a parent, add it to the parent's list
                if reply.parent in nested_replies:
                    nested_replies[reply.parent].append(reply)

        comments_with_replies[comment] = nested_replies

    # Update the pub_date using the format_pub_date function
    for comment, _ in comments_with_replies.items():
        comment.pub_date= format_pub_date(comment.pub_date)

    return render(request, "operaminiclone/viewpost.html", locals())


def about(request):
        return render(request, "operaminiclone/about.html")
def contact(request):
        
        return render(request, "operaminiclone/contact.html")
def addcomment(request):
    data={'success': True, 'message':'Same'}
    return JsonResponse(data)
def sendmessage(request):
       if (request.method == 'POST'):
           form=request.POST
           add=Contact(username=form['username'], email=form['email'], msg=form['message'])
           add.save()
           message="Message sent successfully"
           return render(request, 'operaminiclone/contact.html', locals())
       else:
           return redirect('contact')
def format_pub_date(pub_date):
    now = timezone.now()
    time_difference = now - pub_date.astimezone(timezone.utc)

    if time_difference.total_seconds() < 60 * 60:  # Less than 60 minutes
        minutes_ago = int(time_difference.total_seconds() / 60)
        formatted_date = f"{minutes_ago} min ago"

    elif time_difference.total_seconds() < 60 * 60 * 12:  # Less than 12 hours
        hours_ago = int(time_difference.total_seconds() / 3600)
        formatted_date = f"{hours_ago} hour{'s' if hours_ago > 1 else ''} ago"

    else:
        formatted_date = timezone.localtime(pub_date).strftime("%B %d, %Y %I:%M %p") 
    return formatted_date
class ReaderRegistrationView(View):
    def get(self,request):
        form=ReaderRegistrationForm()
        return render(request,"operaminiclone/register.html", locals())
    def post(self, request):
        form=ReaderRegistrationForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, "Your registration was successful")
        else:
            messages.warning(request, "An error occured during registration")

        return render(request,"operaminiclone/register.html", locals())