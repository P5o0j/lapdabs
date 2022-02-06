PRAGMA foreign_keys = ON;

CREATE DATABASE thisAPP;

CREATE TABLE "PaymentMethod" (
	"paycde"	VARCHAR(10) NOT NULL UNIQUE,
	"method"	VARCHAR(20) NOT NULL,
	PRIMARY KEY("paycde")
);


CREATE TABLE "FuelType" (
	"fuelcde"	VARCHAR(10) NOT NULL UNIQUE,
	"type"	VARCHAR(20) NOT NULL,
	PRIMARY KEY("fuelcde")
);


CREATE TABLE "vehicles" (
	"regnum"	VARCHAR(15) NOT NULL UNIQUE,
	"make"	VARCHAR(20) NOT NULL,
	"model"	VARCHAR(20) NOT NULL,
	"fuelcde"	VARCHAR(20) NOT NULL,
	"millage"	INTEGER NOT NULL,
	"colour"	VARCHAR(20),
	"MOT"	date,
	PRIMARY KEY("regnum"),
	FOREIGN KEY ("fuelcde")
   REFERENCES FuelType("fuelcde")
);


CREATE TABLE "customer" (
	"cuscde"	VARCHAR(10) NOT NULL UNIQUE,
	"regnum"	VARCHAR(20) NOT NULL UNIQUE,
	"name"	VARCHAR(20) NOT NULL,
	"surname"	VARCHAR(20) NOT NULL,
	"company"	VARCHAR(20),
	"addrl1"	VARCHAR(30),
	"addrl2"	VARCHAR(30),
	"addrl3"	VARCHAR(30),
	"postcode"	VARCHAR(20),
	"city"	VARCHAR(20),
	"phonum"	INTEGER,
	"email"	VARCHAR(30),
	PRIMARY KEY("cuscde"),
	FOREIGN KEY("regnum") REFERENCES "vehicles"("regnum")
);



CREATE TABLE "service" (
	"jobcde"	VARCHAR(10) NOT NULL UNIQUE,
	"description"	VARCHAR(99),
	"partno"	VARCHAR(15) UNIQUE,
	"duration"	INTEGER,
	"price"	DOUBLE(6, 2),
	PRIMARY KEY("jobcde")
);


CREATE TABLE "visit" (
	"date"	date NOT NULL,
	"regnum"	VARCHAR(20) NOT NULL,
	"cuscde"	INTEGER NOT NULL,
	"qty"		INTEGER NOT NULL,
	"paycde"	INTEGER NOT NULL,
	"jobcde"	INTEGER NOT NULL,
	"duration"	INTEGER,
	"price"	DOUBLE(6, 2),
	"recheck"	BOOL NOT NULL,
	FOREIGN KEY("jobcde") REFERENCES "service"("jobcde"),
	FOREIGN KEY("cuscde") REFERENCES "customer"("cuscde"),
	FOREIGN KEY("paycde") REFERENCES "paymet"("paycde"),
	FOREIGN KEY("regnum") REFERENCES "customer"("regnum")
);





