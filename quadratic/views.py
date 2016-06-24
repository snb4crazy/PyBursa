from django.shortcuts import render


def quadratic_results(request):
    data = {}
    d = x1 = x2 = None
    is_valid_parameters = True

    for k, v in request.GET.items():
        try:
            data[str(k)] = int(v)
        except ValueError:
            data[str(k)] = str(v)
            is_valid_parameters = False

    if is_valid_parameters and not data['a'] == 0:
        d = data['b'] ** 2 - 4 * data['a'] * data['c']
        if d == 0:
            x1 = x2 = -data['b'] / 2.0 * data['a']
        elif d > 0:
            x1 = (-data['b'] + d ** (1 / 2.0)) / (2 * data['a'])
            x2 = (-data['b'] - d ** (1 / 2.0)) / (2 * data['a'])

    sorted_data = sorted(data.items(), key=lambda x: x[0])
    return render(request, 'results.html', {'data': sorted_data, 'd': d, 'x1': x1, 'x2': x2})
