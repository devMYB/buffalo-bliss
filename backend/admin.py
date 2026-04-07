from sqladmin import Admin, ModelView, BaseView, expose
from .models import Event, AdvertisingRequest, Subscriber, Restaurant, Attraction, Recipe, Article, Magazine
from wtforms import SelectMultipleField, SelectField, Field, FileField, StringField
from wtforms.validators import ValidationError, DataRequired
import os
import shutil

#------------------------------------------------------------
# CUSTOM FIELDS AND VALIDATORS
#------------------------------------------------------------

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

#------------------------------------------------------------
# CATEGORIES
#------------------------------------------------------------

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

RECIPE_CATEGORIES = [
    ("breakfast", "Healthy Breakfast Ideas"),
    ("vegan", "Plant-Based Favorites"),
    ("vegetarian", "Plant-Based Favorites"),
    ("meal-prep", "Wellness Meal Prepping"),
    ("dinner", "Quick Weekly Dinners"),
    ("lunch", "Go-to Lunches"),
    ("dessert", "Indulgent Desserts"),
    ("other", "Good Mood Foods"),
]

ARTICLE_CATEGORIES = [
    ("health", "Health"),
    ("wealth", "Wealth"),
    ("spirit", "Spirit"),
    ("happiness", "Happiness"),
]

#------------------------------------------------------------
# EVENT ADMIN SECTION
#------------------------------------------------------------

class EventAdmin(ModelView, model=Event):
    column_list = ["id", "name", "category"]
    form_columns = [
    "name",
    "location",
    "image",
    "url",
    "description",
    "category",
    "badges",
    "month",
    "time",
    "price",
    "featured",
    "created_at",
    "updated_at",
    ]
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
        },
        "description": {
            "render_kw": {
                "placeholder": "Enter 1-2 line description",
                "class": "form-control",
            }
        },
        "image": {
            "label": "Image URL",
            "render_kw": {
                "placeholder": "Image URL (e.g., https://...)",
                "class": "form-control"
            }
        },
        "url": {
            "label": " Website URL",
            "render_kw": {
                "placeholder": "Official website URL of the event",
                "class": "form-control"
            }
        },
        "badges": {
            "label": "Badges",
            "render_kw": {
                "placeholder": "Seprated by comma e.g. Food, Local vendors, Music",
                "class": "form-control"
            }
        },
        "month": {
            "label": "Month",
            "render_kw": {
                "placeholder": "e.g., May or May-August or Year-Round or Monthly",
                "class": "form-control"
            }
        },
        "time": {
            "label": "Time",
            "render_kw": {
                "placeholder": "e.g., 11:00 AM - 3:00 PM",
                "class": "form-control"
            }
        },
        "location": {
            "label": "Location",
            "render_kw": {
                "placeholder": "e.g., Broadway Market District, Buffalo, NY",
                "class": "form-control"
            }
        },
        "price": {
            "label": "Price",
            "render_kw": {
                "placeholder": "e.g., Free or $10 or $10-20 or Varies",
                "class": "form-control"
            }
        }
    }

    async def on_model_change(self, data, model, is_created, request):
        """Convert category list back to a space-separated string before saving."""
        if "category" in data and isinstance(data["category"], list):
            data["category"] = " ".join(data["category"])
        return await super().on_model_change(data, model, is_created, request)

#------------------------------------------------------------
# ADVERTISING REQUEST ADMIN SECTION
#------------------------------------------------------------

class AdvertisingRequestAdmin(ModelView, model=AdvertisingRequest):
    column_list = ["id", "full_name", "business_name", "created_at"]
    column_sortable_list = ["created_at"]
    icon = "fa-solid fa-envelope"

#------------------------------------------------------------
# SUBSCRIBER ADMIN SECTION
#------------------------------------------------------------

class SubscriberAdmin(ModelView, model=Subscriber):
    column_list = ["id", "email", "created_at"]
    column_sortable_list = ["created_at"]
    icon = "fa-solid fa-users"

