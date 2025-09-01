from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View

from quotes.models import Quote


# Create your views here.
class QuotesListView(View):
    def get(self, request, *args, **kwargs):

        # get all the quotes
        quotes = Quote.objects.all()

        # generate the context to be passed
        context = {
            "quotes": quotes,
        }

        # return the rendered view via html
        return render(request, "quotes_list.html", context=context)


class QuoteDetailView(View):
    def get(self, request, *args, **kwargs):
        quote = Quote.objects.get(pk=self.kwargs['pk'])
        context = {
            "quote": quote,
        }
        return render(request, "quote_detail.html", context=context)


class QuoteCreateView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "quote_create.html", {})

    def post(self, request, *args, **kwargs):
        q = request.POST.get("q")
        quote = Quote.objects.create(quote=q)
        return HttpResponseRedirect(reverse("quotes"))


class QuoteUpdateView(View):
    def get(self, request, *args, **kwargs):
        quote = Quote.objects.get(pk=self.kwargs['pk'])
        context = {
            "quote": quote,
        }
        return render(request, "quote_update.html", context=context)
    def post(self, request, *args, **kwargs):
        quote = Quote.objects.get(pk=self.kwargs['pk'])
        q = request.POST.get("q")
        quote.quote = q
        quote.save()
        return HttpResponseRedirect(reverse("quotes"))

class QuoteDeleteView(View):
    def get(self, request, *args, **kwargs):
        quote = Quote.objects.get(pk=self.kwargs['pk'])
        quote.delete()
        return HttpResponseRedirect(reverse("quotes"))


class QuoteRandomView(View):
    def get(self, request, *args, **kwargs):
        quote = Quote.objects.order_by("?").first()
        context = {
            "quote": quote,
        }
        return render(request, "quote_detail.html", context=context)