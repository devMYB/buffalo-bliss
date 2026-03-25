from sqladmin import Admin, ModelView
from .models import Event, AdvertisingRequest, Subscriber, Restaurant, Attraction
from wtforms import SelectMultipleField
from wtforms.validators import ValidationError

class MultipleSelectStringField(SelectMultipleField):
    """Custom field to handle multi-select to string conversion."""
    def process_data(self, value):
        if value and isinstance(value, str):
            self.data = value.split()
        else:
            self.data = value or []

def validate_category_limit(form, field):
    if field.data and len(field.data) > 3:
        raise ValidationError("You can select at most 3 categories.")

def validate_category_limit_2(form, field):
    if field.data and len(field.data) > 2:
        raise ValidationError("You can select at most 2 categories.")

ATTRACTION_CATEGORIES = [
    ("parks & nature", "Parks & Nature"),
    ("museums", "Museums"),
    ("historic sites", "Historic Sites"),
    ("family friendly", "Family Friendly"),
    ("arts & culture", "Arts & Culture"),
]

EVENT_CATEGORIES = [
    ("cultural", "Cultural"),
    ("art", "Art"),
    ("music", "Music"),
    ("food", "Food"),
    ("entertainment", "Entertainment"),
    ("fitness", "Fitness"),
    ("health", "Health"),
    ("wellness", "Wellness"),
    ("sports", "Sports"),
    ("faith", "Faith"),
    ("spirituality", "Spirituality"),
    ("religion", "Religion"),
]

class EventAdmin(ModelView, model=Event):
    column_list = ["id", "name", "category"]
    form_columns = "__all__"
    icon = "fa-solid fa-calendar-days"
    
    form_overrides = {
        "category": MultipleSelectStringField,
    }
    
    create_template = "custom_create.html"
    edit_template = "custom_edit.html"
    
    form_args = {
        "category": {
            "choices": EVENT_CATEGORIES,
            "validators": [validate_category_limit],
            "description": "Select up to 3 categories.",
            "render_kw": {
                "data-role": "select2-tags",
            }
        }
    }

    async def on_model_change(self, data, model, is_created, request):
        """Convert category list back to a space-separated string before saving."""
        if "category" in data and isinstance(data["category"], list):
            data["category"] = " ".join(data["category"])
        return await super().on_model_change(data, model, is_created, request)

class AdvertisingRequestAdmin(ModelView, model=AdvertisingRequest):
    column_list = ["id", "full_name", "business_name", "created_at"]
    column_sortable_list = ["created_at"]
    icon = "fa-solid fa-envelope"

class SubscriberAdmin(ModelView, model=Subscriber):
    column_list = ["id", "email", "created_at"]
    column_sortable_list = ["created_at"]
    icon = "fa-solid fa-users"

class RestaurantAdmin(ModelView, model=Restaurant):
    column_list = ["id", "name", "address", "badge1", "badge2", "sort_order"]
    column_sortable_list = ["sort_order", "name"]
    form_columns = ["name", "address", "catchy_phrase", "image", "description", "website_url", "badge1", "badge2", "sort_order"]
    icon = "fa-solid fa-utensils"
    name = "Restaurant"
    name_plural = "Restaurants"

class AttractionAdmin(ModelView, model=Attraction):
    column_list = [
        "id",
        "name",
        "address",
        "category",
        "price",
        "featured",
        "created_at"
    ]
    
    column_sortable_list = ["name", "created_at"]
    
    form_columns = "__all__"
    
    icon = "fa-solid fa-map-location-dot"
    name = "Attraction"
    name_plural = "Attractions"
    
    # Use multi-select for category (same pattern as Event)
    form_overrides = {
        "category": MultipleSelectStringField,
    }
    
    create_template = "custom_create.html"
    edit_template = "custom_edit.html"
    
    form_args = {
        "category": {
            "choices": ATTRACTION_CATEGORIES,
            "validators": [validate_category_limit_2],
            "description": "Select up to 2 categories.",
            "render_kw": {
                "data-role": "select2-tags",
            }
        }
    }

    async def on_model_change(self, data, model, is_created, request):
        """Convert category list back to a space-separated string before saving."""
        if "category" in data and isinstance(data["category"], list):
            data["category"] = " ".join(data["category"])
        return await super().on_model_change(data, model, is_created, request)

def setup_admin(app, engine, authentication_backend):
    admin = Admin(app, engine, authentication_backend=authentication_backend, templates_dir="backend/templates")
    admin.add_view(EventAdmin)
    admin.add_view(AdvertisingRequestAdmin)
    admin.add_view(SubscriberAdmin)
    admin.add_view(RestaurantAdmin)
    admin.add_view(AttractionAdmin)
    return admin