#------------------------------------------------------------
# RESTAURANT ADMIN SECTION
#------------------------------------------------------------

class RestaurantAdmin(ModelView, model=Restaurant):
    column_list = ["id", "name", "address", "badge1", "badge2", "sort_order"]
    column_sortable_list = ["sort_order", "name"]
    form_columns = ["name", "address", "image", "website_url", "description", "catchy_phrase", "badge1", "badge2", "sort_order"]
    icon = "fa-solid fa-utensils"
    name = "Restaurant"
    name_plural = "Restaurants"
    form_args = {
        "image": {
            "label": "Image",
            "render_kw": {
                "placeholder": "Image URL (e.g., https://...)",
                "class": "form-control"
            }
        },
        "website_url": {
            "label": "Website URL",
            "render_kw": {
                "placeholder": "Official Website URL of the restaurant",
                "class": "form-control"
            }
        },
        "catchy_phrase": {
            "label": "Catchy Phrase",
            "render_kw": {
                "placeholder": "e.g., Hidden Oasis",
                "class": "form-control"
            }
        }
    }
        

#------------------------------------------------------------
# ATTRACTION ADMIN SECTION
#------------------------------------------------------------

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

#------------------------------------------------------------
# RECIPE ADMIN SECTION
#------------------------------------------------------------

class RecipeAdmin(ModelView, model=Recipe):
    column_list = [
        "id",
        "name",
        "category",
        "badge1",
        "badge2",
        "sort_order",
        "featured"
    ]

    column_sortable_list = ["sort_order", "name"]

    form_columns = "__all__"

    icon = "fa-solid fa-utensils"
    name = "Recipe"
    name_plural = "Recipes"

    # Multi-select category
    form_overrides = {
        "category": MultipleSelectStringField,
    }

    create_template = "custom_create.html"
    edit_template = "custom_edit.html"

    form_args = {
        "category": {
            "choices": RECIPE_CATEGORIES,
            "validators": [validate_category_limit],
            "description": "Select up to 3 categories.",
            "render_kw": {
                "data-role": "select2-tags",
            }
        }
    }

    async def on_model_change(self, data, model, is_created, request):
        if "category" in data and isinstance(data["category"], list):
            data["category"] = " ".join(data["category"])
        return await super().on_model_change(data, model, is_created, request)

#------------------------------------------------------------
# ARTICLE ADMIN SECTION
#------------------------------------------------------------

class ArticleAdmin(ModelView, model=Article):
    column_list = [
        "id",
        "name",
        "category",
        "badge1",
        "badge2",
        "minutes",
        "sort_order",
        "featured"
    ]

    column_sortable_list = ["sort_order", "name"]

    form_columns = "__all__"

    create_template = "article_create.html"
    edit_template = "article_edit.html"

    icon = "fa-solid fa-file-lines"
    name = "Article"
    name_plural = "Articles"

    form_overrides = {
        "category": SelectField,
    }

    form_args = {
        "category": {
            "choices": ARTICLE_CATEGORIES,
        },
        "image": {
            "label": "Image URL / Path",
            "description": "Enter a URL (https://...) or a local path (assets/images/...). You can also upload a file below.",
            "render_kw": {
                "placeholder": "Enter image URL if not uploading",
                "class": "form-control"
            }
        }
    }

    async def on_model_change(self, data, model, is_created, request):
        form_data = await request.form()
        
        # Handle Image Upload (Injected via custom template JS)
        image_file = form_data.get("image_file")
        if image_file and hasattr(image_file, "filename") and image_file.filename:
            filename = image_file.filename
            # Define destination
            dest_dir = os.path.join("assets", "images")
            os.makedirs(dest_dir, exist_ok=True)
            save_path = os.path.join(dest_dir, filename)
            
            # Save file
            with open(save_path, "wb") as buffer:
                shutil.copyfileobj(image_file.file, buffer)
            
            # Store relative path in DB (overrides URL field)
            data["image"] = f"assets/images/{filename}"
            
        return await super().on_model_change(data, model, is_created, request)

