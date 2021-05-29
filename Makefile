install:
	python3 -m venv .venv
	.venv/bin/pip3 install --upgrade wheel pip
	.venv/bin/pip3 install -r requirements.txt 
req:
	.venv/bin/pip3 freeze > requirements.txt
