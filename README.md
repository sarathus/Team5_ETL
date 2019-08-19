# Team5_ETL
Team: Jennis, Thea, Francis, Sarath
Project for Extract, Transform and Load into Database

Pandas used to read geoplaces2.csv ad ratings_final.csv files which provide location of #restaurants and ratings by user id
Pandas files created is "Merge_ETL_with_placeid.ipynb"
Merge_ETL_with_placeid is used in this projects which saves "output_merge_placeid.csv"
The transformation including merging of the two files, removing unncessary columns,removing duplicates and indexing by placeid

Table was created in Postgres under ratings to load up the "output_merge_placeid.csv" data

Sqlalchemy to read postgres database
