CREATE TABLE "output_merge_placeid" (
    "placeID" varchar(20)   NULL,
    "latitude" varchar(20)   NOT NULL,
	"longitude" varchar(20)   NOT NULL,
	"name" varchar(100)   NULL,
	"city" varchar(20)   NOT NULL,
	"userID" varchar(20)   NOT NULL,
	"rating" varchar (20)   NOT NULL,
	"food_rating" varchar (20)   NOT NULL,
	"service_rating" varchar (20)   NOT NULL,
	
	    CONSTRAINT "pk_output_merge_placeid" PRIMARY KEY (
        "name","city","food_rating"
     )
);
DROP TABLE IF EXISTS output_merge_placeid;

SELECT * from output_merge_placeid
