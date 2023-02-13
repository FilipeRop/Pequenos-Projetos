-- CRIANDO O BANCO DE DADOS
create database ESTANTE_LIVROS
owner POSTGRES
tablespace PG_DEFAULT
template TEMPLATE1
encoding UTF8

-- drop
drop table if exists estante;

-- CRIANDO TABELAS

--Tabela ESTANTE
create table ESTANTE(
	id_estante INT not null,
	
	primary key (id_estante)
);

--Tabela GENERO
create table GENERO(
	id_genero INT not null generated always as identity,
	genero VARCHAR(50),
	id_estante INT not null,
	
	primary key (id_genero),
		constraint fk_estante
			foreign key (id_estante)
				references estante (id_estante)
);

--Tabela LIVRO
create table LIVRO(
	id_livro INT not null generated always as identity,
	titulo_livro VARCHAR (50) not null,
	autor_livro VARCHAR (20) not null,
	paginas_livro INT not null,
	id_estante INT not null,
	
	primary key (id_livro),
		constraint fk_estante
			foreign key (id_estante)
				references estante (id_estante)
);

-- INSERINDO VALORES 

--Tabela Estante 
-- Não utilizei geração automática, pois o número de estantes é fixo e ordenano de forma específica
-- Se o número de estantes aumentar, basta acrescenter um valor a essa tabela

insert into estante (id_estante)
values(1);
insert into estante (id_estante)
values(2);
insert into estante (id_estante)
values(3);
insert into estante (id_estante)
values(4);
insert into estante (id_estante)
values(5);
insert into estante (id_estante)
values(6);

--Tabela Genero


insert into genero (genero, id_estante)
values('Matemática/Cálculo', 1);
insert into genero (genero, id_estante)
values('Física/Química', 2);
insert into genero (genero, id_estante)
values('Religião/História', 3);
insert into genero (genero, id_estante)
values ('Literatura Luso-Brasileira', 4);
insert into genero (genero, id_estante)
values ('Literatura Estrangeira', 5);
insert into genero (genero, id_estante)
values ('Filosofia', 6);

--Tabela Livro

insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Matemática - Pensar e Descobrir 6ºano', 'Giovanni JR.', 399, 1);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Matemática - Pensar e Descobrir 7ºano', 'Giovanni JR.', 367, 1);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Matemática - Pensar e Descobrir 8ºano', 'Giovanni JR.', 415, 1);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Matemática - Pensar e Descobrir 9ºano', 'Giovanni JR.', 384, 1);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Matemática 1 - 2°Grau', 'Giovanni/Bonjorno', 263, 1);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Matemática 3 - 2°Grau', 'Giovanni/Bonjorno', 341, 1);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Cálculo com Geometria Analítica', 'Simmons', 829, 1);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Cálculo - Volume 1', 'James Stewart', 692, 1);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Cálculo - Volume 2', 'James Stewart', 651, 1);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Circuitos Elétricos', 'Dorf/Svoboda', 795, 1);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Física Clássica - Cinemática', 'Calçada/Sampaio', 332, 2);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Física Clássica - Dinâmica e Estática', 'Calçada/Sampaio', 507, 2);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Física Clássica - Eletricidade', 'Calçada/Sampaio', 630, 2);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Física Clássica - Óptica e Ondas', 'Calçada/Sampaio', 561, 2);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Bíblia Sagrada - ACF', 'N/A', 942, 3);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Bíblia Sagrada - Tradução em Guarani', 'N/A', 1564, 3);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Alcorão Sagrada - Tradução em Português', 'N/A', 489, 3);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Tao Te King', 'Lao-Tse', 96, 3);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('All the Men of the Bible', 'Lockyer', 381, 3);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('The Amplified New Testament', 'N/A', 983, 3);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Brasil: De Getúlio a Castelo', 'Thomas Skidmore', 512, 3);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Era dos Extremos', 'Eric Hobsbawm', 598, 3);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('O Primo Basílio', 'Eça de Queirós', 250, 4);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Vidas Secas', 'Graciliano Ramos', 155, 4);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Os Sertões', 'Euclides da Cunha', 297, 4);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('A Pata da Gazela', 'José de Alencar', 160, 4);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Triste Fim de Policarpo Quaresma', 'Lima Barreto', 237, 4);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Quincas Borba', 'Machado de Assis', 223, 4);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Esaú e Jacó', 'Machado de Assis', 247, 4);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Poemas Escolhidos', 'Fernando Pessoa', 191, 4);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Auto da Barca do Inferno', 'Gil Vicente', 81, 4);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Os Lusíadas', 'Camões', 325, 4);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Contos Inacabados', 'J.R.R. Tolkien', 622, 5);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('O Hobbit', 'J.R.R. Tolkien', 331, 5);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Box O Senhor dos Anéis', 'J.R.R. Tolkien', 1678, 5);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('As Crônicas de Nárnia', 'C.S. Lewis', 751, 5);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Os Sofrimentos do Jovem Werther', 'Goethe', 185, 5);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('O Castelo', 'Franz Kafka', 361, 5);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('A Metamorfose', 'Franz Kafka', 138, 5);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Crime e Castigo', 'Dostoiévski', 591, 5);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Confissões', 'Santo Agostinho', 288, 6);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('As Sete Astes Liberais', 'Paul Abelson', 196, 6);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('A República', 'Platão', 366, 6);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('A Política', 'Aristóteles', 301, 6);
insert into livro(titulo_livro, autor_livro, paginas_livro, id_estante)
values ('Ortodoxia', 'G.K. Chesterton', 204, 6);


-- UPDATE - ALTERANDO VALORES NA TABELA

update livro 
set titulo_livro  = 'Dom Casmurro'
where id_livro  = 28

update livro 
set paginas_livro = 271
where id_livro = 28

-- DELETE - DELETANDO VALORES NA TABELA

delete from livro 
where id_livro  = 22;

--Querry 

select *
from livro 
where paginas_livro > 200

-- Querry usando join

select livro.titulo_livro, livro.autor_livro, genero.genero, genero.id_estante 
from livro join genero on genero.id_estante = livro.id_estante 
