
# Modulus Oracle Demo

## How to run

- Generate a private key with `openssl`

```
openssl genrsa -out priv.key 512
```

- Create a Python virtual environment

```
virtualenv -p python3 venv
```

- Activate de virtual environment

```
source venv/bin/activate
```

- Install requirements

```
pip install -r requirements.txt
```

- Run the Flask application

```
python main.py
```

- Run the demo script

```
python modulus-oracle.py
```
