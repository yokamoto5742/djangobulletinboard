from django import forms


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control me-2', 'placeholder': 'キーワードを入力', 'aria-label': 'Search'}))
