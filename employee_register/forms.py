from django.forms import ModelForm
#from crispy forms
# https://simpleisbetterthancomplex.com/tutorial/2018/08/13/how-to-use-bootstrap-4-forms-with-django.html

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Employee
class EmployeeForm(ModelForm):
    class Meta:
        model=Employee
        fields='__all__'
        labels={
            'fullname': 'Full Name',
            'empcode': 'EMP. Code'
        }
    def __init__(self,*args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label="Select Position"
        self.fields['empcode'].required=False


