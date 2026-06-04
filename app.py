from flask import Flask
from loan import Loan

app = Flask(__name__)

@app.route("/")
def home():
    loan = Loan(
        principal_amount=1000,
        interest_rate=5,
        term=2,
        month_or_year="M"
    )
    interest = loan.calculate_loan_interest()
    total = loan.calculate_final_amount()
    return f""" Loan Calculator<br><br>
                Pincipal Amount: {loan.principal_amount} Kr<br>
                Interest Rate: {loan.interest_rate}% <br> 
                Term: {loan.term}{loan.month_or_year} <br>
                --------------------------------- <br>
                Interest: {interest} kr<br>
                Total: {total} kr"""""

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)