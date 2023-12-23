from rest_framework import serializers
from hlo.models import ContactUs

class ContactusSerilizer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = "__all__"
        # fields = ["id", "name"]