from pdf_extract_kit.tasks.table_parsing.models.struct_eqtable import TableParsingStructEqTable

from pdf_extract_kit.registry.registry import MODEL_REGISTRY

from .models.cpu_table_parsing import TableParsingCPU


__all__ = [
    "TableParsingStructEqTable",
    "TableParsingCPU",
]
