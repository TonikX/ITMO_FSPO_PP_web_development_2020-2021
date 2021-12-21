from rest_framework.serializers import ModelSerializer

from feedback.models import Feedback


class FeedbackSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = '__all__'


class FeedbackCreateSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['text', 'user', 'service']


class FeedbackPatchSerializer(ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['text']