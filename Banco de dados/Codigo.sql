create schema PetShop;
use PetShop;


create table fornecedor (
nome varchar(45),
cnpj varchar(45),
PRIMARY KEY(cnpj)
);

create table produto (
codigo_barras varchar(45),
nome varchar (45),
PRIMARY KEY(codigo_barras)
);

create table fornecedor_produto (
cnpj varchar(45) NOT NULL,
codigo_barras varchar(45) NOT NULL,
primary key(cnpj, codigo_barras),
CONSTRAINT fk_cnpj FOREIGN KEY (cnpj) REFERENCES fornecedor(cnpj),
CONSTRAINT fk_codigo_barras FOREIGN KEY (codigo_barras) REFERENCES produto(codigo_barras)
);

create table funcionario(
nome varchar(45),
cpf varchar(45),
primary key(cpf)
);

create table estoque (
codigo_barras varchar(45),
primary key (codigo_barras),
quantidade int,
cpf varchar(45) NOT NULL,
CONSTRAINT fk1_codigo_barras FOREIGN KEY (codigo_barras) REFERENCES produto(codigo_barras),
CONSTRAINT fk_cpf_funcionario FOREIGN KEY (cpf) REFERENCES funcionario(cpf)
);

create table tutor (
nome varchar(45),
telefone varchar(45),
primary key(telefone)
);

create table venda (
valor int,
nota_fiscal int,
primary key(nota_fiscal),
cpf varchar(45) NOT NULL,
telefone varchar(45) NOT NULL,
CONSTRAINT fk1_cpf_funcionario FOREIGN KEY (cpf) REFERENCES funcionario(cpf),
CONSTRAINT fk_telefone_tutor FOREIGN KEY (telefone) REFERENCES tutor(telefone)
);

create table categoria_pet(
codigo_categoria int AUTO_INCREMENT,
especie varchar(45),
porte varchar(45),
primary key(codigo_categoria)
);

create table pet(
nome varchar(45),
idade int,
id_pet int AUTO_INCREMENT,
primary key(id_pet),
ficha_medica varchar(45),
raca varchar(45),
codigo_categoria int NOT NULL,
CONSTRAINT fk_codigo_categoria FOREIGN KEY (codigo_categoria) REFERENCES categoria_pet(codigo_categoria)
);

create table servico (
id_servico int auto_increment,
tipo varchar(45),
primary key(id_servico)
);

create table cargo (
id_cargo int auto_increment,
funcao varchar(45),
primary key(id_cargo)
);

create table cargo_funcionario (
id_cargo int NOT NULL,
cpf varchar(45) NOT NULL,
primary key(id_cargo, cpf),
CONSTRAINT fk_id_cargo FOREIGN KEY (id_cargo) REFERENCES cargo(id_cargo),
CONSTRAINT fk5_cpf_funcionario FOREIGN KEY (cpf) REFERENCES funcionario(cpf)
);

create table produto_venda(
nota_fiscal int NOT NULL,
codigo_barras varchar(45) NOT NULL,
primary key(nota_fiscal, codigo_barras),
quantidade int,
CONSTRAINT fk1_nota_fiscal FOREIGN KEY (nota_fiscal) REFERENCES venda(nota_fiscal),
CONSTRAINT fk2_codigo_barras FOREIGN KEY (codigo_barras) REFERENCES produto(codigo_barras)
);

create table pet_tutor(
id_pet int NOT NULL,
telefone_tutor varchar(45) NOT NULL,
primary key(id_pet, telefone_tutor),
CONSTRAINT fk1_id_pet FOREIGN KEY (id_pet) REFERENCES pet(id_pet),
CONSTRAINT fk3_telefone_tutor FOREIGN KEY (telefone_tutor) REFERENCES tutor(telefone)
);

create table venda_servico (
nota_fiscal int NOT NULL,
id_servico int NOT NULL,
primary key(nota_fiscal, id_servico),
CONSTRAINT fk2_nota_fiscal FOREIGN KEY (nota_fiscal) REFERENCES venda(nota_fiscal),
CONSTRAINT fk2_id_servico FOREIGN KEY (id_servico) REFERENCES servico(id_servico)
);

create table agendamento (
n_agendamento int auto_increment,
horario time,
data_ date,
id_cargo int NOT NULL,
telefone_tutor varchar(45) NOT NULL,
id_pet int NOT NULL,
primary key(n_agendamento),
CONSTRAINT fk2_id_cargo FOREIGN KEY (id_cargo) REFERENCES cargo(id_cargo),
CONSTRAINT fk2_telefone_tutor FOREIGN KEY (telefone_tutor) REFERENCES tutor(telefone),
CONSTRAINT fk2_id_pet FOREIGN KEY (id_pet) REFERENCES pet(id_pet)
);

create table agendamento_servico (
n_agendamento int NOT NULL,
id_servico int NOT NULL,
primary key(n_agendamento, id_servico),
CONSTRAINT fk_n_agendamento FOREIGN KEY (n_agendamento) REFERENCES agendamento(n_agendamento),
CONSTRAINT fk3_id_servico FOREIGN KEY (id_servico) REFERENCES servico(id_servico)
);