#------------------------------------------------------------
# MAGAZINE ADMIN SECTION
#------------------------------------------------------------

class MagazineAdmin(ModelView, model=Magazine):
    column_list = ["id", "name", "date_label", "created_at"]
    column_sortable_list = ["name", "created_at"]
    form_columns = ["name", "date_label", "image", "file"]
    icon = "fa-solid fa-book-open"
    name = "Magazine"
    name_plural = "Magazines"

    form_overrides = {
        "image": FileField,
        "file": FileField,
    }

    form_args = {
        "name": {
            "label": "Name",
            "validators": [DataRequired()],
            "description": "Magazine issue name (e.g. March 2026)",
        },
        "date_label": {
            "label": "Date Added",
            "validators": [DataRequired()],
            "description": "Display label for the date (e.g. March 2026)",
            "render_kw": {"placeholder": "March 2026"},
        },
        "image": {
            "label": "Cover Image (Upload)",
            "description": "Upload cover image (will be saved to assets/magazines/images/)",
        },
        "file": {
            "label": "PDF File (Upload)",
            "description": "Upload magazine PDF (will be saved to assets/magazines/media/)",
        },
    }

    async def on_model_change(self, data, model, is_created, request):
        form_data = await request.form()
        
        # Handle Image Upload
        image_file = form_data.get("image")
        if image_file and hasattr(image_file, "filename") and image_file.filename:
            filename = image_file.filename
            # Define destination
            dest_dir = os.path.join("assets", "magazines", "images")
            os.makedirs(dest_dir, exist_ok=True)
            save_path = os.path.join(dest_dir, filename)
            
            # Save file
            with open(save_path, "wb") as buffer:
                shutil.copyfileobj(image_file.file, buffer)
            
            # Store relative path in DB
            data["image"] = f"assets/magazines/images/{filename}"
        elif not is_created:
            # Preserve existing image if no new upload during edit
            data["image"] = model.image
            
        # Handle PDF Upload
        pdf_file = form_data.get("file")
        if pdf_file and hasattr(pdf_file, "filename") and pdf_file.filename:
            filename = pdf_file.filename
            # Define destination
            dest_dir = os.path.join("assets", "magazines", "media")
            os.makedirs(dest_dir, exist_ok=True)
            save_path = os.path.join(dest_dir, filename)
            
            # Save file
            with open(save_path, "wb") as buffer:
                shutil.copyfileobj(pdf_file.file, buffer)
            
            # Store relative path in DB
            data["file"] = f"assets/magazines/media/{filename}"
        elif not is_created:
            # Preserve existing file if no new upload during edit
            data["file"] = model.file
            
        return await super().on_model_change(data, model, is_created, request)

#------------------------------------------------------------
# INSTRUCTIONS ADMIN SECTION
#------------------------------------------------------------

class InstructionsView(BaseView):
    name = "Instructions"
    icon = "fa-solid fa-circle-info"

    @expose("/instructions", methods=["GET"])
    async def instructions_page(self, request):
        return await self.templates.TemplateResponse(
            request, "instructions.html", {"request": request}
        )

#------------------------------------------------------------
# ADMIN SETUP SECTION
#------------------------------------------------------------

def setup_admin(app, engine, authentication_backend):
    admin = Admin(
        app, 
        engine, 
        authentication_backend=authentication_backend, 
        templates_dir="backend/templates"
    )
    admin.add_view(EventAdmin)
    admin.add_view(AdvertisingRequestAdmin)
    admin.add_view(SubscriberAdmin)
    admin.add_view(RestaurantAdmin)
    admin.add_view(AttractionAdmin)
    admin.add_view(RecipeAdmin)
    admin.add_view(ArticleAdmin)
    admin.add_view(MagazineAdmin)
    admin.add_base_view(InstructionsView)
    return admin
