from django import forms

class WhizForm(forms.Form):
    whiz_input = forms.CharField(label="", widget=forms.Textarea(attrs={"cols": '',
                                                              "rows": '',
                                                              "id": "message",
                                                              "placeholder":"Write a post!",
                                                               "value": "message"}))