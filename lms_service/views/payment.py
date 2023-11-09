from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveAPIView, DestroyAPIView, ListAPIView

from lms_service.models import Payment
from lms_service.serializers.payment import PaymentSerializer


class PaymentCreateView(CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentUpdateView(UpdateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentRetrieveView(RetrieveAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class PaymentDestroyView(DestroyAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer


class PaymentListView(ListAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['paid_course', 'paid_lesson', 'payment_method']
    ordering_fields = ['pay_date']