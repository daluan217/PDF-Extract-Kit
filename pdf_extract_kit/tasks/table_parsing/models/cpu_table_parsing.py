from pdf_extract_kit.registry.registry import MODEL_REGISTRY
from .paddle_table import PaddleTableParsing  # assumes it exists

@MODEL_REGISTRY.register("table_parsing_cpu")
class TableParsingCPU:
    def __init__(self, config):
        """
        A CPU-compatible table parsing model using PaddleOCR.
        """
        self.model = PaddleTableParsing(config)

    def predict(self, images, result_path, output_format=None, **kwargs):
        return self.model.predict(images, result_path, output_format, **kwargs)
