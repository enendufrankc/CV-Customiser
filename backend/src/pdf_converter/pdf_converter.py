from docling.document_converter import DocumentConverter


def pdf_converter(source):
    converter = DocumentConverter()
    result = converter.convert(source)
    return result.document.export_to_markdown()