"""Currency configuration shared by exports and printable documents."""

from __future__ import annotations

from datetime import datetime


SUPPORTED_CURRENCIES = {
    "PHP", "EUR", "USD", "CHF", "GBP", "CAD", "AUD", "NZD", "JPY",
    "SGD", "HKD", "AED", "SAR", "INR", "THB", "MYR", "IDR", "VND",
    "KRW", "ZAR", "MXN", "BRL",
}
ZERO_DECIMAL_CURRENCIES = {"JPY", "KRW", "VND", "IDR"}
DEFAULT_CURRENCY = "BRL"
DEFAULT_LANGUAGE = "pt-BR"
DEFAULT_LOCALE = "pt-BR"

PAYMENT_METHOD_LABELS = {
    "cash": "Dinheiro",
    "pix": "PIX",
    "bank_transfer": "Transferência",
    "boleto": "Boleto",
    "card": "Cartão",
    "check": "Cheque",
    "gcash": "PIX",
}

VALID_PAYMENT_METHODS = {"cash", "pix", "bank_transfer", "boleto", "card", "check"}
PAYMENT_METHOD_ALIASES = {
    "bank": "bank_transfer",
    "bank transfer": "bank_transfer",
    "bank-transfer": "bank_transfer",
    "transferencia": "bank_transfer",
    "transferência": "bank_transfer",
    "gcash": "pix",
    "dinheiro": "cash",
    "cartao": "card",
    "cartão": "card",
    "cheque": "check",
}


def normalize_currency(code) -> str:
    normalized = str(code or DEFAULT_CURRENCY).strip().upper()
    return normalized if normalized in SUPPORTED_CURRENCIES else DEFAULT_CURRENCY


def currency_from_connection(connection) -> str:
    row = connection.execute(
        "SELECT value FROM settings WHERE key = 'currency'"
    ).fetchone()
    value = row[0] if row else DEFAULT_CURRENCY
    return normalize_currency(value)


def format_money(amount, currency_code: str) -> str:
    code = normalize_currency(currency_code)
    decimals = 0 if code in ZERO_DECIMAL_CURRENCIES else 2
    value = float(amount or 0)
    formatted = f"{value:,.{decimals}f}"
    if code == "BRL":
        formatted = formatted.replace(",", "X").replace(".", ",").replace("X", ".")
        return f"R$ {formatted}"
    return f"{code} {formatted}"


def format_date_br(value) -> str:
    """Format a date-like value as dd/mm/aaaa."""
    if value in (None, ""):
        return "—"
    text = str(value).strip()
    for fmt in ("%Y-%m-%d", "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M:%S.%f"):
        try:
            return datetime.strptime(text[:26], fmt).strftime("%d/%m/%Y")
        except ValueError:
            continue
    if len(text) >= 10 and text[4] == "-" and text[7] == "-":
        return f"{text[8:10]}/{text[5:7]}/{text[0:4]}"
    return text


def format_payment_method(method) -> str:
    key = str(method or "cash").strip().lower()
    return PAYMENT_METHOD_LABELS.get(key, key.replace("_", " ").title())


def normalize_cpf(value) -> str:
    digits = "".join(ch for ch in str(value or "") if ch.isdigit())
    return digits[:11]


def format_cpf(value) -> str:
    digits = normalize_cpf(value)
    if len(digits) == 11:
        return f"{digits[:3]}.{digits[3:6]}.{digits[6:9]}-{digits[9:]}"
    return str(value or "").strip()
