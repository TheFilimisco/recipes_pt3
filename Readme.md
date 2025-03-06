# API Recipes

## 1. Llegir totes les receptes (Read): 

- Endpoint GET que retorni la llista completa de receptes utilitzant el model 
Recipe. 
@app.get("/recipes") 

## 2. Llegir una recepta per id (Read Item): 

- Endpoint GET amb un paràmetre de ruta recipe_id que retorni la recepta 
corresponent. 
- Gestioneu l'error si no es troba. 
@app.get("/recipes/{recipe_id}") 

## 3. Crear una recepta (Create): 

- Endpoint POST que rep dades segons el model RecipeInput. 
- Afegir la recepta a la llista en memòria assignant-li un id únic. 
@app.post("/recipes") 

## 4. Actualitzar una recepta (Update): 

- Endpoint PUT que rep un recipe_id i un body amb les noves dades. 
- Actualitzeu la recepta en la llista si existeix. 
@app.put("/recipes/{recipe_id}") 

## 5. Eliminar una recepta (Delete): 

- Endpoint DELETE que rep un recipe_id i elimina la recepta corresponent. 
- Gestioneu l'error si la recepta no existeix.  @app.delete("/recipes/{recipe_id}") 

# Addicionals

#### 1. Filtrar receptes per cuina (cuisine): 

- Permet als usuaris recuperar receptes d'una cuina específica. 
#### 2. Filtrar receptes per dificultat: 
- Permet als usuaris llistar receptes segons el nivell de dificultat (Fàcil, Mitjà, 
Difícil). 
#### 3. Cercar receptes per ingredient: 
- Proporciona un endpoint per cercar receptes que continguin un ingredient 
determinat. 
#### 4. Filtrar receptes per temps màxim de preparació: 
- Permet als usuaris trobar receptes que es preparin en un temps màxim 
determinat. 
#### 5. Obtenir receptes per tipus de menjar: 
- Permet als usuaris consultar receptes segons el tipus de menjar (Esmorzar, 
Dinar, Sopar). 
#### 6. Ordenar receptes per calories per ració: 
- Permet als usuaris ordenar les receptes per calories per ració, de manera 
ascendent o descendent. 

