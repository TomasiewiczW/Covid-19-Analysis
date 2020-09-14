import pandas as pd
from webmap.models import Confirmed
from webmap.models import Deaths
from webmap.models import Recovered
from webmap.models import WorldBorder


confirmed = pd.read_csv('../World_total_data/Wolrd_Confirmed.csv', error_bad_lines=False)
deaths = pd.read_csv('../World_total_data/Wolrd_Deaths.csv', error_bad_lines=False)
recovered = pd.read_csv('../World_total_data/Wolrd_Recovered.csv', error_bad_lines=False)


def run():
    print('__Confirmed__')
    for x in confirmed.iterrows():
        C = Confirmed(date=confirmed['date'][x[0]], total=confirmed['confirmed_total'][x[0]])
        print(confirmed['country'][x[0]])
        try:
            C.country = WorldBorder.objects.get(name=confirmed['country'][x[0]])
        except WorldBorder.DoesNotExist:
            C.country = None
        C.save()

    print('__Deaths__')
    for x in deaths.iterrows():
        D = Deaths(date=deaths['date'][x[0]], total=deaths['deaths_total'][x[0]])
        print(deaths['country'][x[0]])
        try:
            D.country = WorldBorder.objects.get(name=deaths['country'][x[0]])
        except WorldBorder.DoesNotExist:
            D.country = None
        D.save()

    print('__Recovered__')
    for x in recovered.iterrows():
        R = Recovered(date=recovered['date'][x[0]], total=recovered['recovered_total'][x[0]])
        print(recovered['country'][x[0]])
        try:
            R.country = WorldBorder.objects.get(name=recovered['country'][x[0]])
        except WorldBorder.DoesNotExist:
            R.country = None
        R.save()
