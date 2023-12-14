from dataclasses import dataclass, field
from dataclasses_json import dataclass_json, config
from datetime import datetime
import dateutil.parser
import json
import lxml.html
import lxml.etree
import os
import requests


@dataclass_json
@dataclass
class Doc:
    title: str
    content: str
    published: str
    president: str
    url: str
    citation: str
    footnote: str
    classification: str = "state-of-the-union"

    def __repr__(self):
        return f"{self.published} {self.title}"

    def save(self) -> bool:
        path = f"data/sotu/"
        filename = f"{path}/{self.published}.json"

        if not os.path.exists(path):
            os.makedirs(path)

        with open(filename, "w") as f:
            f.write(self.to_json())
            return True
        return False


def scrape_listing_page(url):
    page = requests.get(url).content
    page = lxml.html.fromstring(page)
    page.make_links_absolute(url)

    for row in page.cssselect("div.view-content div.row"):
        date = row.cssselect("h4")[0].text_content().strip()
        date = dateutil.parser.parse(date).strftime('%Y-%m-%d')
        link = row.cssselect("div.field-title p a")[0]
        title = link.text_content().strip()
        pres = row.cssselect("div.col-sm-4 p a")[0].text_content().strip()
        sotu_url = link.xpath("@href")[0]
        print(title, date, sotu_url)

        text, footnote, citation = scrape_page(sotu_url)

        sotu = Doc(title,
                   text,
                   date,
                   pres,
                   sotu_url,
                   citation,
                   footnote,
        )

        print(sotu)
        sotu.save()



def scrape_page(url):
    page = requests.get(url).content
    page = lxml.html.fromstring(page)

    content = page.cssselect("div.field-docs-content")[0]
    text = lxml.etree.tostring(content,encoding='unicode')

    footnote = page.cssselect("div.field-docs-footnote")[0].text_content().strip()
    citation = page.cssselect("div.field-prez-document-citation")[0].text_content().strip()

    return (text, footnote, citation)

url ="https://www.presidency.ucsb.edu/documents/app-categories/spoken-addresses-and-remarks/presidential/state-the-union-addresses?items_per_page=60"
scrape_listing_page(url)