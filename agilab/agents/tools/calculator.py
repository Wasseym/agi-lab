def calculator(expr: str) -> str:
    try:
        return str(eval(expr, {'__builtins__':{}}))
    except Exception as e:
        return f"error: {e}"
