# Introdução a Bancos de Dados PostgreSQL com PgAdmin para Iniciantes

## O que é um Banco de Dados?

Um banco de dados pode ser visualizado como uma planilha, onde as informações são organizadas em linhas e colunas. Cada dado pode ser de um tipo específico, como números, texto ou datas. As linhas normalmente representam registros, e a linguagem utilizada para interagir com bancos de dados é a SQL (Structured Query Language).

## Conceitos Chave

- **Chave Primária (Primary Key)**: Identificador único de um registro no banco de dados, garantindo a unicidade dos elementos.
- **Chave Estrangeira (Foreign Key)**: Estabelece uma relação de vinculação entre duas tabelas.

## Comandos SQL Básicos

### Inserção de Dados

```sql
INSERT INTO public.customers(first_name, last_name) VALUES ('TIM', 'ELDER');
```

**Observações:**
- A quantidade e o tipo dos valores inseridos devem corresponder aos campos especificados.
- Comandos SQL são geralmente escritos em caixa alta para melhor leitura.
- O esquema e o nome da tabela devem ser especificados claramente.
- O campo `id` é preenchido automaticamente, por ser a chave primária.

### Seleção de Dados

```sql
SELECT * FROM public.customers;
```

**Dicas:**
- Utilize `SELECT * FROM public."our customers"` para tabelas com espaços no nome.
- Substitua `*` pelos nomes das colunas para selecionar dados específicos.
- Adicione `LIMIT <número>` para limitar a quantidade de resultados retornados.

### Filtros e Condições

```sql
SELECT * FROM public.customers WHERE first_name = 'Luis';
SELECT * FROM public.customers WHERE first_name LIKE 'L%';
```

- O operador `LIKE 'L%'` busca por registros cujo `first_name` começa com "L".
- Utilize `%` para indicar "qualquer coisa" antes ou depois do caractere especificado.
- `OR` e `NOT` podem ser usados para expandir ou negar condições.

### Ordenação de Resultados

```sql
SELECT * FROM public.customers ORDER BY id ASC;
```

- `ORDER BY` organiza os resultados em ordem ascendente (`ASC`) ou descendente (`DESC`).

### Atualização de Dados

```sql
UPDATE public.customers SET last_name = 'Silver' WHERE id = '8';
```

- Utilize `UPDATE` para modificar registros existentes, especificando condições claras para evitar erros.

### Exclusão de Dados

```sql
DELETE FROM public.customers WHERE id = '3';
```

- `DELETE` remove registros. É fundamental garantir que a condição especificada esteja correta para evitar perdas de dados indesejadas.
