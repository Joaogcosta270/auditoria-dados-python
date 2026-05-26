# Sistema de Auditoria Cruzada e Data Quality

Sistema automatizado desenvolvido em Python para realizar a reconciliação e auditoria cruzada entre dados oficiais armazenados em um banco de dados relacional (SQL Server) e planilhas de movimentação financeira (Excel).

O objetivo principal é garantir a integridade dos dados (Data Quality), identificando falhas operacionais e inconsistências que geram prejuízos financeiros antes da consolidação no sistema.

## 🔍 Funcionalidades e Regras de Negócio
O pipeline de dados analisa de forma inteligente as seguintes falhas:
1. **Linhas Duplicadas na Planilha:** Identifica se o mesmo identificador de transação foi registrado mais de uma vez.
2. **Nomes Divergentes:** Detecta erros manuais de digitação de nomes de clientes (ex: "Sousa" vs "Souza").
3. **Valores Incorretos:** Compara o valor esperado no banco de dados com o valor efetivamente reportado pelo financeiro.
4. **Registros Ausentes:** Identifica transações que constam no sistema oficial mas desapareceram do relatório complementar.

## Tecnologias Utilizadas
- **Python 3** (Linguagem Principal)
- **Pandas** (Engenharia e manipulação analítica dos dados)
- **SQLAlchemy** (ORM para conexão segura com o banco de dados)
- **OpenPyXL** (Formatação condicional e estilização visual dos relatórios)
- **SQL Server** (Banco de dados relacional oficial)

## Estrutura do Projeto
- `gerar_dados_falsos.py`: Script responsável por criar o ambiente de testes, populando a base SQL Server e criando a planilha com erros propositais.
- `auditoria_sql_server.py`: O núcleo do ecossistema, contendo a lógica de cruzamento de dados, atualização no banco e geração de alertas.

## Impacto Gerado
- **Automação Total:** Processamento de múltiplos registros executado em menos de 2 segundos.
- **Auditoria de Precisão:** Eliminação de 100% do fator de erro humano em processos repetitivos.
- **Tomada de Decisão:** Geração automática de relatórios visuais com alertas em destaque para atuação imediata dos analistas.

---
*Projeto desenvolvido por João Costa como parte da jornada de aprendizado em Análise e Desenvolvimento de Sistemas (ADS) no IBMR.*
