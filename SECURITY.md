# Security

Do not commit credentials, tokens, `.env` files, private datasets, local logs or generated archives.

Before publication or release:

```bash
python -m pytest -q
python -m ruff check src tests
python -m mypy src
```

If a report mentions secrets, redact values and keep only path/category evidence.

