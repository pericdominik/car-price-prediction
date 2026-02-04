# Car Price Prediction 🚗📈

Projekt iz kolegija **Računarstvo usluga i analiza podataka (RUAP)**  
Tema: **Predikcija cijene rabljenog automobila korištenjem strojnog učenja**

Autori:  
- Dominik Perić  
- Luka Per  

---

## 📌 Opis projekta

Cilj projekta je izgraditi sustav koji na temelju karakteristika vozila (marka, model, godina proizvodnje, kilometraža, tip goriva, snaga motora itd.) predviđa realnu tržišnu cijenu rabljenog automobila.

Projekt uključuje:

- analizu i obradu podatkovnog skupa  
- treniranje više regresijskih modela  
- evaluaciju pomoću MAE, RMSE i R² metrika  
- implementaciju najboljeg modela u Azure Machine Learning  
- izradu REST API-ja  
- razvoj web aplikacije za korisnički unos podataka  

---

## 📊 Dataset

Korišten je javno dostupni dataset s Kaggle platforme:

Used Car Price Prediction Dataset  
https://www.kaggle.com/datasets/taeefnajib/used-car-price-prediction-dataset

Dataset sadrži informacije o:

- brand  
- model  
- godina proizvodnje  
- kilometraža  
- snaga motora  
- tip goriva  
- vrsta mjenjača  
- cijena (ciljna varijabla)

---

## ⚙ Obrada podataka

- uklanjanje nedostajućih vrijednosti  
- encoding kategoričkih varijabli  
- normalizacija numeričkih značajki  
- podjela na trening i test skup (70/30)  

---

## 🤖 Modeli strojnog učenja

Testirani su sljedeći regresijski modeli:

- Linear Regression  
- Decision Forest Regression  
- Neural Network Regression  

Evaluacija je provedena pomoću:

- MAE (Mean Absolute Error)  
- RMSE (Root Mean Squared Error)  
- R² Score  

Najbolji model odabran je prema kombinaciji navedenih metrika.

---

## ☁ Azure Machine Learning

Najuspješniji model deployan je kao web servis koristeći Azure Machine Learning.

Omogućeno je:

- REST API sučelje  
- testiranje endpointa  
- dohvat predviđene cijene vozila putem HTTP zahtjeva  

---

## 🌐 Web aplikacija

Razvijena je jednostavna web aplikacija koja omogućuje:

- unos podataka o vozilu  
- slanje podataka API-ju  
- prikaz predviđene cijene automobila  

Aplikacija služi kao klijentsko sučelje prema Azure ML modelu.

---

## ▶ Pokretanje projekta lokalno

```bash
git clone https://github.com/pericdominik/car-price-prediction
cd car-price-prediction

Instalacija potrebnih paketa:
pip install -r requirements.txt

Pokretanje aplikacije:
python app.py

📁 Struktura projekta
dataset/ – podatkovni skup
preprocessing/ – obrada podataka
training/ – treniranje modela
api/ – Azure endpoint
webapp/ – klijentska aplikacija

✅ Zaključak
Projekt demonstrira kompletnu implementaciju sustava strojnog učenja – od obrade podataka i treniranja modela do deploya u cloud i izrade web aplikacije.
Rezultati pokazuju da je moguće s dobrom točnošću procijeniti tržišnu vrijednost rabljenih automobila koristeći regresijske modele.

📚 Literatura
Kaggle Used Car Dataset
Microsoft Azure Machine Learning dokumentacija
Scikit-learn dokumentacija
