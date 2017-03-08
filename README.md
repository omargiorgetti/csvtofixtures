# csvtofixtures
Converting csv to Django json fixtures file.
## Two examples

### Simple one
 
In the django model is present a class Comune.
 Starting from a csv with the name, code and other information, we have to insert data into the database using the django loaddata command and the Comune.json file
 
### Complex one
As before but more complex.
In the Django model are present two classes, Result and Tipo and starting from a csv file with tipo description, we create a Result.json file the code as a result of the lookup of the description in the tipo.json file.





