from django.shortcuts import render
from django.contrib.auth.models import User
from . forms import Item_details,Subitem_details
from . models import Item,SubItem

def item_detail(request):
	form = Item_details(request.POST or None)
	context = {"form":form}

	if form.is_valid():
		item_type = form.cleaned_data.get('item_type')
		item_id   = item_type + "_iKey"
		print(item_id)

		obj = Item(item_id = item_id, item_type = item_type)
		obj.save()

	else:
		print("item detail form invalid")

	return render(request,'item/item_detail_form.html',context)

def subitem_detail(request):
	form = Subitem_details(request.POST or None)
	context = {"form":form}

	if form.is_valid():
		subitem_name = form.cleaned_data.get('subitem_name')
		uom_desc	 = form.cleaned_data.get('uom_desc')
		uom_quantity = form.cleaned_data.get('uom_quantity')
		uom_quantity_rate = form.cleaned_data.get('uom_quantity_rate')
		subitem_id = subitem_name + "_siKey"
		item = form.cleaned_data.get('item')
		print(item)


		obj = SubItem(subitem_id=subitem_id,
						subitem_name=subitem_name, 
						uom_desc=uom_desc, 
						uom_quantity=uom_quantity, 
						uom_quantity_rate=uom_quantity_rate,
						item = item)
		obj.save()

	else:
		print("subitem detail form invalid")

	return render(request,'item/subitem_detail_form.html',context)