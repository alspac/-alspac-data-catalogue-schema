# Auto generated from alspac_data_catalogue_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-10-31T11:43:24
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
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
ALSPAC_DATA_CATALOGUE_SCHEMA = CurieNamespace('alspac_data_catalogue_schema', 'https://w3id.org/alspac/alspac-data-catalogue-schema/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
DC = CurieNamespace('dc', 'http://purl.org/dc/elements/1.1/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DCTYPE = CurieNamespace('dctype', 'http://purl.org/dc/dcmitype/')
EXAMPLE = CurieNamespace('example', 'https://example.org/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LOCN = CurieNamespace('locn', 'http://www.w3.org/ns/locn#')
ODRL = CurieNamespace('odrl', 'http://www.w3.org/ns/odrl/2/')
ORCID = CurieNamespace('orcid', 'http://example.org/UNKNOWN/orcid/')
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


class AlspacDataSetVersionId(NamedThingId):
    pass


class AlspacDataSetVersionFreezeId(NamedThingId):
    pass


class AbstractDatasetPartId(NamedThingId):
    pass


class DataDistributionId(NamedThingId):
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
    class_name: ClassVar[str] = "alspac_data_catalogue"
    class_model_uri: ClassVar[URIRef] = ALSPAC_DATA_CATALOGUE_SCHEMA.AlspacDataCatalogue

    id: Union[str, AlspacDataCatalogueId] = None
    primary_investigator_orcid: Optional[Union[str, URIorCURIE]] = None
    primary_email: Optional[str] = None
    named_alspac_data_set_collection: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlspacDataCatalogueId):
            self.id = AlspacDataCatalogueId(self.id)

        if self.primary_investigator_orcid is not None and not isinstance(self.primary_investigator_orcid, URIorCURIE):
            self.primary_investigator_orcid = URIorCURIE(self.primary_investigator_orcid)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.named_alspac_data_set_collection is not None and not isinstance(self.named_alspac_data_set_collection, str):
            self.named_alspac_data_set_collection = str(self.named_alspac_data_set_collection)

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
    class_name: ClassVar[str] = "named_alspac_data_set"
    class_model_uri: ClassVar[URIRef] = ALSPAC_DATA_CATALOGUE_SCHEMA.NamedAlspacDataSet

    id: Union[str, NamedAlspacDataSetId] = None
    code_name: Optional[str] = None
    primary_investigator_orcid: Optional[Union[str, URIorCURIE]] = None
    keywords: Optional[str] = None
    has_version: Optional[str] = None
    primary_email: Optional[str] = None
    authors: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedAlspacDataSetId):
            self.id = NamedAlspacDataSetId(self.id)

        if self.code_name is not None and not isinstance(self.code_name, str):
            self.code_name = str(self.code_name)

        if self.primary_investigator_orcid is not None and not isinstance(self.primary_investigator_orcid, URIorCURIE):
            self.primary_investigator_orcid = URIorCURIE(self.primary_investigator_orcid)

        if self.keywords is not None and not isinstance(self.keywords, str):
            self.keywords = str(self.keywords)

        if self.has_version is not None and not isinstance(self.has_version, str):
            self.has_version = str(self.has_version)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.authors is not None and not isinstance(self.authors, str):
            self.authors = str(self.authors)

        super().__post_init__(**kwargs)


@dataclass
class NamedAlspacDataSetCollection(YAMLRoot):
    """
    A holder for named_alspac_data_set objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSPAC_DATA_CATALOGUE_SCHEMA.NamedAlspacDataSetCollection
    class_class_curie: ClassVar[str] = "alspac_data_catalogue_schema:NamedAlspacDataSetCollection"
    class_name: ClassVar[str] = "named_alspac_data_set_collection"
    class_model_uri: ClassVar[URIRef] = ALSPAC_DATA_CATALOGUE_SCHEMA.NamedAlspacDataSetCollection

    entries: Optional[Union[Dict[Union[str, NamedAlspacDataSetId], Union[dict, NamedAlspacDataSet]], List[Union[dict, NamedAlspacDataSet]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=NamedAlspacDataSet, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class AlspacDataSetVersion(NamedThing):
    """
    Represents a version of a named_alspac_data_set. That is a specific set of data which internal people to alspac
    can use.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Dataset
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "alspac_data_set_version"
    class_model_uri: ClassVar[URIRef] = ALSPAC_DATA_CATALOGUE_SCHEMA.AlspacDataSetVersion

    id: Union[str, AlspacDataSetVersionId] = None
    version_number: Optional[str] = None
    version_date: Optional[str] = None
    keywords: Optional[str] = None
    has_previous_version: Optional[str] = None
    has_next_verion: Optional[str] = None
    is_current_version: Optional[str] = None
    primary_email: Optional[str] = None
    authors: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlspacDataSetVersionId):
            self.id = AlspacDataSetVersionId(self.id)

        if self.version_number is not None and not isinstance(self.version_number, str):
            self.version_number = str(self.version_number)

        if self.version_date is not None and not isinstance(self.version_date, str):
            self.version_date = str(self.version_date)

        if self.keywords is not None and not isinstance(self.keywords, str):
            self.keywords = str(self.keywords)

        if self.has_previous_version is not None and not isinstance(self.has_previous_version, str):
            self.has_previous_version = str(self.has_previous_version)

        if self.has_next_verion is not None and not isinstance(self.has_next_verion, str):
            self.has_next_verion = str(self.has_next_verion)

        if self.is_current_version is not None and not isinstance(self.is_current_version, str):
            self.is_current_version = str(self.is_current_version)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.authors is not None and not isinstance(self.authors, str):
            self.authors = str(self.authors)

        super().__post_init__(**kwargs)


@dataclass
class AlspacDataSetVersionFreeze(NamedThing):
    """
    Represents a freeze of a version of named_alspac_data_set. That is a specific set of data which can be applied to
    use.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Dataset
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "alspac_data_set_version_freeze"
    class_model_uri: ClassVar[URIRef] = ALSPAC_DATA_CATALOGUE_SCHEMA.AlspacDataSetVersionFreeze

    id: Union[str, AlspacDataSetVersionFreezeId] = None
    freeze_number: Optional[str] = None
    freeze_date: Optional[str] = None
    freeze_of_version: Optional[str] = None
    freeze_dataset: Optional[str] = None
    primary_email: Optional[str] = None
    authors: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlspacDataSetVersionFreezeId):
            self.id = AlspacDataSetVersionFreezeId(self.id)

        if self.freeze_number is not None and not isinstance(self.freeze_number, str):
            self.freeze_number = str(self.freeze_number)

        if self.freeze_date is not None and not isinstance(self.freeze_date, str):
            self.freeze_date = str(self.freeze_date)

        if self.freeze_of_version is not None and not isinstance(self.freeze_of_version, str):
            self.freeze_of_version = str(self.freeze_of_version)

        if self.freeze_dataset is not None and not isinstance(self.freeze_dataset, str):
            self.freeze_dataset = str(self.freeze_dataset)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.authors is not None and not isinstance(self.authors, str):
            self.authors = str(self.authors)

        super().__post_init__(**kwargs)


@dataclass
class AbstractDatasetPart(NamedThing):
    """
    Represents an abstract part of named alspac data set, in a version or freeze. For example in an omics context the
    data collected for a single chr which would be made availble as a dcat distribution of this type of dataset which
    would be of a specific file.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Dataset
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "abstract_dataset_part"
    class_model_uri: ClassVar[URIRef] = ALSPAC_DATA_CATALOGUE_SCHEMA.AbstractDatasetPart

    id: Union[str, AbstractDatasetPartId] = None
    data_distribution: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AbstractDatasetPartId):
            self.id = AbstractDatasetPartId(self.id)

        if self.data_distribution is not None and not isinstance(self.data_distribution, str):
            self.data_distribution = str(self.data_distribution)

        super().__post_init__(**kwargs)


