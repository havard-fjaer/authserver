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
	docker run -d --name authserver havardfjaer/authserver:latest -p 127.0.0.1:8081:8081
docker-stop:
	docker container stop authserver
	docker container rm authserver
docker-push:
	docker push havardfjaer/authserver:latest
kube-redeploy-pod:
	kubectl rollout restart deployment authserver

