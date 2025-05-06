from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from .serializers import RiskAssessmentSerializer
from .services import calculate_risk_score
from .models import RiskAssessment

class RiskScoreView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = RiskAssessmentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Calculate risk score
        risk_data = calculate_risk_score(serializer.validated_data)
        
        # Save the assessment
        assessment = RiskAssessment(
            **serializer.validated_data,
            risk_score=risk_data['risk_score'],
            risk_breakdown=risk_data['risk_breakdown']
        )
        assessment.save()
        
        return Response({
            'risk_score': risk_data['risk_score'],
            'risk_breakdown': risk_data['risk_breakdown']
        }, status=status.HTTP_200_OK)