import random
import smtplib
import pandas

my_email = "dheeraj.shukla8790spain@gmail.com"
my_password = "xyna otqs mojz lrzp"

with open(file="quotes.txt") as quote:
    quote_list = pandas.Series(quote)
    my_quote = random.choice(quote_list)

data = pandas.read_csv("daily_quotes_name.csv")
quote_dict = {data_row["name"]: data_row["email"] for (index, data_row) in data.iterrows()}

for key in quote_dict:
    name = key
    email = quote_dict[key]
    with open("letter_templates/quotes.txt") as messageBody:
        content = messageBody.read()
        content = content.replace("[NAME]", name)
        content = content.replace("[QUOTES]", my_quote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Today's Quote\n\n{content}"
        )
