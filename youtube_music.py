import pyautogui as pa
import time
from dotenv import load_dotenv
import os

load_dotenv()

search_site = os.getenv('SEARCH_SITE')
search_query = os.getenv('SEARCH_QUERY')

if search_query is None:
    raise ValueError("A variável de ambiente 'SEARCH_QUERY' não foi encontrada. Verifique o arquivo .env.")

pa.PAUSE = 1

pa.press('win')
pa.write('edge')
pa.press('enter')
pa.write(search_site)
pa.sleep(0.5)
pa.press('space')
pa.press('enter')
time.sleep(2)  # Aguarde o YouTube carregar
pa.click(x=787, y=121)
pa.write(search_query)
pa.press('enter')
pa.sleep(2)
pa.click(x=659, y=755)
