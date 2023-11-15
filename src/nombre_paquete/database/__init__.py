import fitz
import sys
import json


def clean_text(text:str)->str:
  characters_to_replace = {
    "'":"",
    "\n":" "
  }
  for character in characters_to_replace.keys():
    text = text.replace(character, characters_to_replace[character])
  return text

def raw_extract(path:str):
  try:
    doc = fitz.open(path)
    meta = doc.metadata
    text = ''
    for page_num in range(0,doc.page_count):
      page=doc.load_page(page_num)
      text+=page.get_text("text")
    meta['pages'] = doc.page_count

    return clean_text(text), clean_text(json.dumps(meta))
  except Exception as e:
    raise Exception(f"Error raw_extract: {e}")
