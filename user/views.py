import json
from datetime import datetime
from user.models import User
from django.utils import timezone
from django.http import HttpResponse
from django.views import View as APIView
from user.serializers import UserSerializer
# Create your views here.


class UserCreateView(APIView):
    def post(self, request, **kwargs):
        body, status = {}, 200
        age = request.POST.get('age')
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        if None in (age, name) or gender not in ('M', 'F'):
            status = 400
            body = {'message': 'name/age/gender not given or invalid'}
        timestamp = request.POST.get('timestamp', timezone.now())
        try:
            timestamp = datetime.strptime(timestamp, "%Y-%m-%d")
        except Exception as e:
            status = 400
            body = {'message': 'timestamp not in proper format'}
        if status == 200:
            user_entity = User.objects.create(
                name=request.POST.get('name'),
                age=request.POST.get('age'),
                gender=request.POST.get('gender'),
                image=request.FILES.get('image'),
                description_text=request.POST.get('description_text'),
                location=request.POST.get('location'),
                timestamp=timestamp
            )
            body = UserSerializer.serializer(user_entity)
        return HttpResponse(json.dumps(body), content_type="application/json", status=status)
