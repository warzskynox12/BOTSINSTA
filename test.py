import requests
import json
import os

# Supprimer le fichier classes.json s'il existe
if os.path.exists("classes.json"):
    os.remove("classes.json")

# URL de destination
url = "https://ent.iledefrance.fr/communication/visible"

# En-têtes HTTP
headers = {
    "Cookie": "webviewignored=true:n33DiVTcIrbMCxJAnib1VOoDer0=; __cf_bm=6y0KDeKAkW6lvyvHDDggu20KM0Et5gYPFVIGTmyXhY0-1728570211-1.0.1.1-2Ngc0XoaaS7HcZCdH8nX6J6k5.4RKqTdXmcAo5L2carUWulqHpvosI4WFYb2grbPJor6spWaja90IOBkgAKHEQ; csrfstate=c0d1e53e-fe0a-4e06-990f-946d08057cc9:3NINcSco8wMZSvcDD/Eb2KCg24o=; nonce=72bf09b7-0e39-4e57-ad47-00d2cc3e3257:YP9NKZ4BjgoRZTdfHFqhfA63v6M=; oneSessionId=23afffd9-78cc-46fc-8774-441d73481d09:zonLK0/WPS31OxNYcUH+1BQwHJU=; authenticated=true; XSRF-TOKEN=66fa69fa-0e24-4499-adaf-643d80da3663",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "X-Xsrf-Token": "66fa69fa-0e24-4499-adaf-643d80da3663",
    "Accept-Language": "fr-FR,fr;q=0.9",
    "Sec-Ch-Ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Content-Type": "application/json;charset=UTF-8",
    "Origin": "https://ent.iledefrance.fr",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://ent.iledefrance.fr/userbook/annuaire",
    "Accept-Encoding": "gzip, deflate, br",
    "Priority": "u=1, i"
}

# Corps de la requête (données JSON)
data = {
    "search": "",
    "types": ["User"],
    "structures": ["f643946c-2392-4c04-8c82-0ed2f4925c1e"],
    "classes": [
        "51ae9bbe-765a-4c38-9270-99a427720739", "8fdca176-469a-4d95-80c3-c7047aae6e80",
        "e7d632b0-40c2-4be1-85a1-2fcc9a9c6796", "12e2e4e7-9365-4a58-a1c3-0f902f0f8c16",
        "51821cc1-0d2b-49dc-958b-b365122b0f6f", "3a1bb2f7-5d33-4f0e-9700-5df719c822d3",
        "4020d69b-acbd-4b0b-9743-82d58825a63b", "b7782835-bbdf-48b1-bf05-55d4c4e81f11",
        "cefa31f6-0e2b-46f1-b2d1-83055c52f394", "3b03cc96-ed6d-4e60-aeaa-3b8f00905189",
        "cc94f9d7-5682-427c-b924-9eb5a826df49", "3172da50-5d2d-476f-b746-0bdb9d242111",
        "0acf3895-528d-4a92-aa45-9bd1c5762e05", "7ad5ed72-9e11-4f17-b632-ec31e47b23cc",
        "65f54b07-26fd-4eeb-bab4-2e4be4e753af", "5257eae1-5f9e-46be-879c-53bf0f9d3759",
        "102f6112-d66c-4de2-8d61-91ea1aa7ee1b", "fa3761d0-095c-47b7-921a-4b4e33470e84",
        "7f7e7eb3-623f-4774-b2b3-502777df5609", "0e59c839-5d52-480f-8a67-a2a9b5f527ae",
        "7b585195-31cf-440f-a2f6-bf1f55833381", "2022da11-1b43-41c9-a0bf-65541eca079a",
        "9c8cc1e2-2f32-4194-9e33-02731374bc49", "9a9d2d88-13bd-4210-896d-c9d58f03cdf7",
        "5ed6b758-1d22-4a51-8cc1-377e6b7cbd73", "6e6efb61-3435-4ca0-9323-e1017e8f0fdd",
        "316c3772-35c3-4ed3-970d-bb672b86f5b6", "e027f1cb-83f2-4d51-b962-37030407f0da",
        "7c2b3873-6838-4ab6-b2f0-fd8a804d2b93", "f0e71a65-f994-4c31-85c7-f72d89fa16e6",
        "7a91ac63-f583-4b2a-a8e7-e558c920c796", "302b3efb-beb1-45ff-a187-1b90cfe1f977",
        "c61f9b5f-9465-4a8f-a7e0-cd6ba7bbaa71", "6dcb1be3-7aaa-45f3-aab3-d413db85fd8b",
        "84d05735-5093-4a66-b2ab-4bda20c690b5", "be153c59-f202-425e-ae2a-aa3b2fbb7c7a",
        "833da8e3-6cf9-4348-abd7-9d24de571c8c", "d4d6724c-90eb-4500-a45a-cb9525534fee",
        "fe533e09-a63c-499e-b316-af31946de2af"
    ],
    "profiles": ["Student"],
    "functions": [],
    "mood": True
}

