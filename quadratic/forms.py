from django import forms


class QuadraticForm(forms.Form):

    a = forms.IntegerField(
        label='коэффициент a', required=True, widget=forms.TextInput({ "placeholder": "Enter a whole number"}))
    b = forms.IntegerField(
        label='коэффициент b', required=True, widget=forms.TextInput({ "placeholder": "Enter a whole number"}))
    c = forms.IntegerField(
        label='коэффициент c', required=True, widget=forms.TextInput({ "placeholder": "Enter a whole number"}))

    def clean_a(self):
        data = self.cleaned_data['a']
        if int(data) is 0:
            msg = u"коэффициент при первом слагаемом уравнения не может быть равным нулю"
            self.add_error('a', msg)
        return data
