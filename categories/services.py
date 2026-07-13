from .models import Category
from .constants import DEFAULT_CATEGORIES

def create_default_categories(user):
    for category in DEFAULT_CATEGORIES:
        Category.objects.get_or_create(
            user=user,
            name=category["name"],
            defaults={
                "category_type": category["category_type"],
                "color": category["color"],
                "icon": category["icon"],
            },
        )