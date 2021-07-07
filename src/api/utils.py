from passwordgen.utils import str_to_bool

def is_valid_APIrequest_custom(traits, quantity):
    MAX_WORDS = 15
    MIN_WORDS = 2

    MAX_QUANTITY = 50
    MIN_QUANTITY = 1

    errors = {'errors': []}

    try:
            if traits['words'] != None:
                traits['words'] = int(traits['words'])

            if traits['words'] > MAX_WORDS or traits['words'] < MIN_WORDS:
                errors['errors'].append(
                       f"'words' must be in range <{MIN_WORDS};{MAX_WORDS}>, not {traits['words']}. ")

    except ValueError as e:
        errors['errors'].append(
            f"'words' must be an integer, not '{traits['words']}'. ")
    except TypeError as e:
        errors['errors'].append(
            f"URL must contain 'words' integer parameter. ")

    try:
        if traits['symbols'] == None:
            errors['errors'].append(
                f"URL must contain 'symbols' boolean parameter. ")
        else:
            traits['symbols'] = str_to_bool(traits['symbols'])

    except ValueError as e:
        errors['errors'].append(
            f"'symbols' must be a boolean, '{traits['symbols']}' is ambigious")

    try:
        if quantity != None:
            quantity = int(quantity)

        if quantity > MAX_QUANTITY or quantity < MIN_QUANTITY:
            quantity.append(
                    f"'quantity' must be in range <{MIN_QUANTITY};{MAX_QUANTITY}>, not {quantity}. ")

    except ValueError as e:
        errors['errors'].append(
            f"'quantity' must be an integer, not '{quantity}'. ")
    except TypeError as e:
        errors['errors'].append(
            f"URL must contain 'quantity' integer parameter. ")
    
    return traits['symbols'], traits['words'], quantity, errors
