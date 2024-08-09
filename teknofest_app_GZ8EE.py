import uvicorn



from fastapi import FastAPI
from pydantic import BaseModel, Field
from mymodel import TddiMlpModel

#from transformers import AutoTokenizer, AutoModel


app = FastAPI()
#tokenizer = AutoTokenizer.from_pretrained("dbmdz/bert-base-turkish-128k-uncased")
#bert = AutoModel.from_pretrained("dbmdz/bert-base-turkish-128k-uncased")

class Item(BaseModel):
    text: str = Field(..., example="""Fiber 100mb SuperOnline kullanıcısıyım yaklaşık 2 haftadır @Twitch @Kick_Turkey gibi canlı yayın platformlarında 360p yayın izlerken donmalar yaşıyoruz.  Başka hiç bir operatörler bu sorunu yaşamazken ben parasını verip alamadığım hizmeti neden ödeyeyim ? @Turkcell """)
'''
def filter(text):
  final_text = ''
  for word in text.split():
    if word.startswith('@'):
      continue
    elif word[:-3] in ['com', 'org']:
      continue
    elif word.startswith('pic') or word.	startswith('http') or word.startswith('www'):
      continue
    else:
      final_text += word + ' '
  return final_text

def feature_extraction(text):
  tokens = tokenizer(text, padding='max_length', truncation=True, max_length=512, return_tensors='pt')
  input_ids = tokens['input_ids']
  attention_mask = tokens['attention_mask']
  x = tokenizer.encode(filter(text))
  with torch.no_grad():
    outputs = bert(input_ids, attention_mask=attention_mask)
  x = outputs.last_hidden_state
  return list(x[0][0].cpu().numpy())
'''
@app.post("/predict/", response_model=dict)
async def predict(item: Item):
    # Tahmin yap
	#predictions =TddiMlpModel.predict(feature_extraction(item.text))
	#result={"entity_list": ["turkcell","bilişim vadisi"] , "result":[ { "entity":"bilişim vadisi" , "sentiment" : "olumlu"},{ "entity":"turkcell" , "sentiment" : "nötr"}]}
	#predictions =TddiMlpModel.predict(x)
	result = {
  "entity_list": [
    "Turknet",
    "Turktelekom",
    "Vodafone",
    "Turkcell"
  ],
  "results": [
    {
      "entity": "Turknet",
      "sentiment": "olumsuz"
    },
    {
      "entity": "Turktelekom",
      "sentiment": "nötr"
    },
    {
      "entity": "Vodafone",
      "sentiment": "nötr"
    },
    {
      "entity": "Turkcell",
      "sentiment": "olumlu"
    }
  ]
}

    
	#return predictions
	return result


if __name__=="__main__":
    uvicorn.run(app,host="0.0.0.0",port=6789)
    