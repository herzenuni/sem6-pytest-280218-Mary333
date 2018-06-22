def compose_dict(keys, values):
    if not isinstance(keys, list) or not isinstance(values, list):
        raise TypeError('Argument should be a list')

    if len(keys) > len(values):
        difference = len(keys) - len(values)
        values = values + ([None] * difference)

    return dict(zip(keys, values))