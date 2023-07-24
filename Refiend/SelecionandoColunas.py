import pandas as pd


#Carregando os dados

df = pd.read_csv("Truested\data-test-analytics_5_csv_truested")

#Transformando DataFrame com as colunas que preciso para minha analise

colunas_selecionadas = ['id', 'state', 'created_at', 'updated_at', 'deleted_at', 'status', 'last_date_purchase', 'average_ticket', 'items_quantity', 'all_orders', 'marketing_source']

novo_df = df[colunas_selecionadas]


#Verificando informações gerais sobre o DateFrame para verificar se houve alguma mudança da tranformação da truested para refiend
print(novo_df.info())


#Exportando novo DateFrame em formato Excel para fazer analise no power bi

novo_df.to_excel('Refiend\data-test_analytics_5_novo_df_excel_refiend.xlsx', index=False )
