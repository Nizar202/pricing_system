from django import forms

class OfferForm(forms.Form):
    association_name = forms.CharField(label='اسم الجمعية', max_length=100)
    customer_address = forms.CharField(label='عنوان العميل', max_length=100)
    service_name = forms.CharField(label='اسم الخدمة', max_length=100)
    service_price = forms.DecimalField(label='سعر الخدمة')
    quantity = forms.IntegerField(label='الكمية', min_value=1)
    total_price = forms.DecimalField(label='السعر الإجمالي', required=False)

    def clean(self):
        cleaned_data = super().clean()
        service_price = cleaned_data.get("service_price")
        quantity = cleaned_data.get("quantity")
        if service_price and quantity:
            cleaned_data['total_price'] = service_price * quantity
        return cleaned_data
