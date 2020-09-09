import pandas as pd
from webmap.models import GDP
from webmap.models import Bloodtype
from webmap.models import Healthcare
from webmap.models import Smoking
from webmap.models import WorldBorder


gdp = pd.read_csv('../supplemental_data/transformed/gdp.csv')
bloodtypes = pd.read_csv('../supplemental_data/transformed/bloodtypes.csv')
healthcare = pd.read_csv('../supplemental_data/transformed/healthcare_rank.csv', engine='python')
smoking_rate = pd.read_csv('../supplemental_data/transformed/smoking_rate.csv')

def run():
    print('__GPD__')
    for x in gdp.iterrows():
        G = GDP(rank=gdp['rank'][x[0]], gdpPerCapita=gdp['gdpPerCapita'][x[0]])
        print(gdp['country'][x[0]])
        try:
            G.country = WorldBorder.objects.get(name=gdp['country'][x[0]])
        except WorldBorder.DoesNotExist:
            G.country = None
        #G.save()

    print('___Bloodtype___')
    for x in bloodtypes.iterrows():
        B = Bloodtype(Ominus=bloodtypes['Ominus'][x[0]], Oplus=bloodtypes['Oplus'][x[0]], Aminus=bloodtypes['Aminus'][x[0]], Bminus=bloodtypes['Bminus'][x[0]], Bplus=bloodtypes['Bplus'][x[0]], ABminus =bloodtypes['ABminus'][x[0]], ABplus=bloodtypes['ABplus'][x[0]])
        print(bloodtypes['country'][x[0]])
        try:
            B.country = WorldBorder.objects.get(name=bloodtypes['country'][x[0]])
        except WorldBorder.DoesNotExist:
            B.country = None
        B.save()

    print('___Healthcare___')
    for x in healthcare.iterrows():
        H = Healthcare(rank=healthcare['rank'][x[0]], score=healthcare['score'][x[0]])
        print(healthcare['country'][x[0]])
        try:
            H.country = WorldBorder.objects.get(name=healthcare['country'][x[0]])
        except WorldBorder.DoesNotExist:
            H.country = None
        H.save()

    print('___Smoking___')
    for x in smoking_rate.iterrows():
        S = Smoking(male=smoking_rate['male'][x[0]], female=smoking_rate['female'][x[0]], total=smoking_rate['total'][x[0]])
        print(smoking_rate['country'][x[0]])
        try:
            S.country = WorldBorder.objects.get(name=smoking_rate['country'][x[0]])
        except WorldBorder.DoesNotExist:
            S.country = None
        S.save()

