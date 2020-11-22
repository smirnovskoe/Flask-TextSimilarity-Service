# Flask REST API for ML model
- Tested on Ubuntu 18.04.5 LTS
- Docker version 19.03.12, build 48a66213fe
- Python 3.6
### Text Similarity Score
- main libs: torch  (776.7 MB =( ), sentence_transformers 
### Endpoints
Use POST request to send data to the service
- http://0.0.0.0:9000/api/ml
- Data format (JSON):
{
    "text1": "***your first text***",
    "text2": "***your second text***"
}
P.S. simple example in test.py 
### Run with Docker
1. sudo docker build -t flask-txtsim-service .
2. sudo docker run 
