import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuration for authentication in Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Here I will use the JSON that I created with the key creation and API activation in Google Sheets
creds = ServiceAccountCredentials.from_json_keyfile_name("planilhaNotas/planilhanotas.json", scope)
client = gspread.authorize(creds)


# Open the spreadsheet by ID for example:
# https://docs.google.com/spreadsheets/d/1aBNO50SgbE35h7OgvyH0x7NqepqwdsRSK2PGl9z5fZc/edit#gid=0 is the spreadsheet link
# the ID is between d/ and /edit = 1aBNO50SgbE35h7OgvyH0x7NqepqwdsRSK2PGl9z5fZc
spreadsheet = client.open_by_key("1aBNO50SgbE35h7OgvyH0x7NqepqwdsRSK2PGl9z5fZc")

# Select the first worksheet and assign the worksheet object to worksheet
worksheet = spreadsheet.get_worksheet(0)

# Read the local spreadsheet and assign it to df(dataframe) [I'm skipping 2 lines using skiprow]
df = pd.read_excel("planilhaNotas\Engenharia de Software_Desafio_[João Vitor Coutinho do Nascimento].xlsx", skiprows=2)

# If there are cells with NaN or Null, we will fill them with 0
df = df.fillna(0)  

# Function I created to calculate the average and update the Status and Grade column for Final Approval
# the Return is of the type (Status, Note for Final Approval)

def gradeCalculator(row):
    media = (row['P1'] + row['P2'] + row['P3']) / 3
    misses = row['Faltas']
    total_classes = 60  

    if misses > 0.25 * total_classes:
        return "Reprovado por Falta", 0
    elif media < 50:
        return "Reprovado por Nota", 0
    elif 50 <= media < 70:
        naf = max(0, (100 - media))
        return "Exame Final", int(round(naf))
    else:
        return "Aprovado", 0

# Apply the function to each row of the DataFrame
df[['Situação', 'Nota para Aprovação Final']] = df.apply(gradeCalculator, axis=1, result_type='expand')

# Update the spreadsheet in Google Sheets from cell A4, as I am ignoring the spreadsheet header (the first 3 lines)
update_data = df.values.tolist()
worksheet.update('A4', update_data)
