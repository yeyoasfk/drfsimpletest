from rest_framework import serializers
from .models import Project

class ProjectSerializer(serializers.ModelSerializer):#combierte modelos en datos consultables
    class Meta:
        model = Project
        fields = ('id','title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at',)#campo solo de lectura, no se edita
