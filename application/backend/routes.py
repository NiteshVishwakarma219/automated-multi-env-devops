from flask import jsonify
from datetime import datetime
from config import Config
from version import VERSION

def register_routes(app):

    @app.route("/")
    def home():
        return f"""
        <h1>CloudOps Dashboard</h1>
        <h2>Environment : {Config.ENVIRONMENT}</h2>
        <h3>Version : {VERSION}</h3>
        <h3>Status : Healthy</h3>
        """

    @app.route("/health")
    def health():
        return jsonify({
            "status": "healthy",
            "environment": Config.ENVIRONMENT,
            "version": VERSION,
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })