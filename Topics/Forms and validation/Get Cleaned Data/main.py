def get_cleaned_data(raw_data):
    promo_code_form = PromoCodeForm(raw_data)
    if promo_code_form.is_valid():
        return promo_code_form.cleaned_data
    return {}
