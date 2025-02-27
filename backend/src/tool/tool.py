from src.scraper.web_scraper import extract_text_from_url, scrape_website, extract_body_content, clean_body_content, split_dom_content
from src.pdf_converter.pdf_converter import pdf_converter 


def customiser_content(resume_path, job_URL):
    # result = scrape_website(job_URL)
    # body_content = extract_body_content(result)
    # job_description = clean_body_content(body_content)
    job_description = extract_text_from_url(job_URL)
    resume_content = pdf_converter(resume_path)
    return job_description, resume_content