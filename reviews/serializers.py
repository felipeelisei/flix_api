from rest_framework import serializers
from reviews.models import Review

class ReviewSerielizer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = '__all__'