from django.forms import ModelForm

from mainapp.models import FeedBack


class MailForm(ModelForm):
    class Meta:
        model = FeedBack
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''