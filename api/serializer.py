from rest_framework import serializers
from pages.models import Projects

## serializers here:
class ProjectsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Projects
		fields = '__all__'

