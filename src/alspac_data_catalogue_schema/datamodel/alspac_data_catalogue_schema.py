# Auto generated from alspac_data_catalogue_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-11-07T21:05:26
# Schema: alspac-data-catalogue-schema
#
# id: https://w3id.org/alspac/alspac-data-catalogue-schema
# description: This project is for the schema of alspac data catalogues and meta data on data sets
# license: MIT

import dataclasses
import sys
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import String

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
ALSPACDCS = CurieNamespace('alspacdcs', 'https://w3id.org/alspac/alspac-data-catalogue-schema/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DCTYPE = CurieNamespace('dctype', 'http://purl.org/dc/dcmitype/')
DOI = CurieNamespace('doi', 'https://doi.org/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LOCN = CurieNamespace('locn', 'http://www.w3.org/ns/locn#')
ODRL = CurieNamespace('odrl', 'http://www.w3.org/ns/odrl/2/')
OWL = CurieNamespace('owl', 'http://www.w3.org/2002/07/owl#')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
SPDX = CurieNamespace('spdx', 'http://spdx.org/rdf/terms#')
TIME = CurieNamespace('time', 'http://www.w3.org/2006/time#')
VCARD = CurieNamespace('vcard', 'http://www.w3.org/2006/vcard/ns#')
DEFAULT_ = ALSPACDCS


# Types

# Class references
class NamedThingId(extended_str):
    pass


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Thing
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = ALSPACDCS.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=ALSPACDCS.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=ALSPACDCS.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=ALSPACDCS.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=ALSPACDCS.primary_email, domain=None, range=Optional[str])

slots.primary_investigator_orcids = Slot(uri=ORCID.id, name="primary_investigator_orcids", curie=ORCID.curie('id'),
                   model_uri=ALSPACDCS.primary_investigator_orcids, domain=None, range=Optional[str])

slots.documentation_authors_orcids = Slot(uri=ORCID.id, name="documentation_authors_orcids", curie=ORCID.curie('id'),
                   model_uri=ALSPACDCS.documentation_authors_orcids, domain=None, range=Optional[str])

slots.named_alspac_data_set_collection = Slot(uri=ALSPACDCS.named_alspac_data_set_collection, name="named_alspac_data_set_collection", curie=ALSPACDCS.curie('named_alspac_data_set_collection'),
                   model_uri=ALSPACDCS.named_alspac_data_set_collection, domain=None, range=Optional[str])

slots.keywords = Slot(uri=ALSPACDCS.keywords, name="keywords", curie=ALSPACDCS.curie('keywords'),
                   model_uri=ALSPACDCS.keywords, domain=None, range=Optional[Union[str, List[str]]])

slots.code_name = Slot(uri=ALSPACDCS.code_name, name="code_name", curie=ALSPACDCS.curie('code_name'),
                   model_uri=ALSPACDCS.code_name, domain=None, range=Optional[str])

slots.authors = Slot(uri=ALSPACDCS.authors, name="authors", curie=ALSPACDCS.curie('authors'),
                   model_uri=ALSPACDCS.authors, domain=None, range=Optional[str])

slots.has_current_version = Slot(uri=DCAT.hasCurrentVersion, name="has_current_version", curie=DCAT.curie('hasCurrentVersion'),
                   model_uri=ALSPACDCS.has_current_version, domain=None, range=Optional[str])

slots.has_previous_version = Slot(uri=ALSPACDCS.has_previous_version, name="has_previous_version", curie=ALSPACDCS.curie('has_previous_version'),
                   model_uri=ALSPACDCS.has_previous_version, domain=None, range=Optional[str])

slots.has_next_version = Slot(uri=ALSPACDCS.has_next_version, name="has_next_version", curie=ALSPACDCS.curie('has_next_version'),
                   model_uri=ALSPACDCS.has_next_version, domain=None, range=Optional[str])

slots.is_current_version = Slot(uri=ALSPACDCS.is_current_version, name="is_current_version", curie=ALSPACDCS.curie('is_current_version'),
                   model_uri=ALSPACDCS.is_current_version, domain=None, range=Optional[str])

slots.has_parts = Slot(uri=ALSPACDCS.has_parts, name="has_parts", curie=ALSPACDCS.curie('has_parts'),
                   model_uri=ALSPACDCS.has_parts, domain=None, range=Optional[str])

slots.freeze_number = Slot(uri=ALSPACDCS.freeze_number, name="freeze_number", curie=ALSPACDCS.curie('freeze_number'),
                   model_uri=ALSPACDCS.freeze_number, domain=None, range=Optional[str])

slots.freeze_date = Slot(uri=ALSPACDCS.freeze_date, name="freeze_date", curie=ALSPACDCS.curie('freeze_date'),
                   model_uri=ALSPACDCS.freeze_date, domain=None, range=Optional[str])

slots.freeze_of_version = Slot(uri=ALSPACDCS.freeze_of_version, name="freeze_of_version", curie=ALSPACDCS.curie('freeze_of_version'),
                   model_uri=ALSPACDCS.freeze_of_version, domain=None, range=Optional[str])

slots.freeze_dataset = Slot(uri=ALSPACDCS.freeze_dataset, name="freeze_dataset", curie=ALSPACDCS.curie('freeze_dataset'),
                   model_uri=ALSPACDCS.freeze_dataset, domain=None, range=Optional[str])

slots.data_distribution = Slot(uri=ALSPACDCS.data_distribution, name="data_distribution", curie=ALSPACDCS.curie('data_distribution'),
                   model_uri=ALSPACDCS.data_distribution, domain=None, range=Optional[str])

slots.abstract_dataset_part = Slot(uri=ALSPACDCS.abstract_dataset_part, name="abstract_dataset_part", curie=ALSPACDCS.curie('abstract_dataset_part'),
                   model_uri=ALSPACDCS.abstract_dataset_part, domain=None, range=Optional[str])

slots.md5sum = Slot(uri=ALSPACDCS.md5sum, name="md5sum", curie=ALSPACDCS.curie('md5sum'),
                   model_uri=ALSPACDCS.md5sum, domain=None, range=Optional[str])

slots.filesize = Slot(uri=DCAT.byteSize, name="filesize", curie=DCAT.curie('byteSize'),
                   model_uri=ALSPACDCS.filesize, domain=None, range=Optional[str])

slots.filetype = Slot(uri=DCAT.mediaType, name="filetype", curie=DCAT.curie('mediaType'),
                   model_uri=ALSPACDCS.filetype, domain=None, range=Optional[str])

slots.number_of_samples = Slot(uri=ALSPACDCS.number_of_samples, name="number_of_samples", curie=ALSPACDCS.curie('number_of_samples'),
                   model_uri=ALSPACDCS.number_of_samples, domain=None, range=Optional[str])

slots.location_on_bc4 = Slot(uri=ALSPACDCS.location_on_bc4, name="location_on_bc4", curie=ALSPACDCS.curie('location_on_bc4'),
                   model_uri=ALSPACDCS.location_on_bc4, domain=None, range=Optional[str])

slots.location_on_bp = Slot(uri=ALSPACDCS.location_on_bp, name="location_on_bp", curie=ALSPACDCS.curie('location_on_bp'),
                   model_uri=ALSPACDCS.location_on_bp, domain=None, range=Optional[str])

slots.main_publication = Slot(uri=ALSPACDCS.main_publication, name="main_publication", curie=ALSPACDCS.curie('main_publication'),
                   model_uri=ALSPACDCS.main_publication, domain=None, range=Optional[str])

slots.landing_page = Slot(uri=DCAT.landingPage, name="landing_page", curie=DCAT.curie('landingPage'),
                   model_uri=ALSPACDCS.landing_page, domain=None, range=Optional[str])

slots.woc_file_md5sum = Slot(uri=ALSPACDCS.woc_file_md5sum, name="woc_file_md5sum", curie=ALSPACDCS.curie('woc_file_md5sum'),
                   model_uri=ALSPACDCS.woc_file_md5sum, domain=None, range=Optional[str])

slots.git_tag = Slot(uri=ALSPACDCS.git_tag, name="git_tag", curie=ALSPACDCS.curie('git_tag'),
                   model_uri=ALSPACDCS.git_tag, domain=None, range=Optional[str])

slots.qc_description = Slot(uri=ALSPACDCS.qc_description, name="qc_description", curie=ALSPACDCS.curie('qc_description'),
                   model_uri=ALSPACDCS.qc_description, domain=None, range=Optional[str])

slots.publications = Slot(uri=ALSPACDCS.publications, name="publications", curie=ALSPACDCS.curie('publications'),
                   model_uri=ALSPACDCS.publications, domain=None, range=Optional[str])

slots.data_distributions = Slot(uri=ALSPACDCS.data_distributions, name="data_distributions", curie=ALSPACDCS.curie('data_distributions'),
                   model_uri=ALSPACDCS.data_distributions, domain=None, range=Optional[str])

slots.number_of_participants = Slot(uri=ALSPACDCS.number_of_participants, name="number_of_participants", curie=ALSPACDCS.curie('number_of_participants'),
                   model_uri=ALSPACDCS.number_of_participants, domain=None, range=Optional[str])