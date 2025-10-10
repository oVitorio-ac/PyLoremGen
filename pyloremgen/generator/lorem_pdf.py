from typing import Optional

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import PageBreak, Paragraph

from .lorem_text import LoremIpsum
from .pdf_utils.cover_page_template import CoverPageBuilder
from .pdf_utils.pdf_page_settings import PagesConfigPDF


class PDFGenerator:
    """
    PDFGenerator class for creating PDF documents with Lorem Ipsum content.

    This class provides functionality to generate
    PDF files filled with Lorem Ipsum text,
    with options for customizing page settings and including cover pages.

    Attributes:
        pages_config (PagesConfigPDF): Configuration for PDF page settings.
        lorem (LoremIpsum): Instance of LoremIpsum for generating text content.

    Methods:
        generate_pdf(filename: str, num_pages: int = 1,
        cover_page_count: bool = True) -> None:
            Generates a PDF document with the specified number of pages.
    """

    def __init__(self, pages_config: Optional[PagesConfigPDF] = None) -> None:
        self.pages_config = pages_config or PagesConfigPDF()
        self.lorem = LoremIpsum()

    def generate_pdf(
        self, filename: str, num_pages: int = 1, cover_page_count: bool = True
    ) -> None:
        """
        Generate a PDF document with Lorem Ipsum content.

        Args:
            filename (str): The name of the output PDF file.
            num_pages (int, optional): The number of pages to generate. Defaults to 1.
            cover_page_count (bool, optional):
                Whether to include a cover page. Defaults to True.
        """
        self.num_pages = num_pages
        doc = self.pages_config.create_document(filename)
        content = []

        # Add cover page
        cover_builder = CoverPageBuilder()
        cover_content = cover_builder.build_cover_page()
        content.extend(cover_content)

        # Determine starting page based on cover page count
        start_page = 1 if cover_page_count else 0

        # Add page breaks and additional pages if necessary
        for _ in range(start_page, self.num_pages + start_page):
            content.append(PageBreak())

            # Generate lorem ipsum paragraphs for each page
            max_characters_per_page = self.pages_config.get_max_characters_per_page()
            remaining_characters = max_characters_per_page

            while remaining_characters > 0:
                lorem_paragraphs = self.lorem.paragraphs(paragraphs_numbers=1)
                paragraph = " ".join(lorem_paragraphs)
                paragraph_length = len(paragraph)
                if paragraph_length > remaining_characters:
                    # Truncate the paragraph to fit the remaining characters on the page
                    paragraph = paragraph[:remaining_characters]
                content.append(Paragraph(paragraph, getSampleStyleSheet()["Normal"]))
                remaining_characters -= paragraph_length

        doc.build(content)
