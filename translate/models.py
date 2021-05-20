from django import forms


class InferForm(forms.Form):
    data_infer = forms.CharField(widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(InferForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['placeholder'] = 'Enter something funny.'
            visible.field.widget.attrs['id'] = 'text'
            visible.field.widget.attrs['name'] = 'text'
            visible.field.widget.attrs['row'] = '4'
            visible.field.widget.attrs['style'] = 'overflow: hidden; word-wrap: break-word; resize: none; height: 160px; '
