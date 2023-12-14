# State of the Union
State of the Union scraper and archive, based on the [UCSB American Presidency Project](https://www.presidency.ucsb.edu/)


This project creates machine-readable JSON files of all State of the Union addresses.

If you just want the data, clone this project and see the data/sotu directory.

Sample JSON:

```json
{
    "title": "Address Before a Joint Session of the Congress on the State of the Union", 
    "content": " <p>Thank you all. Madam Speaker, Vice President ...", 
    "published": "2008-01-28",
    "president": "George W. Bush",
    "url": "https://www.presidency.ucsb.edu/documents/address-before-joint-session-the-congress-the-state-the-union-18",
    "citation": "George W. Bush, Address Before a Joint Session of the Congress on the State of the Union Online by Gerhard Peters and John T. Woolley, The American Presidency Project https://www.presidency.ucsb.edu/node/277182", 
    "footnote": "NOTE: The President spoke at 9:09 p.m. in the House Chamber of the U.S. Capitol. In his remarks, he referred to President Hamid Karzai of Afghanistan; Usama bin Laden, leader of the Al Qaida terrorist organization; Gen. David H. Petraeus, USA, commanding general, Multi-National Force\u2014Iraq; President Mahmoud Abbas of the Palestinian Authority; and former Sen. Robert J. Dole and former Secretary of Health and Human Services Donna E. Shalala, Cochairs, President's Commission on Care for America's Returning Wounded Warriors. The Office of the Press Secretary also released a Spanish language transcript of this address.", 
    "classification": "state-of-the-union"
}
```

To run the scraper:
```python
poetry shell
poetry install
python3 scraper.py
```