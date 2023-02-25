import stripe
from django.conf import settings

stripe.api_key = settings.STRIPE_SECRET_KEY
# Здесь можно создавать скидки и купоны (для примера созданы два купона и два промокода на их основе)

# first_coupon = stripe.Coupon.create(name='first_coup', percent_off=20, duration="once")
# second_coupon = stripe.Coupon.create(name='second_coup', percent_off=15, duration="once")
# first_promo = stripe.PromotionCode.create(coupon=first_coupon, code="FIRST")
# second_promo = stripe.PromotionCode.create(coupon=second_coupon, code="SECOND")

