from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'campaign-subscribers', views.CampaignSubscriberViewSet, basename='campaign-subscriber')
router.register(r'campaign-delivery-channels', views.CampaignDeliveryChannelViewSet, basename='campaign-delivery-channel')
router.register(r'auth-partners', views.AuthPartnerViewSet, basename='auth-partner')
router.register(r'auth-partner-types', views.AuthPartnerTypeViewSet, basename='auth-partner-type')

urlpatterns = [
    # ViewSet routes (auto-generated)
    path('', include(router.urls)),

    # ── Inbound / Lead Form endpoints ────────────────────────────────────────
    path('inbound-publisher',  views.inbound_publisher,       name='inbound-publisher'),       # POST
    path('inbound/',           views.inbound_lead_form,        name='inbound-lead-form'),        # POST
    path('google-inbound',     views.gads_lead_form,           name='gads-lead-form'),           # POST
    path('zapier-inbound',     views.zapier_inbound,           name='zapier-inbound'),           # POST

    # ── Dashboard & Analytics ─────────────────────────────────────────────────
    path('inbound-dashboard',                views.inbound_dashboard,             name='inbound-dashboard'),
    path('auth-partners/dashboard',          views.partner_dashboard,             name='partner-dashboard'),
    path('partner-delivery-counts',          views.partner_delivery_counts,       name='partner-delivery-counts'),
    path('course-delivery-counts',           views.course_delivery_counts,        name='course-delivery-counts'),
    path('partner-error-summary',            views.partner_error_summary,         name='partner-error-summary'),
    path('partner-success-summary',          views.partner_success_summary,       name='partner-success-summary'),
    path('campaignwise-partner-performance', views.campaignwise_partner_perf,     name='campaignwise-partner-performance'),
    path('sourcewise-bifurcation-summary',   views.sourcewise_bifurcation_summary,name='sourcewise-bifurcation-summary'),
    path('sourcewise-lead-summary',          views.sourcewise_lead_summary,       name='sourcewise-lead-summary'),

    # ── Campaign Delivery Histories ───────────────────────────────────────────
    path('campaign-delivery-histories',                views.campaign_delivery_histories,      name='campaign-delivery-histories'),
    path('campaign-delivery-histories/<str:pk>',       views.campaign_delivery_history_detail, name='campaign-delivery-history-detail'),

    # ── Delivery ──────────────────────────────────────────────────────────────
    path('delivery-errors',                    views.delivery_errors,       name='delivery-errors'),
    path('repush-delivery/<str:pk>',           views.repush_delivery,       name='repush-delivery'),
    path('delivery-queue',                     views.delivery_queue_list,   name='delivery-queue-list'),
    path('delivery-queue/<int:pk>',            views.delivery_queue_detail, name='delivery-queue-detail'),

    # ── Auth Partners (non-ViewSet) ───────────────────────────────────────────
    path('auth-partners/detail/<int:pk>',  views.auth_partner_detail,   name='auth-partner-detail'),
    path('auth-partners/list',             views.auth_partner_list,      name='auth-partner-list'),
    path('auth-partners/dropdown',         views.auth_partner_dropdown,  name='auth-partner-dropdown'),

    # ── Auth Partner Types (non-ViewSet) ──────────────────────────────────────
    path('auth-partner-types/dropdown', views.auth_partner_type_dropdown, name='auth-partner-type-dropdown'),

    # ── Authentication ────────────────────────────────────────────────────────
    path('user-login',          views.user_login,    name='user-login'),
    path('otp/create-otp/',     views.get_otp,       name='get-otp'),
    path('otp/validate-otp/',   views.verify_otp,    name='verify-otp'),
    path('auth/logout',         views.user_logout,   name='user-logout'),

    # ── Channels ──────────────────────────────────────────────────────────────
    path('campaign-delivery-channels/auth-partner/<int:pk>', views.partner_delivery_channels, name='partner-delivery-channels'),

    # ── Campaign Subscriber (non-ViewSet) ─────────────────────────────────────
    path('campaign-subscribers/dropdown',          views.campaign_subscriber_dropdown,    name='campaign-subscriber-dropdown'),
    path('campaign-subscribers/by-partner/<int:pk>', views.campaign_subscriber_by_partner, name='campaign-subscriber-by-partner'),
    path('campaign-subscribers/<int:pk>/deactivate/', views.toggle_subscriber_activation,  name='toggle-subscriber-activation'),

    # ── Subscribers ──────────────────────────────────────────────────────────
    path('subscribers/add',  views.add_subscriber,      name='add-subscriber'),
    path('subscribers',      views.subscriber_list,     name='subscriber-list'),

    # ── Leads ─────────────────────────────────────────────────────────────────
    path('leads',            views.get_all_leads,        name='get-all-leads'),
    path('leads/<str:pk>',   views.get_specific_lead,    name='get-specific-lead'),

    # ── Test Leads ────────────────────────────────────────────────────────────
    path('test-lead',           views.test_lead,              name='test-lead'),
    path('test-lead/<str:pk>',  views.get_specific_test_lead, name='get-specific-test-lead'),

    # ── Misc / Utility ────────────────────────────────────────────────────────
    path('campaigns',            views.campaigns_list,    name='campaigns-list'),
    path('locations',            views.locations_dropdown, name='locations-dropdown'),
    path('export/csv',           views.export_csv,         name='export-csv'),
    path('activity-tasks',       views.activity_tasks,     name='activity-tasks'),
]