
from rest_framework import serializers
from mapapp.models import GeoData_table, LANGUAGE_CHOICES, LEXERS, STYLE_CHOICES

#MapappSerializer class is replicating a lot of information that's also contained in the Attendance_table model
class GeoData_tableSerializer(serializers.ModelSerializer):
    class Meta:
        model=GeoData_table
        fields = ('id','user_id','created','lat','lng')