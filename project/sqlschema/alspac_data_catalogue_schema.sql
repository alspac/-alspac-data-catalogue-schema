

CREATE TABLE abstract_dataset_part (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	data_distribution TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE alspac_data_catalogue (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	primary_investigator_orcid TEXT, 
	primary_email TEXT, 
	named_alspac_data_set_collection TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE alspac_data_set_version (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	version_number TEXT, 
	version_date TEXT, 
	keywords TEXT, 
	has_previous_version TEXT, 
	has_next_verion TEXT, 
	is_current_version TEXT, 
	primary_email TEXT, 
	authors TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE alspac_data_set_version_freeze (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	freeze_number TEXT, 
	freeze_date TEXT, 
	freeze_of_version TEXT, 
	freeze_dataset TEXT, 
	primary_email TEXT, 
	authors TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE data_distribution (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	abstract_dataset_part TEXT, 
	md5sum TEXT, 
	filesize TEXT, 
	filetype TEXT, 
	number_of_samples TEXT, 
	location_on_bc4 TEXT, 
	location_on_bp TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE named_alspac_data_set (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	code_name TEXT, 
	primary_investigator_orcid TEXT, 
	keywords TEXT, 
	has_version TEXT, 
	primary_email TEXT, 
	authors TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE named_alspac_data_set_collection (
	entries TEXT, 
	PRIMARY KEY (entries)
);

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);
