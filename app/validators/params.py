# _*_ coding: utf-8 _*_
"""
  Created by Alimazing on 2018/6/16.
"""
from wtforms import IntegerField, StringField
from wtforms.validators import DataRequired, ValidationError

from app.validators.base import BaseValidator

__author__ = 'Alimazing'


class IDMustBePositiveInt(BaseValidator):
	id = IntegerField(validators=[DataRequired()])

	def validate_id(self, value):
		id = value.data
		if not self.isPositiveInteger(id):
			raise ValidationError(message='id must be positive integer')
		self.id.data = int(id)

class IDCollection(BaseValidator):
	ids = StringField(validators=[DataRequired()])

	def validate_ids(self, value):
		ids = value.data.split(',')
		for id in ids:
			if not self.isPositiveInteger(id):
				raise ValidationError(message='ids must be positive integers which separated by dot')
		self.ids.data = list(map(lambda x: int(x), ids))

class Count(BaseValidator):
	count = IntegerField(default='15')

	def validate_count(self, value):
		count = value.data
		if not self.isPositiveInteger(count) or not (1 <= int(count) <= 15):
			raise ValidationError(message='count必须是[1, 15]区间内 的正整数')
		self.count.data = int(count)

