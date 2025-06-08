import requests

API_URL  = "https://dataset.city.shizuoka.jp/dataset/9d7b970c-3514-4c92-b109-2631ed3b1492/resource/91f69f19-0e48-4f28-be3d-292faf4bb88f/download/221007-public-wireless-lan-2407.json"

a = requests.get(API_URL)
b = a.json()

print(b)
