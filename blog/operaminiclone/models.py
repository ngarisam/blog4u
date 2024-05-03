from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField  # Import the RichTextField from CKEditor
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.contrib.auth.models import User

# Choice tuple for categories
CATEGORY_CHOICES = (
    ('Jobs', 'Jobs'),
    ('Entertainment', 'Entertainment'),
    ('Politics', 'Politics'),
    ('Health', 'Health'),
    ('Sports', 'Sports'),
    ('Relationship', 'Relationship'),
    ('Society', 'Society'),
    ('Fashion and Design', 'Fashion and Design'),
    ('Agriculture', 'Agriculture'),
    ('Business', 'Business'),
    ('Education', 'Education'),
)

# Choice tuple for author status
AUTHOR_STATUS_CHOICES = (
    ('Active', 'Active'),
    ('Demoted', 'Demoted'),
    ('Expelled', 'Expelled'),
)

BLOG_STATUS=(
    ("pending", "pending"),
    ("revise", "revise"),
    ("published", "published"),
    ("rejected", "rejected"),
)



class AuthorProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_level = models.PositiveIntegerField(default=1)
    join_date = models.DateTimeField(auto_now_add=True)
    published_articles = models.PositiveIntegerField(default=0)
    rejected_articles = models.PositiveIntegerField(default=0)
    author_status = models.CharField(max_length=10, choices=AUTHOR_STATUS_CHOICES, default='Active')
    payment_details = models.TextField(blank=True)
    monetized_articles = models.PositiveIntegerField(default=0)
    lifetime_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    pending_earnings = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return self.user.username

class Blog(models.Model):
    heading = models.CharField(max_length=100)
    content = RichTextUploadingField()  # Use RichTextField for rich content
    blog_status = models.CharField(max_length=10, choices=BLOG_STATUS, default="pending")
    coverimage = models.ImageField(upload_to='blog_covers/')
    author = models.ForeignKey(AuthorProfile, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    categories = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    link = models.CharField(max_length=150, null=True, default=None, blank=True, editable=False)

    def __str__(self):
        return self.heading
    
class ReaderProfile(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    usernamename=models.CharField(max_length=100)
    email=models.EmailField()   
    def __str__(self):
        return self.name
    

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    reader = models.ForeignKey(User, on_delete=models.CASCADE) #must be logged in
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment: {self.text} for '{self.blog.heading}'"

class Reply(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='replies_to_comment')
    text = models.TextField(max_length=240 )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    parent=models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reply: {self.text} on Comment: {self.comment.text}"

class BlogView(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    session_id = models.CharField(max_length=50, null=True, blank=True)
    view_date = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        if self.user:
            return f"View of '{self.blog.heading}' by {self.user.username}"
        else:
            return f"Anonymous view of '{self.blog.heading}'"

class Contact(models.Model):
    username=models.CharField(max_length=50)
    email=models.EmailField()
    msg=models.TextField(max_length=240)

    def __str__(self):
        return f"{self.username} sent you a message "