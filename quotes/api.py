from ninja import NinjaAPI
from .models import Quote
from .schemas import QuoteSchema

app = NinjaAPI()

@app.get("/", response=list[QuoteSchema])
def list_quotes(request):
    return Quote.objects.all()

@app.get("/{id}/", response=QuoteSchema)
def detail_quote(request, id: int):
    return Quote.objects.get(id=id)