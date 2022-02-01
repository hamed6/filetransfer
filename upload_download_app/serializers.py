from rest_framework import serializers
from .models import Organization

class FileSerializer(serializers.ModelSerializer):
    class Meta():
        model=Organization
        fields= ('organization_name', 'organization_files', 'file_dlnumber')