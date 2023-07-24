import pandas as pd
import numpy as np

#Carregando os dados

df = pd.read_csv("Raw\data-test-analytics_5.csv")

#Verificando se há dados nulos
print(df.isnull().sum())

#Verificando informações gerais sobre o DateFrame
print(df.info())

#Verificando estatíscas básicas dos dados
print(df.describe())


#Fazendo a tipagem dos dados que contém datas

df['created_at'] = pd.to_datetime(df['created_at'])
df['updated_at'] = pd.to_datetime(df['updated_at'])
df['deleted_at'] = pd.to_datetime(df['deleted_at'])
df['last_date_purchase'] = pd.to_datetime(df['last_date_purchase'])

df.to_csv("Truested/data-test-analytics_5_csv_truested")