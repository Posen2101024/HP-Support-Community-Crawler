# HP Support Community

HP support community discussions on https://h30434.www3.hp.com .

## Initialize

- Download [Chromedriver](https://chromedriver.chromium.org/downloads)

	***run*** `mv chromedriver HP-Support-Community-Crawler/chromedriver`

- Download Model

    ***run*** `sh download.sh`

## Update

- Update

    ***run*** `sh update.sh`
    
- Update **Notebooks**

    ***run*** `sh update.sh Notebooks`
    
- Current status

    ***run*** `sh status.sh`

## Directory Layout

```
HP/
│
├── crawler/                 # Crawler Package
│   ├── __init__.py
│   ├── multiple.py
│   ├── parser.py
│   ├── service.py
│   ├── util.py
│   └── work.py
│
├── model/                   # Dataset
│   ├── Desktops/
│   ├── Gaming/
│   ├── Notebooks/           # Notebooks Dataset
│   │   ├── url/             # Topics Url
│   │   ├── html/            # Topics Html
│   │   ├── content/         # Topics Content
│   │   └── forum.csv        # Forums Url
│   ├── Printers/
│   ├── Software/
│   └── Tablets/
│
├── requirements.txt
│
├── main.py
│
├── download.sh
│
├── update.sh
│
├── status.sh
│
└── README.md
```
