# Youngstorage

## How to RUN

> fitst clone the project
```
git clone https://github.com/PABYoungStorage/youngstorage-latest.git
cd youngstorage-latest
```

> create a virtual env using python venv

### mac/linux
```
python3 -m venv .venv
```

### windows
```
python -m venv .venv
```

> Then activate the venv and install the required packages

### mac/linux
```
source .venv/bin/activate
pip install -r requirements.txt
```

### mac/linux
```
.venv/bin/activate
pip install -r requirements.txt
```

> run the project
```
flask --app flaskr run --debug --host=0.0.0.0
```
- --debug for to enable the debug option
- --host for to service the webpage to the public like 0.0.0.0