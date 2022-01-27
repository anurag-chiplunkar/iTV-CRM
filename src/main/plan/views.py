from django.shortcuts import render
from django.contrib.auth.models import User
from . forms import Plan_details
from . models import Plan

def plan_detail(request):
	form = Plan_details(request.POST or None)
	context = {"form":form}

	if form.is_valid():
		plan_desc = form.cleaned_data.get('plan_desc')
		p_id = plan_desc + "_pKey"
		print(p_id)

		customertype = form.cleaned_data.get('customertype')
		item = form.cleaned_data.get('item')
		subitem = form.cleaned_data.get('subitem')

		obj = Plan(p_id = p_id,
						plan_desc = plan_desc,
						customertype = customertype,
						item = item,
						subitem = subitem
							)
		obj.save()

	else:
		print("plan detail form invalid")

	return render(request,'plan/plan_detail_form.html',context)
