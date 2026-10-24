
# 📦 Sistema de Gestão de Entregas

🚚 **Transformando dados de entregas em informações operacionais com Python.**

Projeto pessoal desenvolvido para aplicar programação a problemas de **Engenharia de Transportes e Logística**, com cadastro de entregas, cálculo de indicadores e geração de relatórios operacionais.

<p>
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/Status-Em%20desenvolvimento-orange" alt="Em desenvolvimento"/>
  <img src="https://img.shields.io/badge/Área-Logística-2ea44f" alt="Logística"/>
</p>

---

## 🚀 Funcionalidades

### 📋 Cadastro de entregas
- Registro da quantidade de entregas.
- Cadastro de cliente e cidade.
- Registro de distância percorrida, peso e valor da entrega.
- Validação de entradas numéricas e de valores positivos.

### 📊 Resumo operacional
- 💰 Valor total das entregas.
- 🛣️ Distância total registrada.
- ⚖️ Peso total transportado.

### 📈 Indicadores médios
- Valor médio por entrega.
- Distância média por entrega.
- Peso médio por entrega.

### 🏆 Maiores indicadores
- Maior distância registrada.
- Maior valor de entrega.
- Maior peso registrado.

### 🧾 Relatórios individuais
Para cada entrega, o sistema apresenta:
- Cliente e cidade.
- Distância, peso e valor.
- Valor por quilômetro.
- Valor por quilograma.

### 🇧🇷 Formatação brasileira
Os valores numéricos são apresentados com vírgula decimal e ponto para separar milhares.

---

## 🖥️ Exemplo de utilização

O sistema solicita os dados de cada entrega e, ao final, apresenta um resumo operacional e os relatórios individuais.

Exemplo ilustrativo de indicadores para duas entregas:

| Indicador | Resultado |
|---|---:|
| 📦 Entregas registradas | 2 |
| 💰 Valor total | R$ 800,00 |
| 🛣️ Distância total | 150,00 km |
| ⚖️ Peso total | 300,00 kg |
| 💵 Valor médio por entrega | R$ 400,00 |
| 📏 Distância média | 75,00 km |

> ℹ️ Os números acima são apenas ilustrativos. Os resultados reais dependem dos dados informados durante a execução.

---

## 🛠️ Tecnologias e conceitos

| Tecnologia / conceito | Aplicação |
|---|---|
| 🐍 Python | Lógica e desenvolvimento do sistema |
| 📚 Listas | Armazenamento dos dados das entregas |
| 🔁 Laços de repetição | Cadastro e validação das entradas |
| 🛡️ Tratamento de exceções | Tratamento de entradas numéricas inválidas |
| 🧮 Funções | Formatação de números |
| 📊 Operações com dados | Totais, médias e identificação de máximos |
| 🔧 Git e GitHub | Controle de versão e hospedagem do projeto |

---

## ▶️ Como executar

### Pré-requisito
Ter o [Python instalado](https://www.python.org/downloads/).

### Passos

1. Clone o repositório:

   ```bash
   git clone https://github.com/mateusliz2007-cpu/controle-entregas-python.git
   ```

2. Entre na pasta do projeto:

   ```bash
   cd controle-entregas-python
   ```

3. Execute o programa:

   ```bash
   python main.py
   ```

   💡 No Windows, também é possível utilizar `py main.py`.

---

## 🎯 Objetivos de aprendizado

Este projeto faz parte do meu desenvolvimento em programação, buscando conectar conhecimentos técnicos a aplicações práticas na logística.

- 💻 Desenvolver raciocínio lógico com Python.
- 📊 Trabalhar com dados e indicadores operacionais.
- 🚛 Explorar problemas relacionados a transporte e entregas.
- 📈 Evoluir para projetos de análise de dados e otimização logística.

## 🗺️ Próximos passos

- [ ] 🧹 Melhorar a organização e a estrutura do código.
- [ ] 💾 Explorar formas de salvar os dados das entregas.
- [ ] 📊 Ampliar os indicadores de desempenho logístico.
- [ ] 📉 Criar análises comparativas entre entregas.
- [ ] 🧪 Desenvolver testes para validar os cálculos.

---

## 👨‍💻 Sobre

Desenvolvido por **Mateus**, estudante de Engenharia de Transportes e Logística, como projeto de aprendizado em Python.

🔗 **Repositório:** [controle-entregas-python](https://github.com/mateusliz2007-cpu/controle-entregas-python)

💡 **Interesses:** logística, transporte, análise de dados, programação e otimização de operações.
