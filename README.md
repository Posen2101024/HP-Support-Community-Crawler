# HP Crawler

## Initialize

- Requirements
    ```
    pip3 install -r requirements.txt
    ```

- Download [Chromedriver](https://chromedriver.chromium.org/downloads)
    - [Chrome version 80](https://chromedriver.storage.googleapis.com/index.html?path=80.0.3987.106/)
    - [Chrome version 78](https://chromedriver.storage.googleapis.com/index.html?path=78.0.3904.105/)

## Update

- Update
    ```
    sh update.sh
    ```
    
- Update **Notebooks**
    ```
    sh update.sh Notebooks
    ```
    
- Watch update status
    ```
    sh status.sh
    ```

## Directory Layout
```
HP/
│
├── crawler/                 # Crawler Package
│   ├── __init__.py
│   ├── chromedriver         # Your Chromedriver
│   ├── multiple.py
│   ├── parser.py
│   ├── service.py
│   ├── util.py
│   └── work.py
│
├── model/                   # Data
│   ├── Desktops/
│   ├── Gaming/
│   ├── Notebooks/           # Notebooks Data
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
├── update.sh                # Update Topics
│
├── status.sh                # Watch Work Status
│
├── requirements.txt
│
└── README.md
```