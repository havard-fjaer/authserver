init:
	python3 -m venv .env
	pip3 install -r requirements.txt
	source .env/bin/activate
	pip3 install -U pip
	pip3 install pyjwt[crypto]
run:
	python3 server.py
docker-build: 
	docker build -t havardfjaer/authserver:latest .
docker-run: 
	docker run -it havardfjaer/authserver:latest -p 8080:8080
docker-push:
	docker push havardfjaer/authserver:latest

