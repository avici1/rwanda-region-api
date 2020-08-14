import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count

from api.models import Address

@api_view(['GET'])
def index(request):
	queryset = []
	response = [];
	returnStatus = status.HTTP_200_OK

	data = request.GET
	count = len(data)

	if 'province' not in data and count != 1:
		queryset = Address.objects.values('province') \
								  .annotate(group_by = Count('province')) \
								  .order_by('province')
		
		if queryset.count() > 0:
			for value in queryset:
				obj = [{ 'province': value['province'] }]
				response = response + obj
		else:
			response = [{ 'error': 'invalid province' }]
	elif 'province' in data and count == 1:
		queryset = Address.objects.values('province', 'district') \
								  .annotate(group_by = Count('province')) \
								  .filter(province = data['province']) \
								  .order_by('district')

		if queryset.count() > 0:
			for value in queryset:
				obj = [{ 
					'province': value['province'], 
					'district': value['district'] 
				}]

				response = response + obj
		else:
			response = [{ 'error': 'invalid province' }]
	elif 'district' in data and count == 1:
		queryset = Address.objects.values('province', 'district', 'sector') \
								  .annotate(group_by = Count('district')) \
								  .filter(district = data['district']) \
								  .order_by('sector')

		if queryset.count() > 0:
			for value in queryset:
				obj = [{ 
					'province': value['province'], 
					'district': value['district'], 
					'sector': value['sector'] 
				}]

				response = response + obj
		else:
			response = [{ 'error': 'invalid district' }]
	elif 'sector' in data and count == 1:
		queryset = Address.objects.values('province', 'district', 'sector', 'cell') \
								  .annotate(group_by = Count('sector')) \
								  .filter(sector = data['sector']) \
								  .order_by('cell')

		if queryset.count() > 0:
			for value in queryset:
				obj = [{ 
					'province': value['province'], 
					'district': value['district'], 
					'sector': value['sector'],
					'cell': value['cell']
				}]

				response = response + obj
		else:
			response = [{ 'error': 'invalid sector' }]
	elif 'cell' in data and count == 1:
		queryset = Address.objects.values('province', 'district', 'sector', 'cell', 'village') \
								  .annotate(group_by = Count('cell')) \
								  .filter(cell = data['cell']) \
								  .order_by('village')

		if queryset.count() > 0:
			for value in queryset:
				obj = [{ 
					'province': value['province'], 
					'district': value['district'], 
					'sector': value['sector'],
					'cell': value['cell'],
					'village': value['village']
				}]

				response = response + obj
		else:
			response = [{ 'error': 'invalid cell' }]
	else:
		response = [{ 'error': 'invalid query params' }]
		returnStatus = status.HTTP_404_NOT_FOUND

	return Response(data = response, content_type="application/json", status = returnStatus)