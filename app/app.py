import os
import socket
import logging
import datetime
from flask import Flask, jsonify

# Production logging - feeds into CloudWatch via awslogs driver
logging.basicConfig(
	level=logging.INFO,
	format='%(asctime)s [%(levelname)s] %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)

@app.route('/')
def home():
    logger.info('Home endpoint hit')
    return (
        '<h1>Project 3 - Version2 - Auto Deployed via CI/CD</h1>'
        '<p>Built by Shashank Ballaya</p>'
        f'<p>Container: {socket.gethostname()}</p>'
	)

@app.route('/health')
def health(): 
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.datetime.now(datetime.timezone.utc).isoformat()
	})

@app.route('/info')
def info():
    return jsonify({
        'app': 'Project 3',
        'Platform': 'AWS ECS Fargate',
        'region': os.environ.get('AWS_REGION', 'ap-south-1'),
        'container_id': socket.gethostname()
	})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)