@dataclass
class DataDistribution(NamedThing):
    """
    A dataset distribution has a loaction, file type and file size.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Distribution
    class_class_curie: ClassVar[str] = "dcat:Distribution"
    class_name: ClassVar[str] = "data_distribution"
    class_model_uri: ClassVar[URIRef] = ALSPAC_DATA_CATALOGUE_SCHEMA.DataDistribution

    id: Union[str, DataDistributionId] = None
    abstract_dataset_part: Optional[str] = None
    md5sum: Optional[str] = None
    filesize: Optional[str] = None
    filetype: Optional[str] = None
    number_of_samples: Optional[str] = None
    location_on_bc4: Optional[str] = None
    location_on_bp: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataDistributionId):
            self.id = DataDistributionId(self.id)

        if self.abstract_dataset_part is not None and not isinstance(self.abstract_dataset_part, str):
            self.abstract_dataset_part = str(self.abstract_dataset_part)

        if self.md5sum is not None and not isinstance(self.md5sum, str):
            self.md5sum = str(self.md5sum)

        if self.filesize is not None and not isinstance(self.filesize, str):
            self.filesize = str(self.filesize)

        if self.filetype is not None and not isinstance(self.filetype, str):
            self.filetype = str(self.filetype)

        if self.number_of_samples is not None and not isinstance(self.number_of_samples, str):
            self.number_of_samples = str(self.number_of_samples)

        if self.location_on_bc4 is not None and not isinstance(self.location_on_bc4, str):
            self.location_on_bc4 = str(self.location_on_bc4)

        if self.location_on_bp is not None and not isinstance(self.location_on_bp, str):
            self.location_on_bp = str(self.location_on_bp)

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

slots.primary_investigator_orcid = Slot(uri=ORCID.id, name="primary_investigator_orcid", curie=ORCID.curie('id'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.primary_investigator_orcid, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.named_alspac_data_set_collection = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.named_alspac_data_set_collection, name="named_alspac_data_set_collection", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('named_alspac_data_set_collection'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.named_alspac_data_set_collection, domain=None, range=Optional[str])

slots.keywords = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.keywords, name="keywords", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('keywords'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.keywords, domain=None, range=Optional[str])

slots.code_name = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.code_name, name="code_name", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('code_name'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.code_name, domain=None, range=Optional[str])

slots.authors = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.authors, name="authors", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('authors'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.authors, domain=None, range=Optional[str])

slots.has_version = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.has_version, name="has_version", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('has_version'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.has_version, domain=None, range=Optional[str])

slots.version_number = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.version_number, name="version_number", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('version_number'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.version_number, domain=None, range=Optional[str])

slots.version_date = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.version_date, name="version_date", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('version_date'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.version_date, domain=None, range=Optional[str])

slots.has_previous_version = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.has_previous_version, name="has_previous_version", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('has_previous_version'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.has_previous_version, domain=None, range=Optional[str])

slots.has_next_verion = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.has_next_verion, name="has_next_verion", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('has_next_verion'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.has_next_verion, domain=None, range=Optional[str])

slots.is_current_version = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.is_current_version, name="is_current_version", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('is_current_version'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.is_current_version, domain=None, range=Optional[str])

slots.freeze_number = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.freeze_number, name="freeze_number", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('freeze_number'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.freeze_number, domain=None, range=Optional[str])

slots.freeze_date = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.freeze_date, name="freeze_date", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('freeze_date'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.freeze_date, domain=None, range=Optional[str])

slots.freeze_of_version = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.freeze_of_version, name="freeze_of_version", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('freeze_of_version'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.freeze_of_version, domain=None, range=Optional[str])

slots.freeze_dataset = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.freeze_dataset, name="freeze_dataset", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('freeze_dataset'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.freeze_dataset, domain=None, range=Optional[str])

slots.data_distribution = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.data_distribution, name="data_distribution", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('data_distribution'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.data_distribution, domain=None, range=Optional[str])

slots.abstract_dataset_part = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.abstract_dataset_part, name="abstract_dataset_part", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('abstract_dataset_part'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.abstract_dataset_part, domain=None, range=Optional[str])

slots.md5sum = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.md5sum, name="md5sum", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('md5sum'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.md5sum, domain=None, range=Optional[str])

slots.filesize = Slot(uri=DCAT.byteSize, name="filesize", curie=DCAT.curie('byteSize'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.filesize, domain=None, range=Optional[str])

slots.filetype = Slot(uri=DCAT.mediaType, name="filetype", curie=DCAT.curie('mediaType'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.filetype, domain=None, range=Optional[str])

slots.number_of_samples = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.number_of_samples, name="number_of_samples", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('number_of_samples'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.number_of_samples, domain=None, range=Optional[str])

slots.location_on_bc4 = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.location_on_bc4, name="location_on_bc4", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('location_on_bc4'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.location_on_bc4, domain=None, range=Optional[str])

slots.location_on_bp = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.location_on_bp, name="location_on_bp", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('location_on_bp'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.location_on_bp, domain=None, range=Optional[str])

slots.namedAlspacDataSetCollection__entries = Slot(uri=ALSPAC_DATA_CATALOGUE_SCHEMA.entries, name="namedAlspacDataSetCollection__entries", curie=ALSPAC_DATA_CATALOGUE_SCHEMA.curie('entries'),
                   model_uri=ALSPAC_DATA_CATALOGUE_SCHEMA.namedAlspacDataSetCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, NamedAlspacDataSetId], Union[dict, NamedAlspacDataSet]], List[Union[dict, NamedAlspacDataSet]]]])