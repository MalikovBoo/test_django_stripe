import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY
# здесь можно создавать налоги на продажу

# second_tax = stripe.TaxRate.create(
#   display_name="First Tax",
#   inclusive=False,
#   percentage=17.25,
#   description="First Sales Tax",
# )
