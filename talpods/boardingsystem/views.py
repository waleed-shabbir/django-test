from rest_framework.views import APIView
from rest_framework.response import Response

from .serialzers import BoardingPassSerializer
from .controllers import BoardingPassesSorter
import json


class BoardingPassSort(APIView):
    def post(self, request, *args, **kwargs):
        """
        This API recieves a list of json objects of BoardingPass as input
        and it returns the sorted list of BoardingPass objects as json
		"""
        json_body = json.loads(request.body)
        if len(json_body) > 0:
            serializer = BoardingPassSerializer(data=json_body, many=True)
            if serializer.is_valid():
                sorter = BoardingPassesSorter(serializer.save())
                sorter.sort()
                result_set = sorter.get_sorted_cards()
                result = [r.as_json() for r in result_set]
            else:
                return Response({
                    "data": [],
                    "message": "Input data is invalid",
                    "code": 403
                }, status=403)
        else:
            return Response({
                "data": [],
                "message": "Input cannot be empty",
                "code": 403
            }, status=403)

        return Response({
            "data": result,
            "message": "Success",
            "code": 200
        }, status=200)
