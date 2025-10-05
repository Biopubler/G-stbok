# Demonstrera filhantering genom en enkel besöksräknare
from flask import Flask, render_template, request

app = Flask(__name__)
FILE_PATH = "counter.txt" # lägg eventuellt till sökväg via undermapp vid behov

@app.route("/") 
def index():
  return render_template("Gäst.html")

@app.route("/submit", methods=['POST', 'GET'])
def submit():
    print('funkar?')
    # här skriver du kod som hanterar det su skickar med formuläret
    return "Under construction..."

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0') # filerna servas via din IP-adress i det lokala nätverket



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

# @app.route("/submit", methods=['POST'])
# def submit():
#     print('funkar?')
#    # här skriver du kod som hanterar det su skickar med formuläret
#     return "Under construction..."

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0') # filerna servas via din IP-adress i det lokala nätverket