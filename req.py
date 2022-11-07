import requests
Base="http://127.0.0.1:5000/"
response=requests.put(Base+"/pdf",{"path":"/Users/bipin/Desktop/hh/PHY2005 - Module-5 Complete PPT_compressed.pdf","angle":180,"page_number":10})
print(response.json())
