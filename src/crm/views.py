from django.shortcuts import render

from cms.models import CmsSlider
from crm.models import Order
from .forms import OrderForm
from price.models import PriceTable, PriceCard
from telegrambot.sendmessage import send_message


def index(request):
	slider_list = CmsSlider.objects.all()
	price_cards = PriceCard.objects.all()
	pc_1 = price_cards[0]
	pc_2 = price_cards[1]
	pc_3 = price_cards[2]
	price_table = PriceTable.objects.all()
	form = OrderForm()
	context = {
		'slider_list': slider_list,
		'pc_1': pc_1,
		'pc_2': pc_2,
		'pc_3': pc_3,
		'price_table': price_table,
		'form': form,
	}
	return render(request, 'index.html', context=context)


def thanks(request):
	if request.POST:
		name = request.POST['name']
		phone = request.POST['phone']
		account = Order(order_name=name, order_phone=phone)
		account.save()
		send_message(tg_name=name, tg_phone=phone)
		context = {
			'name': name,
			'phone': phone
		}
		return render(request, 'thanks.html', context)
	else:
		return render(request, 'thanks.html')
