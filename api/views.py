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
		queryset = Address.objects.values('province').annotate(group_by = Count('province')).order_by('province')
		
		for value in queryset:
			response = response + [{ 'province': value['province'] }]
	else:
		response = [{ 'error': 'invalid query params' }]
		returnStatus = status.HTTP_404_NOT_FOUND

	return Response(data = response, content_type="application/json", status = returnStatus)