from django.shortcuts import render
from quadratic.forms import QuadraticForm


def quadratic_results(request):
    if request.method == 'GET':
        form = QuadraticForm(request.GET)
        disc = {}
        text_result = {}
        if form.is_valid():
            a = int(request.GET['a'])
            b = int(request.GET['b'])
            c = int(request.GET['c'])
            disc['message'] = "Дискриминант: "
            disc['value'] = b**2 - 4*a*c

            if disc['value'] < 0:
                text_result['message'] = "Дискриминант меньше нуля, уравнение не имеет действительных решений."
            elif disc['value'] == 0:
                x = (-b + disc['value'] ** (1/2.0)) / 2*a
                text_result['message'] = "Дискриминант равен нулю, уравнение имеет один действительный корень: x1=x2 = "
                text_result['value'] = x
            else:
                x1 = (-b + disc['value'] ** (1 / 2.0)) / 2*a
                x2 = (-b - disc['value'] ** (1 / 2.0)) / 2*a
                text_result['message'] = "Квадратное уравнение имеет два действительных корня: "
                text_result['value'] = u"x1 = %.1f, x2 = %.1f" % (x1, x2)

        content = {"disc": disc, "text_result": text_result, 'form': form}

        return render(request, 'quadratic/results.html', content)

    else:
        form = QuadraticForm()

    return render(request, 'quadratic/results.html', {'form': form})
