from ninja import ModelSchema
from .models import Quote

class QuoteSchema(ModelSchema):
    class Meta:
        model = Quote
        fields = '__all__'