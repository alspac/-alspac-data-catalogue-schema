

CREATE TABLE "AlspacDataCatalogue" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	primary_investigator_orcids TEXT, 
	primary_email TEXT, 
	named_alspac_datasets TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AlspacDataSetVersion" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	qc_description TEXT, 
	version_of TEXT, 
	is_current_version TEXT, 
	has_previous_version TEXT, 
	has_next_version TEXT, 
	has_parts TEXT, 
	has_freezes TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(version_of) REFERENCES "NamedAlspacDataset" (id)
);

CREATE TABLE "DataDistribution" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	md5sum TEXT, 
	filesize TEXT, 
	filetype TEXT, 
	number_of_participants INTEGER, 
	number_of_gene_expression_probe_values INTEGER, 
	number_of_variants INTEGER, 
	number_of_cpgs INTEGER, 
	required_files TEXT, 
	"belongsToContainer" TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "DatasetPart" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	data_distributions TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "NamedAlspacDataset" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	landing_page_url TEXT, 
	primary_investigator_orcids TEXT, 
	has_current_version TEXT, 
	versions TEXT, 
	primary_email TEXT, 
	documentation_authors_orcids TEXT, 
	main_publication_doi TEXT, 
	publications_dois TEXT, 
	in_catalog TEXT, 
	derived_from TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(has_current_version) REFERENCES "AlspacDataSetVersion" (id), 
	FOREIGN KEY(main_publication_doi) REFERENCES "Paper" (id), 
	FOREIGN KEY(in_catalog) REFERENCES "AlspacDataCatalogue" (id)
);

CREATE TABLE "Paper" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "Person" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	PRIMARY KEY (id)
);

CREATE TABLE "AlspacDataSetVersionFreeze" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	linker_file_md5sum TEXT, 
	freeze_size TEXT, 
	woc_file_md5sum TEXT, 
	all_individuals_to_exclude_md5sum TEXT, 
	is_current_freeze BOOLEAN, 
	freeze_number TEXT, 
	freeze_date DATE, 
	previous_freeze TEXT, 
	next_freeze TEXT, 
	freeze_of_alspac_dataset_version TEXT, 
	freeze_of_named_alspac_dataset TEXT, 
	primary_email TEXT, 
	git_tag TEXT, 
	has_parts TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(previous_freeze) REFERENCES "AlspacDataSetVersionFreeze" (id), 
	FOREIGN KEY(next_freeze) REFERENCES "AlspacDataSetVersionFreeze" (id), 
	FOREIGN KEY(freeze_of_alspac_dataset_version) REFERENCES "AlspacDataSetVersion" (id), 
	FOREIGN KEY(freeze_of_named_alspac_dataset) REFERENCES "NamedAlspacDataset" (id)
);

CREATE TABLE "KnownIssue" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	issue_description TEXT, 
	logged_by TEXT, 
	logged_date TEXT, 
	"AlspacDataSetVersion_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlspacDataSetVersion_id") REFERENCES "AlspacDataSetVersion" (id)
);

CREATE TABLE "QCKeyValue" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	qc_key TEXT, 
	qc_value TEXT, 
	"AlspacDataSetVersion_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlspacDataSetVersion_id") REFERENCES "AlspacDataSetVersion" (id)
);

CREATE TABLE "Script" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	md5sum TEXT, 
	filesize TEXT, 
	filetype TEXT, 
	"AlspacDataSetVersion_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlspacDataSetVersion_id") REFERENCES "AlspacDataSetVersion" (id)
);

CREATE TABLE "UGKeyValue" (
	id TEXT NOT NULL, 
	name TEXT, 
	description TEXT, 
	ug_key TEXT, 
	ug_value TEXT, 
	"AlspacDataSetVersion_id" TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY("AlspacDataSetVersion_id") REFERENCES "AlspacDataSetVersion" (id)
);

CREATE TABLE "AlspacDataCatalogue_see_also" (
	backref_id TEXT, 
	see_also TEXT, 
	PRIMARY KEY (backref_id, see_also), 
	FOREIGN KEY(backref_id) REFERENCES "AlspacDataCatalogue" (id)
);

CREATE TABLE "AlspacDataSetVersion_authors" (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES "AlspacDataSetVersion" (id)
);

CREATE TABLE "NamedAlspacDataset_keywords" (
	backref_id TEXT, 
	keywords TEXT, 
	PRIMARY KEY (backref_id, keywords), 
	FOREIGN KEY(backref_id) REFERENCES "NamedAlspacDataset" (id)
);

CREATE TABLE "Script_authors" (
	backref_id TEXT, 
	authors TEXT, 
	PRIMARY KEY (backref_id, authors), 
	FOREIGN KEY(backref_id) REFERENCES "Script" (id)
);
