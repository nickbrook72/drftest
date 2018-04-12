# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import ListCreateAPIView, GenericAPIView
from rest_framework import serializers, mixins
from rest_framework.response import Response

from drftest.models import Album, Track


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('name')


class AlbumSerializer(serializers.ModelSerializer):
    tracks = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('name', 'tracks')

    def create(self, validated_data):
        print(validated_data)
        tracks_data = validated_data.pop('tracks')
        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            Track.objects.create(album=album, **track_data)
        return album



# class DropdownStringOptionSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DropdownStringOption
#         fields = ('id', 'value', 'is_public')


class AlbumDetailView(ListCreateAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()


