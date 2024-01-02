CREATE TABLE "Users" (
	"UserID"	INTEGER NOT NULL,
	"Email"	TEXT NOT NULL,
	"Password"	TEXT NOT NULL,
	"FirstName"	TEXT NOT NULL,
	"LastName"	TEXT NOT NULL,
	"Phone Number"	INTEGER NOT NULL,
	"Description" TEXT NOT NULL,
	"associateCommunity" TEXT,
	"LinkedIn"	TEXT,
	"Tokens"	INTEGER,
	"Community "	TEXT,
	"Company"	TEXT,
	"Mentor Status"	INTEGER DEFAULT 0,
	PRIMARY KEY("UserID" AUTOINCREMENT)
);
	
CREATE TABLE "communities" (
	"name" TEXT NOT NULL,
	"tokenAmount" TEXT NOT NULL,
	"private" BOOLEAN,

	PRIMARY KEY("name")
);
INSERT INTO 'Users'('Email','Password','FirstName','LastName','Phone Number','Description','associateCommunity','Tokens') VALUES ('craigdavid@gmail.com', 'Starworld123!','Craig','David','01252671872','specialising in python and leadership skills','students','1');
INSERT INTO 'Users'('Email','Password','FirstName','LastName','Phone Number','Description','associateCommunity','Tokens') VALUES ('crudelations@outlook.com', 'Stfujamal!','Omar','Ikram','07375748765','experience in the operations sector','students','2');
INSERT INTO 'Users'('Email','Password','FirstName','LastName','Phone Number','Description','associateCommunity','Tokens') VALUES ('basilpesto@hotmail.com', 'chickennrice123','basil','ahmed','01758685748','back end specialist, database knowledge','Microsoft','1');
INSERT INTO 'Users'('Email','Password','FirstName','LastName','Phone Number','Description','associateCommunity','Tokens') VALUES ('thomasjefferson@hotmail.com', 'politics55!','Thomas','Jefferson','07866913748','Full stack experience, 10 years in development field','Microsoft','1');
INSERT INTO 'Users'('Email','Password','FirstName','LastName','Phone Number','Description','associateCommunity','Tokens') VALUES ('trefflerbusiness@outlook.com', 'SASS1999!','Alan','Treffler','09866726733','CFO of PEGA systems, head of european team, previously business officer','PEGA','3');
INSERT INTO 'Users'('Email','Password','FirstName','LastName','Phone Number','Description','associateCommunity','Tokens') VALUES ('Andrew Reynolds', 'Baker4!','Andrew','Reynolds','01252763827','Owner of baker skateboards, human resources skills, previously child prodigy','Baker','0');


CREATE TABLE "ApprovedMentors" (
	"UserID"	INTEGER,
	"Description"	TEXT,
	"Tags"	TEXT
);


CREATE TABLE "Mentors" (
	"UserID"	INTEGER,
	"Description"	TEXT,
	"Tags"	TEXT,
	"Image" BLOB
);

CREATE TABLE "Pools" (
    "PoolID" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "Name" TEXT NOT NULL,
    "Description" TEXT NOT NULL
);

CREATE TABLE "Moderator" (
	"Email"	TEXT NOT NULL,
	"Password"	TEXT NOT NULL
);

INSERT INTO "Moderator" ("Email","Password")
	VALUES ("qq@q", "qq")

CREATE TABLE "PendingMentors" (
	"Email"	TEXT,
	"Description"	TEXT
);