# serializers.py
from rest_framework import serializers
from .models import TrainingResult


class TrainingResultserializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TrainingResult
        fields = ('type', 'filename', 'time', 'auc', 'macro', 'macro_recall', 'weighted', 'result_url')
