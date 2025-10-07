# Demonstrera filhantering genom en enkel besöksräknare
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)
FILE_PATH = "counter.txt" # lägg eventuellt till sökväg via undermapp vid behov

@app.route("/") 
def index():
    inlägg = []
    try:  # ← FRÅN DEN BORTKOMMENTERADE KODEN
        with open("counter.txt", "r", encoding="utf-8") as file:
            inlägg = file.readlines()
    except Exception as e:  # ← FRÅN DEN BORTKOMMENTERADE KODEN
        print(f"Fel vid filhantering: {e}")
    
    return render_template("Gäst.html", inlägg=inlägg)

@app.route("/submit", methods=['POST', 'GET'])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    homepage = request.form.get("homepage")
    tel =  request.form.get("tel")
    comment = request.form.get("comment")

    timestamp = datetime.now().strftime("%d/%m-%Y %H:%M")

    print(f"Namn: {name}")
    print(f"Email: {email}")
    print(f"Homepage: {homepage}")
    print(f"Tel: {tel}")
    print(f"Comment: {comment}")

    with open("counter.txt", "a", encoding="utf-8") as f:
      f.write(f"{name}|{email}|{homepage}|{tel}|{comment}\n")
      f.write("---\n")

    print(f'funkar {name} ?')
    # här skriver du kod som hanterar det su skickar med formuläret
    return (f"Hej...klockan är: {timestamp}| du är väl: {name} | {email} | {homepage}  | {tel} | {comment}?") 


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') # filerna servas via din IP-adress i det lokala nätverket



# Nedan var tydligen ett exempel :( 
# Trodde det skulle vara den viktigaste delen.

# @app.route("/")   RÖR INTE UNDER NÅGRA OMSTÄNDIGHETER! 
                #Url till det = http://10.32.35.175:5000
# def show_nbr_visitors():
#     try: # använd undantagshantering när du har med filer att göra!
#         with open(FILE_PATH, 'r') as file: # läsa från filen
#             number = int(file.read()) # läs och typkonvertera besökarsantalet från fil
#             number = number + 1 # öka med ett
#         with open(FILE_PATH, 'w', encoding='utf-8') as file: # skriva till filen
#             file.write(str(number))
#     except Exception as e:
#         return "Fel vid filhantering:" + str(e)
#     return f"Välkommen till sidan! Denna sida har laddats {str(number)} gånger."


# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0') # filerna servas via din IP-adress i det lokala nätverket