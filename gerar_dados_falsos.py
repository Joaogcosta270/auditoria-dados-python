import pandas as pd
from sqlalchemy import create_engine, text

conexao_url = r"mssql+pyodbc://localhost\SQLEXPRESS/auditoria?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
engine = create_engine(conexao_url)

def gerar_dados():
    print("Gerando dados de teste...")

    # -------------------------------------------------------
    # Dados do SQL Server (fonte oficial — todos corretos)
    # -------------------------------------------------------
    vendas_sql = [
        (101, 'Ana Silva',       1500.00, 'Pendente'),
        (102, 'Bruno Costa',     2300.50, 'Pendente'),
        (103, 'Carlos Sousa',     450.00, 'Pendente'),
        (104, 'Daniela Lima',     890.00, 'Pendente'),
        (105, 'Eduardo Gomes',   1200.00, 'Pendente'),
        (106, 'Fernanda Rocha',   750.00, 'Pendente'),
        (107, 'Gabriel Mendes',  3200.00, 'Pendente'),
        (108, 'Helena Vieira',    620.00, 'Pendente'),
        (109, 'Igor Pinto',      1800.00, 'Pendente'),
        (110, 'Juliana Nunes',    950.00, 'Pendente'),
        (111, 'Kevin Alves',     2100.00, 'Pendente'),
        (112, 'Larissa Campos',   480.00, 'Pendente'),
        (113, 'Marcos Teixeira', 1350.00, 'Pendente'),
        (114, 'Natalia Freitas',  870.00, 'Pendente'),
        (115, 'Otávio Carvalho', 2750.00, 'Pendente'),
        (116, 'Patricia Dias',    530.00, 'Pendente'),
        (117, 'Rafael Cunha',    1680.00, 'Pendente'),
        (118, 'Sabrina Lopes',    390.00, 'Pendente'),
        (119, 'Thiago Martins',  2200.00, 'Pendente'),
        (120, 'Ursula Ferreira',  710.00, 'Pendente'),
        (121, 'Victor Hugo',     1450.00, 'Pendente'),
        (122, 'Wanda Ribeiro',    990.00, 'Pendente'),
        (123, 'Xavier Moraes',   3100.00, 'Pendente'),
        (124, 'Yasmin Cardoso',   560.00, 'Pendente'),
        (125, 'Zeca Oliveira',   1900.00, 'Pendente'),
        (126, 'Amanda Borges',    840.00, 'Pendente'),
        (127, 'Bernardo Castro', 2400.00, 'Pendente'),
        (128, 'Camila Farias',    670.00, 'Pendente'),
        (129, 'Diego Monteiro',  1550.00, 'Pendente'),
        (130, 'Elaine Pereira',   920.00, 'Pendente'),
        (131, 'Fábio Nascimento',1750.00, 'Pendente'),
        (132, 'Giovana Melo',     430.00, 'Pendente'),
        (133, 'Henrique Saraiva',2600.00, 'Pendente'),
        (134, 'Isabela Correia',  780.00, 'Pendente'),
        (135, 'Jonas Barbosa',   1300.00, 'Pendente'),
    ]

    # -------------------------------------------------------
    # Planilha do financeiro — COM erros propositais
    # -------------------------------------------------------
    vendas_excel = [
        # Corretas
        {'id_venda': 101, 'cliente': 'Ana Silva',        'valor_pago': 1500.00},
        # Duplicada (erro)
        {'id_venda': 102, 'cliente': 'Bruno Costa',      'valor_pago': 2300.50},
        {'id_venda': 102, 'cliente': 'Bruno Costa',      'valor_pago': 2300.50},
        # Nome divergente (erro)
        {'id_venda': 103, 'cliente': 'Carlos Souza',     'valor_pago':  450.00},
        # Valor divergente (erro)
        {'id_venda': 104, 'cliente': 'Daniela Lima',     'valor_pago':  800.00},
        {'id_venda': 105, 'cliente': 'Eduardo Gomes',    'valor_pago': 1200.00},
        {'id_venda': 106, 'cliente': 'Fernanda Rocha',   'valor_pago':  750.00},
        {'id_venda': 107, 'cliente': 'Gabriel Mendes',   'valor_pago': 3200.00},
        # Valor divergente (erro)
        {'id_venda': 108, 'cliente': 'Helena Vieira',    'valor_pago':  500.00},
        {'id_venda': 109, 'cliente': 'Igor Pinto',       'valor_pago': 1800.00},
        # Nome divergente (erro)
        {'id_venda': 110, 'cliente': 'Juliana Nune',     'valor_pago':  950.00},
        {'id_venda': 111, 'cliente': 'Kevin Alves',      'valor_pago': 2100.00},
        {'id_venda': 112, 'cliente': 'Larissa Campos',   'valor_pago':  480.00},
        # Valor divergente (erro)
        {'id_venda': 113, 'cliente': 'Marcos Teixeira',  'valor_pago': 1000.00},
        {'id_venda': 114, 'cliente': 'Natalia Freitas',  'valor_pago':  870.00},
        {'id_venda': 115, 'cliente': 'Otávio Carvalho',  'valor_pago': 2750.00},
        # Ausente no Excel (ID 116 não aparece — erro)
        {'id_venda': 117, 'cliente': 'Rafael Cunha',     'valor_pago': 1680.00},
        {'id_venda': 118, 'cliente': 'Sabrina Lopes',    'valor_pago':  390.00},
        {'id_venda': 119, 'cliente': 'Thiago Martins',   'valor_pago': 2200.00},
        # Duplicada (erro)
        {'id_venda': 120, 'cliente': 'Ursula Ferreira',  'valor_pago':  710.00},
        {'id_venda': 120, 'cliente': 'Ursula Ferreira',  'valor_pago':  710.00},
        {'id_venda': 121, 'cliente': 'Victor Hugo',      'valor_pago': 1450.00},
        {'id_venda': 122, 'cliente': 'Wanda Ribeiro',    'valor_pago':  990.00},
        {'id_venda': 123, 'cliente': 'Xavier Moraes',    'valor_pago': 3100.00},
        # Valor divergente (erro)
        {'id_venda': 124, 'cliente': 'Yasmin Cardoso',   'valor_pago':  400.00},
        {'id_venda': 125, 'cliente': 'Zeca Oliveira',    'valor_pago': 1900.00},
        {'id_venda': 126, 'cliente': 'Amanda Borges',    'valor_pago':  840.00},
        # Nome divergente (erro)
        {'id_venda': 127, 'cliente': 'Bernardo Castros', 'valor_pago': 2400.00},
        {'id_venda': 128, 'cliente': 'Camila Farias',    'valor_pago':  670.00},
        {'id_venda': 129, 'cliente': 'Diego Monteiro',   'valor_pago': 1550.00},
        {'id_venda': 130, 'cliente': 'Elaine Pereira',   'valor_pago':  920.00},
        # Ausente no Excel (ID 131 não aparece — erro)
        {'id_venda': 132, 'cliente': 'Giovana Melo',     'valor_pago':  430.00},
        {'id_venda': 133, 'cliente': 'Henrique Saraiva', 'valor_pago': 2600.00},
        {'id_venda': 134, 'cliente': 'Isabela Correia',  'valor_pago':  780.00},
        {'id_venda': 135, 'cliente': 'Jonas Barbosa',    'valor_pago': 1300.00},
    ]

    # -------------------------------------------------------
    # Popular o SQL Server
    # -------------------------------------------------------
    try:
        with engine.begin() as conn:
            conn.execute(text("DELETE FROM vendas"))
            for v in vendas_sql:
                conn.execute(
                    text("INSERT INTO vendas (id_venda, cliente, valor_original, status_sistema) VALUES (:id, :cli, :val, :sts)"),
                    {"id": v[0], "cli": v[1], "val": v[2], "sts": v[3]}
                )
        print(f"-> SQL Server populado com {len(vendas_sql)} registros!")
    except Exception as e:
        print(f"Erro ao popular SQL Server: {e}")
        return

    # -------------------------------------------------------
    # Gerar a planilha do financeiro
    # -------------------------------------------------------
    df = pd.DataFrame(vendas_excel)
    df.to_excel('Planilhas_financeiro.xlsx', index=False)
    print(f"-> Planilha gerada com {len(vendas_excel)} linhas (incluindo erros propositais)!")
    print("\nErros inseridos propositalmente:")
    print("  - ID 102: Duplicado")
    print("  - ID 103: Nome divergente (Sousa → Souza)")
    print("  - ID 104: Valor divergente (890 → 800)")
    print("  - ID 108: Valor divergente (620 → 500)")
    print("  - ID 110: Nome divergente (Nunes → Nune)")
    print("  - ID 113: Valor divergente (1350 → 1000)")
    print("  - ID 116: Ausente na planilha")
    print("  - ID 120: Duplicado")
    print("  - ID 124: Valor divergente (560 → 400)")
    print("  - ID 127: Nome divergente (Castro → Castros)")
    print("  - ID 131: Ausente na planilha")

if __name__ == '__main__':
    gerar_dados()