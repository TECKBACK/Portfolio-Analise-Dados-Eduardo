-- ==========================================================
-- PORTFÓLIO DE ANÁLISE DE DADOS (SQL)
-- Autor: Eduardo
-- Ferramentas: SQL (Sintaxe compatível com SQLite/PostgreSQL/MySQL)
-- Contexto: Análise de banco de dados de uma Loja (E-commerce)
-- ==========================================================

-- 1. VISÃO GERAL DOS PRODUTOS
-- Objetivo: Listar os produtos e seus preços para entender o catálogo.
SELECT TOP 10 ProductName, Price 
FROM Products; -- Olhando apenas os 10 primeiros para não poluir a tela

-- 2. ANÁLISE DE PREÇOS (FILTROS)
-- Objetivo: Encontrar produtos "Premium" (acima de $50).
SELECT * FROM Products
WHERE Price > 50
ORDER BY Price DESC; -- Ordenado do mais caro para o mais barato

-- 3. ANÁLISE DE CLIENTES (AGREGAÇÃO SIMPLES)
-- Objetivo: Descobrir de quais países vêm nossos clientes.
-- Pergunta de Negócio: "Quantos clientes temos em cada país?"
SELECT 
    Country, 
    COUNT(CustomerID) AS TotalClientes
FROM 
    Customers
GROUP BY 
    Country
ORDER BY 
    TotalClientes DESC; -- Países com mais clientes aparecem primeiro

-- 4. INTELIGÊNCIA DE PRODUTOS (AGREGAÇÃO AVANÇADA)
-- Objetivo: Entender a média de preço por categoria de produto.
-- Pergunta de Negócio: "Qual categoria tem os produtos mais caros em média?"
SELECT 
    CategoryID, 
    AVG(Price) AS PrecoMedio
FROM 
    Products
GROUP BY 
    CategoryID
ORDER BY 
    PrecoMedio DESC;

-- 5. EXEMPLO DE MANIPULAÇÃO DE DADOS (CUIDADO: Apenas para demonstração)
-- Comentado para evitar execução acidental no banco de produção.

/*
-- Inserindo um novo produto teste
INSERT INTO Products (ProductName, Price) 
VALUES ('Produto Teste do Eduardo', 10.50);

-- Atualizando o preço desse produto
UPDATE Products 
SET Price = 9.99 
WHERE ProductName = 'Produto Teste do Eduardo';

-- Removendo o produto teste
DELETE FROM Products 
WHERE ProductName = 'Produto Teste do Eduardo';
*/