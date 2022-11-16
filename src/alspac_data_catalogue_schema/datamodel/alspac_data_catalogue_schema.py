# Auto generated from alspac_data_catalogue_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-11-16T15:30:32
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
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
ORCID = CurieNamespace('ORCID', 'https://orcid.org/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
ALSPAC_DATA_CATALOGUE_SCHEMA = CurieNamespace('alspac_data_catalogue_schema', 'https://w3id.org/alspac/alspac-data-catalogue-schema/')
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
DEFAULT_ = ALSPAC_DATA_CATALOGUE_SCHEMA


# Types

# Class references
class NamedThingId(URIorCURIE):
    pass


class AlspacDataCatalogueId(NamedThingId):
    pass


class NamedAlspacDataSetId(NamedThingId):
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
    class_model_uri: ClassVar[URIRef] = ALSPAC_DATA_CATALOGUE_SCHEMA.NamedThing

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


@dataclass
class AlspacDataCatalogue(NamedThing):
    """
    Represents an alspac data catalogue. That is a set of named alspac data sets.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Catalog
    class_class_curie: ClassVar[str] = "dcat:Catalog"
    class_name: ClassVar[str] = "AlspacDataCatalogue"
    class_model_uri: ClassVar[URIRef] = ALSPAC_DATA_CATALOGUE_SCHEMA.AlspacDataCatalogue

    id: Union[str, AlspacDataCatalogueId] = None
    primary_investigator_orcids: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    primary_email: Optional[str] = None
    named_alspac_data_set_collection: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlspacDataCatalogueId):
            self.id = AlspacDataCatalogueId(self.id)

        if not isinstance(self.primary_investigator_orcids, list):
            self.primary_investigator_orcids = [self.primary_investigator_orcids] if self.primary_investigator_orcids is not None else []
        self.primary_investigator_orcids = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.primary_investigator_orcids]

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if not isinstance(self.named_alspac_data_set_collection, list):
            self.named_alspac_data_set_collection = [self.named_alspac_data_set_collection] if self.named_alspac_data_set_collection is not None else []
        self.named_alspac_data_set_collection = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.named_alspac_data_set_collection]

        super().__post_init__(**kwargs)


@dataclass
class NamedAlspacDataSet(NamedThing):
    """
    Represents a named_alspac_data_set. That is a set of data that has been collected or produced to be named, reused
    and distributed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Dataset
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "NamedAlspacDataSet"
    class_model_uri: ClassVar[URIRef] = ALSPAC_DATA_CATALOGUE_SCHEMA.NamedAlspacDataSet

    id: Union[str, NamedAlspacDataSetId] = None
    landing_page: Optional[str] = None
    primary_investigator_orcids: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    keywords: Optional[Union[str, List[str]]] = empty_list()
    has_current_version: Optional[Union[str, URIorCURIE]] = None
    primary_email: Optional[str] = None
    documentation_authors_orcids: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()
    main_publication: Optional[str] = None
    publications: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedAlspacDataSetId):
            self.id = NamedAlspacDataSetId(self.id)

        if self.landing_page is not None and not isinstance(self.landing_page, str):
            self.landing_page = str(self.landing_page)

        if not isinstance(self.primary_investigator_orcids, list):
            self.primary_investigator_orcids = [self.primary_investigator_orcids] if self.primary_investigator_orcids is not None else []
        self.primary_investigator_orcids = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.primary_investigator_orcids]

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if self.has_current_version is not None and not isinstance(self.has_current_version, URIorCURIE):
            self.has_current_version = URIorCURIE(self.has_current_version)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if not isinstance(self.documentation_authors_orcids, list):
            self.documentation_authors_orcids = [self.documentation_authors_orcids] if self.documentation_authors_orcids is not None else []
        self.documentation_authors_orcids = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.documentation_authors_orcids]

        if self.main_publication is not None and not isinstance(self.main_publication, str):
            self.main_publication = str(self.main_publication)

        if self.publications is not None and not isinstance(self.publications, str):
            self.publications = str(self.publications)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.primary_email, domain=None, range=Optional[str])

slots.primary_investigator_orcids = Slot(uri=ORCID.id, name="primary_investigator_orcids", curie=ORCID.curie('id'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.primary_investigator_orcids, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.documentation_authors_orcids = Slot(uri=ORCID.id, name="documentation_authors_orcids", curie=ORCID.curie('id'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.documentation_authors_orcids, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.named_alspac_data_set_collection = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.named_alspac_data_set_collection, name="named_alspac_data_set_collection", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('named_alspac_data_set_collection'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.named_alspac_data_set_collection, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.keywords = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.keywords, name="keywords", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('keywords'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.keywords, domain=None, range=Optional[Union[str, List[str]]])

slots.has_current_version = Slot(uri=DCAT.hasCurrentVersion, name="has_current_version", curie=DCAT.curie('hasCurrentVersion'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.has_current_version, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.main_publication = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.main_publication, name="main_publication", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('main_publication'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.main_publication, domain=None, range=Optional[str])

slots.landing_page = Slot(uri=DCAT.landingPage, name="landing_page", curie=DCAT.curie('landingPage'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.landing_page, domain=None, range=Optional[str])

slots.publications = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.publications, name="publications", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('publications'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.publications, domain=None, range=Optional[str])