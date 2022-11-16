

CREATE TABLE "AlspacDataCatalogue" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	primary_email TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedAlspacDataSet" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	landing_page TEXT, 
	has_current_version TEXT, 
	primary_email TEXT, 
	main_publication TEXT, 
	publications TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AlspacDataCatalogue_primary_investigator_orcids" (
	backref_id TEXT, 
	primary_investigator_orcids TEXT, 
	PRIMARY KEY (backref_id, primary_investigator_orcids), 
	FOREIGN KEY(backref_id) REFERENCES "AlspacDataCatalogue" (id)
);

CREATE TABLE "AlspacDataCatalogue_named_alspac_data_set_collection" (
	backref_id TEXT, 
	named_alspac_data_set_collection TEXT, 
	PRIMARY KEY (backref_id, named_alspac_data_set_collection), 
	FOREIGN KEY(backref_id) REFERENCES "AlspacDataCatalogue" (id)
);

CREATE TABLE "NamedAlspacDataSet_primary_investigator_orcids" (
	backref_id TEXT, 
	primary_investigator_orcids TEXT, 
	PRIMARY KEY (backref_id, primary_investigator_orcids), 
	FOREIGN KEY(backref_id) REFERENCES "NamedAlspacDataSet" (id)
);

CREATE TABLE "NamedAlspacDataSet_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "NamedAlspacDataSet" (id)
);

CREATE TABLE "NamedAlspacDataSet_documentation_authors_orcids" (
	backref_id TEXT, 
	documentation_authors_orcids TEXT, 
	PRIMARY KEY (backref_id, documentation_authors_orcids), 
	FOREIGN KEY(backref_id) REFERENCES "NamedAlspacDataSet" (id)
);
