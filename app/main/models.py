# -*- coding=utf-8 -*-

from mongoengine import (BooleanField, DateTimeField, Document,
                         EmbeddedDocument, StringField, EmbeddedDocumentListField)


class Navigator(Document):
    title = StringField(required=True)
    link = StringField(required=True)