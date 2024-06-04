from rest_framework import serializers
from .models import ContactMessage

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields =['name', 'email', 'message']

from rest_framework import serializers
from .models import ContactMessage

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']


from rest_framework import serializers
from .models import Projects

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ['id', 'prj_name', 'short_desc', 'is_deleted', 'current_date', 'updated_date', 'prj_image', 'project_hosted_link']
