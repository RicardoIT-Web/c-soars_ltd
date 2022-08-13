"""Set Payment signals"""
from django.apps import AppConfig


class PaymentConfig(AppConfig):
    """Set Payment signals"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "payment"

    def ready(self):
        import payment.signals
