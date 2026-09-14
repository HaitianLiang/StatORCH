class OptionalAdapterUnavailable(RuntimeError):
    pass

def require_external_adapter(name: str):
    raise OptionalAdapterUnavailable(
        f"{name} requires a model/domain-specific adapter and is intentionally not silently emulated."
    )
