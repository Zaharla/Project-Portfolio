"""This is the client-side to interact with the phishing API.
It provides a command-line interface for users to query and modify the
database."""

import requests
import json

def get_all_domains():
    endpoint = "http://127.0.0.1:5000/domains"
    result = requests.get(endpoint).json()
    return result

def check_if_phishing(domain):
    endpoint = f"http://127.0.0.1:5000/domains/check/{domain}"
    result = requests.get(endpoint).json()
    return result

def add_phishing_domain(domain, reported_by):
    endpoint = "http://127.0.0.1:5000/domains/add"
    data = {"domain": domain, "reported_by": reported_by}
    result = requests.post(
        endpoint,
        headers={'content-type': 'application/json'},
        data=json.dumps(data)
    )
    return result.json()

def remove_phishing_domain(domain_id):
    endpoint = f"http://127.0.0.1:5000/domains/remove/{domain_id}"
    response = requests.delete(endpoint)
    try:
       result = response.json()
    except requests.exceptions.JSONDecodeError:  #This will handle a case where the response is not in JSON format
       result = {"message": response.text} #stores the response text in a dictionary
    return result["message"]

def run():
    print("nWelcome to Phishing Domain Checker")
    print("A: View all phishing domains")
    print("B: Check if a website is phishing")
    print("C: Report a new phishing website")
    print("D: Remove a phishing website entry")

    choice = input("Choose an option (A, B, C, D): ").strip().upper()

    if choice == "A":
        print (get_all_domains())
    elif choice == "B":
        domain = input ("Enter the website to check: ")
        print(check_if_phishing(domain))
    elif choice == "C":
        domain = input("Enter the phishing domain: ")
        reported_by = input ("Enter your/email: ")
        print(add_phishing_domain(domain, reported_by))
    elif choice == "D":
        domain_id = input("Enter the domain ID to remove: ")
        print(remove_phishing_domain(domain_id))
    else:
        print("Invalid option. Please select A, B, C, or D ")

if __name__ =="__main__":
    run()

