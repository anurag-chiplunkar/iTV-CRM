from django import forms


class Common_DateInput(forms.DateInput):
    widgetInputType = "date"

    def __init__(self, **kwargs):
        kwargs["format"] = "%Y-%m-%d"
        super().__init__(**kwargs)
