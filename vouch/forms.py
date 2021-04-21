from django import  forms
from vouch.models import Voucher, contact

class ConsumerForm(forms.ModelForm):
    mobile = forms.IntegerField()
    voucher = forms.CharField(max_length=8)

    class Meta:
        model=Voucher
        fields=('voucher',
                )

        model = contact
        fields = ('mobile',
                  )
