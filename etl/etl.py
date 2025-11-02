try:
    # %%
    import pandas as pd
    import re

    # %%
    movimentacoes = pd.read_excel('./data/raw/movimentacao-2025-11-02-09-10-19.xlsx')

    # %%
    movimentacoes['Preço unitário'] = movimentacoes['Preço unitário'].replace('-', '0')
    movimentacoes['Valor da Operação'] = movimentacoes['Valor da Operação'].replace('-', '0')

    # %%
    movimentacoes['Entrada/Saída'] = movimentacoes['Entrada/Saída'].astype('str')
    movimentacoes['Data'] = movimentacoes['Data'].astype('datetime64[ns]')
    movimentacoes['Movimentação'] = movimentacoes['Movimentação'].astype('str')
    movimentacoes['Produto'] = movimentacoes['Produto'].astype('str')
    movimentacoes['Instituição'] = movimentacoes['Instituição'].astype('str')
    movimentacoes['Quantidade'] = movimentacoes['Quantidade'].astype('float64')
    movimentacoes['Preço unitário'] = movimentacoes['Preço unitário'].astype('float64')
    movimentacoes['Valor da Operação'] = movimentacoes['Valor da Operação'].astype('float64')

    # %% [markdown]
    # Entrada = Crédito
    # 
    # Saída = Débito
    # 

    # %%
    movimentacoes.loc[movimentacoes['Entrada/Saída'] == 'Debito', 'Valor da Operação'] *= -1
    movimentacoes.loc[movimentacoes['Entrada/Saída'] == 'Debito', 'Preço unitário'] *= -1

    # %% [markdown]
    # Analizando o dataframe, notei o que eu realmente preciso para analisar as movimentações...

    # %%
    movimentacoes['Tipo'] = movimentacoes['Produto'].str.split().str[0]

    # %%
    def classificar_tipo(produto):
        if isinstance(produto, str):
            if produto.startswith('Tesouro'):
                return 'Tesouro'
            elif produto.startswith('LCI'):
                return 'LCI'
            elif produto.startswith('LCA'):
                return 'LCA'
            elif produto.startswith('CDB'):
                return 'CDB'
            elif re.match(r'\b[A-Z]{4}\d{1,2}\b', produto):  # ex: PETR4, VALE3, ITUB4
                return 'Ação'
            elif re.match(r'\b[A-Z]{4}\d{2}\b', produto):  # ex: HGLG11, MXRF11
                return 'FII'
            else:
                return 'Outro'
        return 'Desconhecido'


    # %%
    movimentacoes['Tipo'] = movimentacoes['Produto'].apply(classificar_tipo)

    # %%
    df_movimentacoes = movimentacoes[
        (movimentacoes['Movimentação'] == 'Compra') | 
        (movimentacoes['Movimentação'] == 'COMPRA / VENDA') | 
        (movimentacoes['Movimentação'] == 'Transferência - Liquidação') |
        (movimentacoes['Movimentação'] == 'APLICAÇÃO')
    ]

    # %%
    df_rendimentos = movimentacoes[
        (movimentacoes['Movimentação'] == 'Rendimento') | 
        (movimentacoes['Movimentação'] == 'Juros Sobre Capital Próprio') | 
        (movimentacoes['Movimentação'] == 'Dividendo') | 
        (movimentacoes['Movimentação'] == 'Dividendo - Transferido') | 
        (movimentacoes['Movimentação'] == 'RESGATE ANTECIPADO') | 
        (movimentacoes['Movimentação'] == 'Leilão de Fração') 
    ]

    # %%
    df_movimentacoes.to_csv('./data/processed/movimentacoes.csv', index=False)
    df_rendimentos.to_csv('./data/processed/rendimentos.csv', index=False)

    # %%
    df_movimentacoes.to_parquet('./data/analytics/movimentacoes.parquet', index=False)
    df_rendimentos.to_parquet('./data/analytics/rendimentos.parquet', index=False)

    print("\n\nArquivo de movimentações processado com sucesso.\n\n")
except(Exception) as e:
    print(f"Erro ao processar: {e}")

