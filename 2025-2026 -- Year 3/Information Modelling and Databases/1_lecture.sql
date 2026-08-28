-- 1_lecture.sql
-- Создание таблицы для банковских счетов

-- Создание таблицы Account с тремя полями:
-- account_nr - номер счета (целое число)
-- balance - баланс (число с 2 знаками после запятой)
-- type - тип счета (текст)
CREATE TABLE Account(
    account_nr INT,
    balance NUMERIC(9, 2),
    type TEXT
);

-- Вставка тестовых данных в таблицу
-- Два счета: один сберегательный, другой текущий
INSERT INTO Account(account_nr, balance, type)
VALUES 
    (12345, 1000.00, 'savings'),    -- Сберегательный счет с балансом 1000.00
    (67890, 2846.92, 'checking');   -- Текущий счет с балансом 2846.92

-- Запрос 1: Получить баланс для счета номер 67890
SELECT balance
FROM Account
WHERE account_nr = 67890;

-- Запрос 2: Найти номера сберегательных счетов с отрицательным балансом
SELECT account_nr
FROM Account
WHERE type = 'savings' AND balance < 0;