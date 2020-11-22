# Flask REST API for ML model
- Tested on Ubuntu 18.04.5 LTS
- Docker version 19.03.12, build 48a66213fe
- Python 3.6
### Text Similarity Score
- main libs: torch  (776.7 MB =( ), sentence_transformers 
### Endpoints
Use POST request to send data to the service
- Endpoint: http://0.0.0.0:9999/api/ml
- Data format (JSON):
{
    "text1": "***your first text***",
    "text2": "***your second text***"
}
- simple POST request: test.py 
### Run with Docker
1. sudo docker build -t flask-txtsim-image .
2. sudo docker run --rm --name flask-txtsim-service -p 9999:9999 flask-txtsim-image
