from django import template
from reviews_list.models import Reviews_list
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def calculate_rating(current_product):
        reviews = Reviews_list.objects.filter(product=current_product)
        review_avg = 0
        # if product has greater reviews than 0...
        if len(reviews) > 0:
            for review in reviews:
                review_avg += review.review_rating
            review_avg = review_avg / len(reviews)
            review = '<small class="text-muted">' \
                '<i class="fas fa-star mr-1"></i>%d / 5</small>' \
                % review_avg
        else:
            review = '<small class="text-muted">No Rating</small>'

        # mark a string as safe for (HTML) output purposes.
        return mark_safe(review)
