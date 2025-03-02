from selenium.webdriver import Remote, ChromeOptions
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
from dotenv import load_dotenv
import os

load_dotenv()


def extract_text_from_url(url):
    # Set up headless Chrome options
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    
    # Initialize the WebDriver (ensure chromedriver is installed and in your PATH)
    driver = webdriver.Chrome(options=options)
    
    try:
        # Load the webpage
        driver.get(url)
        html = driver.page_source
    finally:
        driver.quit()
    
    # Parse the HTML using Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")
    
    # Remove unwanted script and style elements
    for element in soup(["script", "style"]):
        element.decompose()
    
    # Extract text and clean up whitespace
    text = soup.get_text(separator=" ")
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    clean_text = ' '.join(chunk for chunk in chunks if chunk)
    
    return clean_text

def scrape_website(website):
    print("Connecting to Scraping Browser...")
    sbr_connection = ChromiumRemoteConnection(SBR_WEBDRIVER, "goog", "chrome")
    with Remote(sbr_connection, options=ChromeOptions()) as driver:
        driver.get(website)
        print("Waiting captcha to solve...")
        solve_res = driver.execute(
            "executeCdpCommand",
            {
                "cmd": "Captcha.waitForSolve",
                "params": {"detectTimeout": 10000},
            },
        )
        print("Captcha solve status:", solve_res["value"]["status"])
        print("Navigated! Scraping page content...")
        html = driver.page_source
        return html
    

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    return cleaned_content


def split_dom_content(dom_content, max_length=6000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]

