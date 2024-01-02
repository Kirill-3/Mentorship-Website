CREATE TABLE "Users" (
	"UserID"	INTEGER NOT NULL,
	"Email"	TEXT NOT NULL,
	"Password"	TEXT NOT NULL,
	"First Name"	TEXT NOT NULL,
	"Last Name"	TEXT NOT NULL,
	"Phone Number"	INTEGER NOT NULL,
	"LinkedIn"	TEXT,
	"Tokens"	INTEGER,
	"Community "	TEXT,
	"Company"	TEXT,
	"Mentor Status"	INTEGER,
	PRIMARY KEY("UserID" AUTOINCREMENT)
);

CREATE TABLE "Mentors" (
	"UserID"	INTEGER,
	"Description"	TEXT,
	"Tags"	TEXT
);