response = requests.post(url, headers=headers, json=data)

try:
    response_data = response.json()
except json.JSONDecodeError:
    print("Erreur lors du décodage de la réponse JSON.")
    response_data = {}

if isinstance(response_data, dict) and "users" in response_data:
    response_data = response_data["users"]

# Fonction pour gérer les données valides
def vrais(response_data):
    print("response_data est une liste comme attendu.")
    filtered_data = [{"id": person["id"], "displayname": person["displayName"]} for person in response_data]
    with open("response.json", "w", encoding="utf-8") as f:
        json.dump(filtered_data, f, ensure_ascii=False, indent=4,)

# Fonction pour gérer les données invalides
def faux(response_data):
    print("response_data n'est pas une liste comme attendu.")

if isinstance(response_data, list):
    vrais(response_data)
else:
    faux(response_data)

# Lire le fichier response.json
with open("response.json", "r", encoding="utf-8") as f:
    response_data = json.load(f)

# Vérifier si response_data est une liste
if isinstance(response_data, list):
    for person in response_data:
        person_id = person["id"]
        displayname = person["displayname"]
        url = 'https://ent.iledefrance.fr/userbook/api/person'
        params = {
            'id': person_id,
            "type": "undefined"
        }
        headers = {
            "Cookie": "webviewignored=true:n33DiVTcIrbMCxJAnib1VOoDer0=; __cf_bm=6y0KDeKAkW6lvyvHDDggu20KM0Et5gYPFVIGTmyXhY0-1728570211-1.0.1.1-2Ngc0XoaaS7HcZCdH8nX6J6k5.4RKqTdXmcAo5L2carUWulqHpvosI4WFYb2grbPJor6spWaja90IOBkgAKHEQ; csrfstate=c0d1e53e-fe0a-4e06-990f-946d08057cc9:3NINcSco8wMZSvcDD/Eb2KCg24o=; nonce=72bf09b7-0e39-4e57-ad47-00d2cc3e3257:YP9NKZ4BjgoRZTdfHFqhfA63v6M=; oneSessionId=23afffd9-78cc-46fc-8774-441d73481d09:zonLK0/WPS31OxNYcUH+1BQwHJU=; authenticated=true; XSRF-TOKEN=66fa69fa-0e24-4499-adaf-643d80da3663",
            "Sec-Ch-Ua-Platform": "\"Windows\"",
            "X-Xsrf-Token": "66fa69fa-0e24-4499-adaf-643d80da3663",
            "Accept-Language": "fr-FR,fr;q=0.9",
            "Accept": "application/json, text/plain, */*",
            "Sec-Ch-Ua": "\"Chromium\";v=\"129\", \"Not=A?Brand\";v=\"8\"",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.6668.71 Safari/537.36",
            "Sec-Ch-Ua-Mobile": "?0",
            "Sec-Fetch-Site": "same-origin",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Dest": "empty",
            "Referer": "https://ent.iledefrance.fr/userbook/annuaire",
            "Accept-Encoding": "gzip, deflate, br",
            "Priority": "u=1, i"
        }

        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200: 
            person_data = response.json()
            results = person_data.get("result", [])
            if results:
                person = results[0]
                person_id = person.get("id")
                displayname = person.get("displayName")
                schools = person.get("schools", [])
                if schools:
                    classes = schools[0].get("classes", [])
                    # Ajouter ou mettre à jour la classe pour chaque ID
                    if classes:
                        class_name = classes[0]
                        with open(f"classe/{class_name}.json", "a", encoding="utf-8") as f:
                            json.dump({"displayName": displayname,}, f, ensure_ascii=False, indent=4)
                        with open("classes.json", "a", encoding="utf-8") as f:
                            json.dump({"displayName": displayname, "classes": class_name}, f, ensure_ascii=False, indent=4)
                        print(f"{displayname}; {class_name}")
        else:
            print(f"Erreur lors de la requête : {response.status_code}")
    print("Fin du script.")
