from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# ── ViewSets (router-registered) ─────────────────────────────────────────────

class CampaignSubscriberViewSet(viewsets.ViewSet):
    """CRUD for campaign subscribers."""

    def list(self, request):
        return Response([])

    def create(self, request):
        return Response({}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        return Response({})

    def update(self, request, pk=None):
        return Response({})

    def partial_update(self, request, pk=None):
        return Response({})

    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_204_NO_CONTENT)


class CampaignDeliveryChannelViewSet(viewsets.ViewSet):
    """CRUD for campaign delivery channels."""

    def list(self, request):
        return Response([])

    def create(self, request):
        return Response({}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        return Response({})

    def update(self, request, pk=None):
        return Response({})

    def partial_update(self, request, pk=None):
        return Response({})

    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthPartnerViewSet(viewsets.ViewSet):
    """CRUD for auth partners."""

    def list(self, request):
        return Response([])

    def create(self, request):
        return Response({}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        return Response({})

    def update(self, request, pk=None):
        return Response({})

    def partial_update(self, request, pk=None):
        return Response({})

    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_204_NO_CONTENT)


class AuthPartnerTypeViewSet(viewsets.ViewSet):
    """CRUD for auth partner types."""

    def list(self, request):
        return Response([])

    def create(self, request):
        return Response({}, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        return Response({})

    def update(self, request, pk=None):
        return Response({})

    def partial_update(self, request, pk=None):
        return Response({})

    def destroy(self, request, pk=None):
        return Response(status=status.HTTP_204_NO_CONTENT)


# ── Inbound / Lead Form endpoints ─────────────────────────────────────────────

@api_view(['POST'])
def inbound_publisher(request):
    return Response({'status': 'ok'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def inbound_lead_form(request):
    return Response({'status': 'ok'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def gads_lead_form(request):
    return Response({'status': 'ok'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def zapier_inbound(request):
    return Response({'status': 'ok'}, status=status.HTTP_200_OK)


# ── Dashboard & Analytics ─────────────────────────────────────────────────────

@api_view(['GET'])
def inbound_dashboard(request):
    return Response({})


@api_view(['GET'])
def partner_dashboard(request):
    return Response({})


@api_view(['GET'])
def partner_delivery_counts(request):
    return Response({})


@api_view(['GET'])
def course_delivery_counts(request):
    return Response({})


@api_view(['GET'])
def partner_error_summary(request):
    return Response({})


@api_view(['GET'])
def partner_success_summary(request):
    return Response({})


@api_view(['GET'])
def campaignwise_partner_perf(request):
    return Response({})


@api_view(['GET'])
def sourcewise_bifurcation_summary(request):
    return Response({})


@api_view(['GET'])
def sourcewise_lead_summary(request):
    return Response({})


# ── Campaign Delivery Histories ───────────────────────────────────────────────

@api_view(['GET'])
def campaign_delivery_histories(request):
    return Response([])


@api_view(['GET'])
def campaign_delivery_history_detail(request, pk):
    return Response({'pk': pk})


# ── Delivery ──────────────────────────────────────────────────────────────────

@api_view(['GET'])
def delivery_errors(request):
    return Response([])


@api_view(['POST'])
def repush_delivery(request, pk):
    return Response({'status': 'repushed', 'pk': pk})


@api_view(['GET'])
def delivery_queue_list(request):
    return Response([])


@api_view(['GET', 'PUT', 'DELETE'])
def delivery_queue_detail(request, pk):
    return Response({'pk': pk})


# ── Auth Partners (non-ViewSet) ───────────────────────────────────────────────

@api_view(['GET', 'PUT', 'DELETE'])
def auth_partner_detail(request, pk):
    return Response({'pk': pk})


@api_view(['GET'])
def auth_partner_list(request):
    return Response([])


@api_view(['GET'])
def auth_partner_dropdown(request):
    return Response([])


# ── Auth Partner Types (non-ViewSet) ──────────────────────────────────────────

@api_view(['GET'])
def auth_partner_type_dropdown(request):
    return Response([])


# ── Authentication ────────────────────────────────────────────────────────────

@api_view(['POST'])
def user_login(request):
    return Response({'token': 'stub-token'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def get_otp(request):
    return Response({'otp': 'sent'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def verify_otp(request):
    return Response({'verified': True}, status=status.HTTP_200_OK)


@api_view(['POST'])
def user_logout(request):
    return Response({'status': 'logged out'}, status=status.HTTP_200_OK)


# ── Channels ──────────────────────────────────────────────────────────────────

@api_view(['GET'])
def partner_delivery_channels(request, pk):
    return Response([])


# ── Campaign Subscriber (non-ViewSet) ─────────────────────────────────────────

@api_view(['GET'])
def campaign_subscriber_dropdown(request):
    return Response([])


@api_view(['GET'])
def campaign_subscriber_by_partner(request, pk):
    return Response([])


@api_view(['POST'])
def toggle_subscriber_activation(request, pk):
    return Response({'status': 'toggled', 'pk': pk})


# ── Subscribers ───────────────────────────────────────────────────────────────

@api_view(['POST'])
def add_subscriber(request):
    return Response({'status': 'added'}, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def subscriber_list(request):
    return Response([])


# ── Leads ─────────────────────────────────────────────────────────────────────

@api_view(['GET'])
def get_all_leads(request):
    return Response([])


@api_view(['GET'])
def get_specific_lead(request, pk):
    return Response({'pk': pk})


# ── Test Leads ────────────────────────────────────────────────────────────────

@api_view(['GET', 'POST'])
def test_lead(request):
    return Response({})


@api_view(['GET'])
def get_specific_test_lead(request, pk):
    return Response({'pk': pk})


# ── Misc / Utility ────────────────────────────────────────────────────────────

@api_view(['GET'])
def campaigns_list(request):
    return Response([])


@api_view(['GET'])
def locations_dropdown(request):
    return Response([])


@api_view(['GET'])
def api_overview(request):
    return Response({'status': 'ok', 'message': 'API overview'})


@api_view(['GET'])
def export_csv(request):
    return Response({'format': 'csv', 'rows': []})


@api_view(['GET'])
def activity_tasks(request):
    return Response([])