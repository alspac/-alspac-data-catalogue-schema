

CREATE TABLE alspac_data_catalogue (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	primary_email TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE alspac_data_catalogue_primary_investigator_orcids (
	backref_id TEXT, 
	primary_investigator_orcids TEXT, 
	PRIMARY KEY (backref_id, primary_investigator_orcids), 
	FOREIGN KEY(backref_id) REFERENCES alspac_data_catalogue (id)
);
