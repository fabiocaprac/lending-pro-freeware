# Prazo Certo

App desktop **offline** para **gestão de crediário, empréstimos e cobrança** no Brasil.

Registre clientes (com CPF), contratos, juros, carnê, fiador, garantia e pagamentos em **dinheiro, PIX, transferência, boleto ou cartão**. Os dados ficam no seu computador — sem nuvem obrigatória e sem telemetria.

## Padrões Brasil

- Interface em **português (Brasil)**
- Moeda **R$ (BRL)**
- Datas **dd/mm/aaaa**
- Telefone `(11) 98765-4321`

## Recursos

| Área | O que faz |
| --- | --- |
| **Painel** | Capital ativo, juros recebidos, inadimplência, PAR e vencimentos do dia |
| **Clientes** | Ficha com foto, CPF, renda, documentos e histórico |
| **Empréstimos** | Juros prefixados ou saldo decrescente, taxas, CET, carnê |
| **Pagamentos** | Parciais, estorno com auditoria, PIX e demais formas BR |
| **Cobrança** | Agenda, alertas de atraso e SMS com modelos em português |
| **Documentos** | Contrato, recibo e carnê em PDF; Excel da carteira |
| **Segurança** | Login local opcional, fiador, garantia e backup no aparelho |

Não há recursos para ocultar operação, cobrança violenta ou evasão. É um **livro-caixa de crediário**.

## Rodar do código

Python 3.11+, Node.js 22+ e as dependências nativas do pywebview.

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt -r requirements-dev.txt
npm ci
npm run build:css
python main.py
```

Checagens:

```bash
npm run check
npm test
```

Os dados locais ficam em `~/.local/share/PrazoCerto` (Linux), `~/Library/Application Support/PrazoCerto` (macOS) ou `%APPDATA%\PrazoCerto` (Windows).

## Licença

MIT. Copyright © 2026.
