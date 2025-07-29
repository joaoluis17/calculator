# 🏥 Calculadora de IMC

Uma aplicação web simples e intuitiva para calcular o Índice de Massa Corporal (IMC) desenvolvida em Python com Flask.

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![Flask](https://img.shields.io/badge/Flask-2.0%2B-green)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 📋 Sobre o Projeto

Esta calculadora de IMC oferece uma interface web limpa e responsiva para calcular e classificar o Índice de Massa Corporal segundo os padrões da Organização Mundial da Saúde (OMS).

### ✨ Funcionalidades

- 🧮 Cálculo preciso do IMC
- 📊 Classificação automática segundo padrões da OMS
- 🎨 Interface responsiva e intuitiva
- ⚡ Validação de dados em tempo real
- 🔄 Prevenção de reenvio de formulário
- 🌈 Feedback visual com cores diferenciadas por categoria

### 📈 Classificações do IMC

| IMC | Classificação |
|-----|---------------|
| Abaixo de 18,5 | Abaixo do peso |
| 18,5 - 24,9 | Peso ideal |
| 25,0 - 29,9 | Sobrepeso |
| 30,0 - 39,9 | Obesidade |
| 40,0 ou mais | Obesidade mórbida |

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### Instalação

1. **Clone o repositório**
   ```bash
   git clone [https://github.com/joaoluis17/calculator
   cd calculator
   ```

2. **Crie um ambiente virtual (recomendado)**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Instale as dependências**
   ```bash
   pip install flask
   ```

4. **Execute a aplicação**
   ```bash
   python app.py
   ```

5. **Acesse no navegador**
   ```
   http://127.0.0.1:5000
   ```

## 📁 Estrutura do Projeto

```
calculadora-imc/
│
├── app.py                 # Aplicação Flask principal
├── templates/
│   └── index.html        # Template HTML
├── requirements.txt      # Dependências do projeto
├── README.md            # Documentação
└── .gitignore          # Arquivos ignorados pelo Git
```

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python 3.7+
- **Framework Web**: Flask 2.0+
- **Frontend**: HTML5, CSS3
- **Template Engine**: Jinja2

## 💻 Uso da Aplicação

1. Acesse a aplicação no navegador
2. Digite seu **peso** em quilogramas (kg)
3. Digite sua **altura** em metros (m)
4. Clique em **"Calcular IMC"**
5. Visualize o resultado com a classificação correspondente

### Exemplo de Uso

```
Peso: 70.5 kg
Altura: 1.75 m
Resultado: IMC = 23.0 (Peso ideal)
```

## 🤝 Como Contribuir

Contribuições são sempre bem-vindas! Para contribuir:

1. **Fork** o projeto
2. Crie uma **branch** para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. Abra um **Pull Request**

### 💡 Ideias para Contribuição

- [ ] Adicionar histórico de cálculos
- [ ] Implementar gráfico de evolução do IMC
- [ ] Adicionar calculadora de IMC para crianças
- [ ] Implementar modo escuro
- [ ] Adicionar mais idiomas
- [ ] Criar API REST
- [ ] Adicionar testes unitários

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## 📞 Contato

João Luis Prado - [@JohnPrado1728](https://x.com/JohnPrado1728) - jluispprado@hotmail.com - [Portfólio](https://joao-luis-prado.netlify.app/)

Link do Projeto: [https://github.com/joaoluis17/calculator](https://github.com/joaoluis17/calculator)

## 🙏 Agradecimentos

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Organização Mundial da Saúde (OMS)](https://www.who.int/)
- [Python.org](https://www.python.org/)

---

⭐ **Se este projeto te ajudou, não esqueça de dar uma estrela!** ⭐
