# HP Support Community

HP support community discussions on https://h30434.www3.hp.com .

## Initialize

- Download [Chromedriver](https://chromedriver.chromium.org/downloads)

    - Chrome version 84

        ***run*** `sh download/chromedriver.sh 84.0.4147.30`

- Download Model

    ***run*** `sh download/model.sh`

## Update

- Update

    ***run*** `sh update.sh`
    
- Update **Notebooks**

    ***run*** `sh update.sh Notebooks`
    
- Update status

    ***run*** `sh status.sh`

## Directory Layout

```
HP/
│
├── crawler/                 # Crawler Package
│   ├── chromedriver/
│   ├── __init__.py
│   ├── multiple.py
│   ├── parser.py
│   ├── service.py
│   ├── util.py
│   └── work.py
│
├── download/
│   ├── chromedriver.sh
│   └── model.sh
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
├── update.py
│
├── update.sh
│
├── status.sh
│
└── README.md
```
