"""
This is the server and flask goes in this file.
"""

from flask import Flask, jsonify, request
from db_utils import get_all_domains,check_domain,add_domain,remove_domain

app = Flask(__name__)

@app.route("/domains", methods=["GET"])
def get_domains():
    return jsonify (get_all_domains())

@app.route("/domains/check/<domain>", methods=["GET"])
def check_phishing(domain):
    result = check_domain(domain)
    return jsonify({"phishing": bool(result), "domain": domain})

@app.route("/domains/add", methods=["POST"])
def add_phishing_domain():
    try:
        data = request.get_json()
        domain = data.get("domain")
        reported_by = data.get("reported_by")

        if not domain or not reported_by:  #checks if the domain or reported by is missing or empty.
            return jsonify({"error": "missing required fields"}), 400  #returns a json error response

        result = add_domain(domain,reported_by)
        return jsonify ({"message":result})

    except Exception as e:
        print(f"API Error: {e}")
        return jsonify ({"error": str (e)}), 500
@app.route("/domains/remove/<int:domain_id>", methods=["DELETE"])
def delete_phishing_domain(domain_id):
    result = remove_domain(domain_id)
    return jsonify({"message": result})

if __name__ == "__main__":
    app.run(debug=True)


