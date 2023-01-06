# Auto generated from alspac_data_catalogue_schema.yaml by pythongen.py version: 0.9.0
# Generation date: 2023-01-06T11:39:59
# Schema: alspac-data-catalogue-schema
#
# id: http://purl.org/alspac/alspac-data-catalogue-schema/
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
from linkml_runtime.linkml_model.types import Boolean, Date, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
IAO = CurieNamespace('IAO', 'http://purl.obolibrary.org/obo/IAO_')
ORCID = CurieNamespace('ORCID', 'http://identifiers.org/orcid/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
ALSPACDCS = CurieNamespace('alspacdcs', 'http://purl.org/alspac/alspac-data-catalogue-schema/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/vocab/')
DCAT = CurieNamespace('dcat', 'http://www.w3.org/ns/dcat#')
DCE = CurieNamespace('dce', 'http://purl.org/dc/elements/1.1/')
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DCTYPES = CurieNamespace('dctypes', 'http://purl.org/dc/dcmitype/')
DOI = CurieNamespace('doi', 'https://doi.org/')
EXAMPLE = CurieNamespace('example', 'http://example.org/rdf#')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
IDENTIFIER = CurieNamespace('identifier', 'https://registry.identifiers.org/registry/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
LOCN = CurieNamespace('locn', 'http://www.w3.org/ns/locn#')
NFO = CurieNamespace('nfo', 'http://www.semanticdesktop.org/ontologies/2007/03/22/nfo/v1.2/')
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
class NamedThingId(URIorCURIE):
    pass


class PersonId(NamedThingId):
    pass


class PaperId(NamedThingId):
    pass


class AlspacDataCatalogueId(NamedThingId):
    pass


class NamedAlspacDatasetId(NamedThingId):
    pass


class AlspacDataSetVersionId(NamedThingId):
    pass


class ScriptId(NamedThingId):
    pass


class AlspacDataSetVersionFreezeId(NamedThingId):
    pass


class DatasetPartId(NamedThingId):
    pass


class DataDistributionId(NamedThingId):
    pass


class KnownIssueId(NamedThingId):
    pass


class QCKeyValueId(NamedThingId):
    pass


class UGKeyValueId(NamedThingId):
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


@dataclass
class Person(NamedThing):
    """
    A person
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = FOAF.Person
    class_class_curie: ClassVar[str] = "foaf:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = ALSPACDCS.Person

    id: Union[str, PersonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        super().__post_init__(**kwargs)


@dataclass
class Paper(NamedThing):
    """
    a scientific paper
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSPACDCS.Paper
    class_class_curie: ClassVar[str] = "alspacdcs:Paper"
    class_name: ClassVar[str] = "Paper"
    class_model_uri: ClassVar[URIRef] = ALSPACDCS.Paper

    id: Union[str, PaperId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PaperId):
            self.id = PaperId(self.id)

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
    class_model_uri: ClassVar[URIRef] = ALSPACDCS.AlspacDataCatalogue

    id: Union[str, AlspacDataCatalogueId] = None
    primary_investigator_orcids: Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]] = empty_dict()
    primary_email: Optional[str] = None
    named_alspac_datasets: Optional[Union[Dict[Union[str, NamedAlspacDatasetId], Union[dict, "NamedAlspacDataset"]], List[Union[dict, "NamedAlspacDataset"]]]] = empty_dict()
    see_also: Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlspacDataCatalogueId):
            self.id = AlspacDataCatalogueId(self.id)

        self._normalize_inlined_as_list(slot_name="primary_investigator_orcids", slot_type=Person, key_name="id", keyed=True)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        self._normalize_inlined_as_list(slot_name="named_alspac_datasets", slot_type=NamedAlspacDataset, key_name="id", keyed=True)

        if not isinstance(self.see_also, list):
            self.see_also = [self.see_also] if self.see_also is not None else []
        self.see_also = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.see_also]

        super().__post_init__(**kwargs)


@dataclass
class NamedAlspacDataset(NamedThing):
    """
    Represents a named_alspac_data_set. That is a set of data that has been collected or produced to be named, reused
    and distributed.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Dataset
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "NamedAlspacDataset"
    class_model_uri: ClassVar[URIRef] = ALSPACDCS.NamedAlspacDataset

    id: Union[str, NamedAlspacDatasetId] = None
    landing_page_url: Optional[str] = None
    primary_investigator_orcids: Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]] = empty_dict()
    keywords: Optional[Union[str, List[str]]] = empty_list()
    has_current_version: Optional[Union[str, AlspacDataSetVersionId]] = None
    versions: Optional[Union[Dict[Union[str, AlspacDataSetVersionId], Union[dict, "AlspacDataSetVersion"]], List[Union[dict, "AlspacDataSetVersion"]]]] = empty_dict()
    primary_email: Optional[str] = None
    documentation_authors_orcids: Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]] = empty_dict()
    main_publication_doi: Optional[Union[str, PaperId]] = None
    publications_dois: Optional[Union[Dict[Union[str, PaperId], Union[dict, Paper]], List[Union[dict, Paper]]]] = empty_dict()
    in_catalog: Optional[Union[str, AlspacDataCatalogueId]] = None
    derived_from: Optional[Union[Dict[Union[str, NamedAlspacDatasetId], Union[dict, "NamedAlspacDataset"]], List[Union[dict, "NamedAlspacDataset"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedAlspacDatasetId):
            self.id = NamedAlspacDatasetId(self.id)

        if self.landing_page_url is not None and not isinstance(self.landing_page_url, str):
            self.landing_page_url = str(self.landing_page_url)

        self._normalize_inlined_as_list(slot_name="primary_investigator_orcids", slot_type=Person, key_name="id", keyed=True)

        if not isinstance(self.keywords, list):
            self.keywords = [self.keywords] if self.keywords is not None else []
        self.keywords = [v if isinstance(v, str) else str(v) for v in self.keywords]

        if self.has_current_version is not None and not isinstance(self.has_current_version, AlspacDataSetVersionId):
            self.has_current_version = AlspacDataSetVersionId(self.has_current_version)

        self._normalize_inlined_as_list(slot_name="versions", slot_type=AlspacDataSetVersion, key_name="id", keyed=True)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        self._normalize_inlined_as_list(slot_name="documentation_authors_orcids", slot_type=Person, key_name="id", keyed=True)

        if self.main_publication_doi is not None and not isinstance(self.main_publication_doi, PaperId):
            self.main_publication_doi = PaperId(self.main_publication_doi)

        self._normalize_inlined_as_list(slot_name="publications_dois", slot_type=Paper, key_name="id", keyed=True)

        if self.in_catalog is not None and not isinstance(self.in_catalog, AlspacDataCatalogueId):
            self.in_catalog = AlspacDataCatalogueId(self.in_catalog)

        self._normalize_inlined_as_list(slot_name="derived_from", slot_type=NamedAlspacDataset, key_name="id", keyed=True)

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
    class_name: ClassVar[str] = "AlspacDataSetVersion"
    class_model_uri: ClassVar[URIRef] = ALSPACDCS.AlspacDataSetVersion

    id: Union[str, AlspacDataSetVersionId] = None
    qc_description: Optional[str] = None
    qc_parts: Optional[Union[Dict[Union[str, QCKeyValueId], Union[dict, "QCKeyValue"]], List[Union[dict, "QCKeyValue"]]]] = empty_dict()
    ug_parts: Optional[Union[Dict[Union[str, UGKeyValueId], Union[dict, "UGKeyValue"]], List[Union[dict, "UGKeyValue"]]]] = empty_dict()
    version_of: Optional[Union[str, NamedAlspacDatasetId]] = None
    is_current_version: Optional[str] = None
    has_previous_version: Optional[Union[str, URIorCURIE]] = None
    has_next_version: Optional[Union[str, URIorCURIE]] = None
    authors: Optional[Union[str, List[str]]] = empty_list()
    has_parts: Optional[Union[Dict[Union[str, DatasetPartId], Union[dict, "DatasetPart"]], List[Union[dict, "DatasetPart"]]]] = empty_dict()
    known_issues: Optional[Union[Dict[Union[str, KnownIssueId], Union[dict, "KnownIssue"]], List[Union[dict, "KnownIssue"]]]] = empty_dict()
    has_scripts: Optional[Union[Dict[Union[str, ScriptId], Union[dict, "Script"]], List[Union[dict, "Script"]]]] = empty_dict()
    has_freezes: Optional[Union[Dict[Union[str, AlspacDataSetVersionFreezeId], Union[dict, "AlspacDataSetVersionFreeze"]], List[Union[dict, "AlspacDataSetVersionFreeze"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlspacDataSetVersionId):
            self.id = AlspacDataSetVersionId(self.id)

        if self.qc_description is not None and not isinstance(self.qc_description, str):
            self.qc_description = str(self.qc_description)

        self._normalize_inlined_as_list(slot_name="qc_parts", slot_type=QCKeyValue, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ug_parts", slot_type=UGKeyValue, key_name="id", keyed=True)

        if self.version_of is not None and not isinstance(self.version_of, NamedAlspacDatasetId):
            self.version_of = NamedAlspacDatasetId(self.version_of)

        if self.is_current_version is not None and not isinstance(self.is_current_version, str):
            self.is_current_version = str(self.is_current_version)

        if self.has_previous_version is not None and not isinstance(self.has_previous_version, URIorCURIE):
            self.has_previous_version = URIorCURIE(self.has_previous_version)

        if self.has_next_version is not None and not isinstance(self.has_next_version, URIorCURIE):
            self.has_next_version = URIorCURIE(self.has_next_version)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        self._normalize_inlined_as_list(slot_name="has_parts", slot_type=DatasetPart, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="known_issues", slot_type=KnownIssue, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_scripts", slot_type=Script, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="has_freezes", slot_type=AlspacDataSetVersionFreeze, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class Script(NamedThing):
    """
    A description and attributes of a script included in a version or freeze
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSPACDCS.Script
    class_class_curie: ClassVar[str] = "alspacdcs:Script"
    class_name: ClassVar[str] = "Script"
    class_model_uri: ClassVar[URIRef] = ALSPACDCS.Script

    id: Union[str, ScriptId] = None
    authors: Optional[Union[str, List[str]]] = empty_list()
    md5sum: Optional[str] = None
    filesize: Optional[str] = None
    filetype: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScriptId):
            self.id = ScriptId(self.id)

        if not isinstance(self.authors, list):
            self.authors = [self.authors] if self.authors is not None else []
        self.authors = [v if isinstance(v, str) else str(v) for v in self.authors]

        if self.md5sum is not None and not isinstance(self.md5sum, str):
            self.md5sum = str(self.md5sum)

        if self.filesize is not None and not isinstance(self.filesize, str):
            self.filesize = str(self.filesize)

        if self.filetype is not None and not isinstance(self.filetype, str):
            self.filetype = str(self.filetype)

        super().__post_init__(**kwargs)


@dataclass
class AlspacDataSetVersionFreeze(NamedThing):
    """
    Represents a freeze of a version of named_alspac_data_set. That is a specific set of data which can be applied to
    use by external colabs. It is normally a subset of files in a version of named alspac dataset, but sometimes file
    types will also change. For example .Rdata changed to .csv.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Dataset
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "AlspacDataSetVersionFreeze"
    class_model_uri: ClassVar[URIRef] = ALSPACDCS.AlspacDataSetVersionFreeze

    id: Union[str, AlspacDataSetVersionFreezeId] = None
    linker_file_md5sum: Optional[str] = None
    freeze_size: Optional[str] = None
    woc_file_md5sum: Optional[str] = None
    all_individuals_to_exclude_md5sum: Optional[str] = None
    is_current_freeze: Optional[Union[bool, Bool]] = None
    freeze_number: Optional[str] = None
    freeze_date: Optional[Union[str, XSDDate]] = None
    previous_freeze: Optional[Union[str, AlspacDataSetVersionFreezeId]] = None
    next_freeze: Optional[Union[str, AlspacDataSetVersionFreezeId]] = None
    freeze_of_alspac_dataset_version: Optional[Union[str, AlspacDataSetVersionId]] = None
    freeze_of_named_alspac_dataset: Optional[Union[str, NamedAlspacDatasetId]] = None
    primary_email: Optional[str] = None
    git_tag: Optional[str] = None
    has_parts: Optional[Union[Dict[Union[str, DatasetPartId], Union[dict, "DatasetPart"]], List[Union[dict, "DatasetPart"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AlspacDataSetVersionFreezeId):
            self.id = AlspacDataSetVersionFreezeId(self.id)

        if self.linker_file_md5sum is not None and not isinstance(self.linker_file_md5sum, str):
            self.linker_file_md5sum = str(self.linker_file_md5sum)

        if self.freeze_size is not None and not isinstance(self.freeze_size, str):
            self.freeze_size = str(self.freeze_size)

        if self.woc_file_md5sum is not None and not isinstance(self.woc_file_md5sum, str):
            self.woc_file_md5sum = str(self.woc_file_md5sum)

        if self.all_individuals_to_exclude_md5sum is not None and not isinstance(self.all_individuals_to_exclude_md5sum, str):
            self.all_individuals_to_exclude_md5sum = str(self.all_individuals_to_exclude_md5sum)

        if self.is_current_freeze is not None and not isinstance(self.is_current_freeze, Bool):
            self.is_current_freeze = Bool(self.is_current_freeze)

        if self.freeze_number is not None and not isinstance(self.freeze_number, str):
            self.freeze_number = str(self.freeze_number)

        if self.freeze_date is not None and not isinstance(self.freeze_date, XSDDate):
            self.freeze_date = XSDDate(self.freeze_date)

        if self.previous_freeze is not None and not isinstance(self.previous_freeze, AlspacDataSetVersionFreezeId):
            self.previous_freeze = AlspacDataSetVersionFreezeId(self.previous_freeze)

        if self.next_freeze is not None and not isinstance(self.next_freeze, AlspacDataSetVersionFreezeId):
            self.next_freeze = AlspacDataSetVersionFreezeId(self.next_freeze)

        if self.freeze_of_alspac_dataset_version is not None and not isinstance(self.freeze_of_alspac_dataset_version, AlspacDataSetVersionId):
            self.freeze_of_alspac_dataset_version = AlspacDataSetVersionId(self.freeze_of_alspac_dataset_version)

        if self.freeze_of_named_alspac_dataset is not None and not isinstance(self.freeze_of_named_alspac_dataset, NamedAlspacDatasetId):
            self.freeze_of_named_alspac_dataset = NamedAlspacDatasetId(self.freeze_of_named_alspac_dataset)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.git_tag is not None and not isinstance(self.git_tag, str):
            self.git_tag = str(self.git_tag)

        self._normalize_inlined_as_list(slot_name="has_parts", slot_type=DatasetPart, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class DatasetPart(NamedThing):
    """
    Represents a part of named alspac data set, in a version or freeze. For example in an omics context the data
    collected for a single chr which would be made availble as a dcat distribution of this type of dataset which would
    be of a specific file.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Dataset
    class_class_curie: ClassVar[str] = "dcat:Dataset"
    class_name: ClassVar[str] = "DatasetPart"
    class_model_uri: ClassVar[URIRef] = ALSPACDCS.DatasetPart

    id: Union[str, DatasetPartId] = None
    data_distributions: Optional[Union[Dict[Union[str, DataDistributionId], Union[dict, "DataDistribution"]], List[Union[dict, "DataDistribution"]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DatasetPartId):
            self.id = DatasetPartId(self.id)

        self._normalize_inlined_as_list(slot_name="data_distributions", slot_type=DataDistribution, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass
class DataDistribution(NamedThing):
    """
    A dataset distribution has a location, file type and file size.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = DCAT.Distribution
    class_class_curie: ClassVar[str] = "dcat:Distribution"
    class_name: ClassVar[str] = "DataDistribution"
    class_model_uri: ClassVar[URIRef] = ALSPACDCS.DataDistribution

    id: Union[str, DataDistributionId] = None
    md5sum: Optional[str] = None
    filesize: Optional[str] = None
    filetype: Optional[str] = None
    number_of_participants: Optional[int] = None
    number_of_gene_expression_probe_values: Optional[int] = None
    number_of_variants: Optional[int] = None
    number_of_cpgs: Optional[int] = None
    required_files: Optional[Union[Dict[Union[str, DataDistributionId], Union[dict, "DataDistribution"]], List[Union[dict, "DataDistribution"]]]] = empty_dict()
    belongsToContainer: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataDistributionId):
            self.id = DataDistributionId(self.id)

        if self.md5sum is not None and not isinstance(self.md5sum, str):
            self.md5sum = str(self.md5sum)

        if self.filesize is not None and not isinstance(self.filesize, str):
            self.filesize = str(self.filesize)

        if self.filetype is not None and not isinstance(self.filetype, str):
            self.filetype = str(self.filetype)

        if self.number_of_participants is not None and not isinstance(self.number_of_participants, int):
            self.number_of_participants = int(self.number_of_participants)

        if self.number_of_gene_expression_probe_values is not None and not isinstance(self.number_of_gene_expression_probe_values, int):
            self.number_of_gene_expression_probe_values = int(self.number_of_gene_expression_probe_values)

        if self.number_of_variants is not None and not isinstance(self.number_of_variants, int):
            self.number_of_variants = int(self.number_of_variants)

        if self.number_of_cpgs is not None and not isinstance(self.number_of_cpgs, int):
            self.number_of_cpgs = int(self.number_of_cpgs)

        self._normalize_inlined_as_list(slot_name="required_files", slot_type=DataDistribution, key_name="id", keyed=True)

        if self.belongsToContainer is not None and not isinstance(self.belongsToContainer, str):
            self.belongsToContainer = str(self.belongsToContainer)

        super().__post_init__(**kwargs)


@dataclass
class KnownIssue(NamedThing):
    """
    Known issues for a dataset should have a description, when they are logged and by who
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSPACDCS.KnownIssue
    class_class_curie: ClassVar[str] = "alspacdcs:KnownIssue"
    class_name: ClassVar[str] = "KnownIssue"
    class_model_uri: ClassVar[URIRef] = ALSPACDCS.KnownIssue

    id: Union[str, KnownIssueId] = None
    issue_description: Optional[str] = None
    logged_by: Optional[str] = None
    logged_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, KnownIssueId):
            self.id = KnownIssueId(self.id)

        if self.issue_description is not None and not isinstance(self.issue_description, str):
            self.issue_description = str(self.issue_description)

        if self.logged_by is not None and not isinstance(self.logged_by, str):
            self.logged_by = str(self.logged_by)

        if self.logged_date is not None and not isinstance(self.logged_date, str):
            self.logged_date = str(self.logged_date)

        super().__post_init__(**kwargs)


@dataclass
class QCKeyValue(NamedThing):
    """
    A qc part with a key and a value.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSPACDCS.QCKeyValue
    class_class_curie: ClassVar[str] = "alspacdcs:QCKeyValue"
    class_name: ClassVar[str] = "QCKeyValue"
    class_model_uri: ClassVar[URIRef] = ALSPACDCS.QCKeyValue

    id: Union[str, QCKeyValueId] = None
    qc_key: Optional[str] = None
    qc_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, QCKeyValueId):
            self.id = QCKeyValueId(self.id)

        if self.qc_key is not None and not isinstance(self.qc_key, str):
            self.qc_key = str(self.qc_key)

        if self.qc_value is not None and not isinstance(self.qc_value, str):
            self.qc_value = str(self.qc_value)

        super().__post_init__(**kwargs)


@dataclass
class UGKeyValue(NamedThing):
    """
    A user guide entry.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = ALSPACDCS.UGKeyValue
    class_class_curie: ClassVar[str] = "alspacdcs:UGKeyValue"
    class_name: ClassVar[str] = "UGKeyValue"
    class_model_uri: ClassVar[URIRef] = ALSPACDCS.UGKeyValue

    id: Union[str, UGKeyValueId] = None
    ug_key: Optional[str] = None
    ug_value: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, UGKeyValueId):
            self.id = UGKeyValueId(self.id)

        if self.ug_key is not None and not isinstance(self.ug_key, str):
            self.ug_key = str(self.ug_key)

        if self.ug_value is not None and not isinstance(self.ug_value, str):
            self.ug_value = str(self.ug_value)

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=ALSPACDCS.id, domain=None, range=URIRef)

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=ALSPACDCS.name, domain=None, range=Optional[str])

slots.see_also = Slot(uri=ALSPACDCS.see_also, name="see_also", curie=ALSPACDCS.curie('see_also'),
                   model_uri=ALSPACDCS.see_also, domain=None, range=Optional[Union[Union[str, URIorCURIE], List[Union[str, URIorCURIE]]]])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=ALSPACDCS.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=ALSPACDCS.primary_email, domain=None, range=Optional[str])

slots.primary_investigator_orcids = Slot(uri=ALSPACDCS.primary_investigator_orcids, name="primary_investigator_orcids", curie=ALSPACDCS.curie('primary_investigator_orcids'),
                   model_uri=ALSPACDCS.primary_investigator_orcids, domain=None, range=Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]])

slots.documentation_authors_orcids = Slot(uri=ALSPACDCS.documentation_authors_orcids, name="documentation_authors_orcids", curie=ALSPACDCS.curie('documentation_authors_orcids'),
                   model_uri=ALSPACDCS.documentation_authors_orcids, domain=None, range=Optional[Union[Dict[Union[str, PersonId], Union[dict, Person]], List[Union[dict, Person]]]])

slots.named_alspac_datasets = Slot(uri=ALSPACDCS.named_alspac_datasets, name="named_alspac_datasets", curie=ALSPACDCS.curie('named_alspac_datasets'),
                   model_uri=ALSPACDCS.named_alspac_datasets, domain=None, range=Optional[Union[Dict[Union[str, NamedAlspacDatasetId], Union[dict, NamedAlspacDataset]], List[Union[dict, NamedAlspacDataset]]]])

slots.derived_from = Slot(uri=ALSPACDCS.derived_from, name="derived_from", curie=ALSPACDCS.curie('derived_from'),
                   model_uri=ALSPACDCS.derived_from, domain=None, range=Optional[Union[Dict[Union[str, NamedAlspacDatasetId], Union[dict, NamedAlspacDataset]], List[Union[dict, NamedAlspacDataset]]]])

slots.required_files = Slot(uri=ALSPACDCS.required_files, name="required_files", curie=ALSPACDCS.curie('required_files'),
                   model_uri=ALSPACDCS.required_files, domain=None, range=Optional[Union[Dict[Union[str, DataDistributionId], Union[dict, DataDistribution]], List[Union[dict, DataDistribution]]]])

slots.versions = Slot(uri=ALSPACDCS.versions, name="versions", curie=ALSPACDCS.curie('versions'),
                   model_uri=ALSPACDCS.versions, domain=None, range=Optional[Union[Dict[Union[str, AlspacDataSetVersionId], Union[dict, AlspacDataSetVersion]], List[Union[dict, AlspacDataSetVersion]]]])

slots.keywords = Slot(uri=ALSPACDCS.keywords, name="keywords", curie=ALSPACDCS.curie('keywords'),
                   model_uri=ALSPACDCS.keywords, domain=None, range=Optional[Union[str, List[str]]])

slots.in_catalog = Slot(uri=ALSPACDCS.in_catalog, name="in_catalog", curie=ALSPACDCS.curie('in_catalog'),
                   model_uri=ALSPACDCS.in_catalog, domain=None, range=Optional[Union[str, AlspacDataCatalogueId]])

slots.version_of = Slot(uri=ALSPACDCS.version_of, name="version_of", curie=ALSPACDCS.curie('version_of'),
                   model_uri=ALSPACDCS.version_of, domain=None, range=Optional[Union[str, NamedAlspacDatasetId]])

slots.has_current_version = Slot(uri=DCAT.hasCurrentVersion, name="has_current_version", curie=DCAT.curie('hasCurrentVersion'),
                   model_uri=ALSPACDCS.has_current_version, domain=None, range=Optional[Union[str, AlspacDataSetVersionId]])

slots.has_previous_version = Slot(uri=ALSPACDCS.has_previous_version, name="has_previous_version", curie=ALSPACDCS.curie('has_previous_version'),
                   model_uri=ALSPACDCS.has_previous_version, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.has_next_version = Slot(uri=ALSPACDCS.has_next_version, name="has_next_version", curie=ALSPACDCS.curie('has_next_version'),
                   model_uri=ALSPACDCS.has_next_version, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.is_current_version = Slot(uri=ALSPACDCS.is_current_version, name="is_current_version", curie=ALSPACDCS.curie('is_current_version'),
                   model_uri=ALSPACDCS.is_current_version, domain=None, range=Optional[str])

slots.has_parts = Slot(uri=ALSPACDCS.has_parts, name="has_parts", curie=ALSPACDCS.curie('has_parts'),
                   model_uri=ALSPACDCS.has_parts, domain=None, range=Optional[Union[Dict[Union[str, DatasetPartId], Union[dict, DatasetPart]], List[Union[dict, DatasetPart]]]])

slots.has_freezes = Slot(uri=ALSPACDCS.has_freezes, name="has_freezes", curie=ALSPACDCS.curie('has_freezes'),
                   model_uri=ALSPACDCS.has_freezes, domain=None, range=Optional[Union[Dict[Union[str, AlspacDataSetVersionFreezeId], Union[dict, AlspacDataSetVersionFreeze]], List[Union[dict, AlspacDataSetVersionFreeze]]]])

slots.has_scripts = Slot(uri=ALSPACDCS.has_scripts, name="has_scripts", curie=ALSPACDCS.curie('has_scripts'),
                   model_uri=ALSPACDCS.has_scripts, domain=None, range=Optional[Union[Dict[Union[str, ScriptId], Union[dict, Script]], List[Union[dict, Script]]]])

slots.freeze_number = Slot(uri=ALSPACDCS.freeze_number, name="freeze_number", curie=ALSPACDCS.curie('freeze_number'),
                   model_uri=ALSPACDCS.freeze_number, domain=None, range=Optional[str])

slots.freeze_date = Slot(uri=ALSPACDCS.freeze_date, name="freeze_date", curie=ALSPACDCS.curie('freeze_date'),
                   model_uri=ALSPACDCS.freeze_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.is_current_freeze = Slot(uri=ALSPACDCS.is_current_freeze, name="is_current_freeze", curie=ALSPACDCS.curie('is_current_freeze'),
                   model_uri=ALSPACDCS.is_current_freeze, domain=None, range=Optional[Union[bool, Bool]])

slots.previous_freeze = Slot(uri=ALSPACDCS.previous_freeze, name="previous_freeze", curie=ALSPACDCS.curie('previous_freeze'),
                   model_uri=ALSPACDCS.previous_freeze, domain=None, range=Optional[Union[str, AlspacDataSetVersionFreezeId]])

slots.next_freeze = Slot(uri=ALSPACDCS.next_freeze, name="next_freeze", curie=ALSPACDCS.curie('next_freeze'),
                   model_uri=ALSPACDCS.next_freeze, domain=None, range=Optional[Union[str, AlspacDataSetVersionFreezeId]])

slots.freeze_of_alspac_dataset_version = Slot(uri=ALSPACDCS.freeze_of_alspac_dataset_version, name="freeze_of_alspac_dataset_version", curie=ALSPACDCS.curie('freeze_of_alspac_dataset_version'),
                   model_uri=ALSPACDCS.freeze_of_alspac_dataset_version, domain=None, range=Optional[Union[str, AlspacDataSetVersionId]])

slots.freeze_of_named_alspac_dataset = Slot(uri=ALSPACDCS.freeze_of_named_alspac_dataset, name="freeze_of_named_alspac_dataset", curie=ALSPACDCS.curie('freeze_of_named_alspac_dataset'),
                   model_uri=ALSPACDCS.freeze_of_named_alspac_dataset, domain=None, range=Optional[Union[str, NamedAlspacDatasetId]])

slots.linker_file_md5sum = Slot(uri=ALSPACDCS.linker_file_md5sum, name="linker_file_md5sum", curie=ALSPACDCS.curie('linker_file_md5sum'),
                   model_uri=ALSPACDCS.linker_file_md5sum, domain=None, range=Optional[str])

slots.md5sum = Slot(uri=ALSPACDCS.md5sum, name="md5sum", curie=ALSPACDCS.curie('md5sum'),
                   model_uri=ALSPACDCS.md5sum, domain=None, range=Optional[str])

slots.filesize = Slot(uri=DCAT.byteSize, name="filesize", curie=DCAT.curie('byteSize'),
                   model_uri=ALSPACDCS.filesize, domain=None, range=Optional[str])

slots.filetype = Slot(uri=DCAT.mediaType, name="filetype", curie=DCAT.curie('mediaType'),
                   model_uri=ALSPACDCS.filetype, domain=None, range=Optional[str])

slots.number_of_participants = Slot(uri=ALSPACDCS.number_of_participants, name="number_of_participants", curie=ALSPACDCS.curie('number_of_participants'),
                   model_uri=ALSPACDCS.number_of_participants, domain=None, range=Optional[int])

slots.number_of_variants = Slot(uri=ALSPACDCS.number_of_variants, name="number_of_variants", curie=ALSPACDCS.curie('number_of_variants'),
                   model_uri=ALSPACDCS.number_of_variants, domain=None, range=Optional[int])

slots.number_of_cpgs = Slot(uri=ALSPACDCS.number_of_cpgs, name="number_of_cpgs", curie=ALSPACDCS.curie('number_of_cpgs'),
                   model_uri=ALSPACDCS.number_of_cpgs, domain=None, range=Optional[int])

slots.belongsToContainer = Slot(uri=ALSPACDCS.belongsToContainer, name="belongsToContainer", curie=ALSPACDCS.curie('belongsToContainer'),
                   model_uri=ALSPACDCS.belongsToContainer, domain=None, range=Optional[str])

slots.number_of_gene_expression_probe_values = Slot(uri=ALSPACDCS.number_of_gene_expression_probe_values, name="number_of_gene_expression_probe_values", curie=ALSPACDCS.curie('number_of_gene_expression_probe_values'),
                   model_uri=ALSPACDCS.number_of_gene_expression_probe_values, domain=None, range=Optional[int])

slots.main_publication_doi = Slot(uri=ALSPACDCS.main_publication_doi, name="main_publication_doi", curie=ALSPACDCS.curie('main_publication_doi'),
                   model_uri=ALSPACDCS.main_publication_doi, domain=None, range=Optional[Union[str, PaperId]])

slots.landing_page_url = Slot(uri=DCAT.landingPage, name="landing_page_url", curie=DCAT.curie('landingPage'),
                   model_uri=ALSPACDCS.landing_page_url, domain=None, range=Optional[str])

slots.woc_file_md5sum = Slot(uri=ALSPACDCS.woc_file_md5sum, name="woc_file_md5sum", curie=ALSPACDCS.curie('woc_file_md5sum'),
                   model_uri=ALSPACDCS.woc_file_md5sum, domain=None, range=Optional[str])

slots.all_individuals_to_exclude_md5sum = Slot(uri=ALSPACDCS.all_individuals_to_exclude_md5sum, name="all_individuals_to_exclude_md5sum", curie=ALSPACDCS.curie('all_individuals_to_exclude_md5sum'),
                   model_uri=ALSPACDCS.all_individuals_to_exclude_md5sum, domain=None, range=Optional[str])

slots.git_tag = Slot(uri=ALSPACDCS.git_tag, name="git_tag", curie=ALSPACDCS.curie('git_tag'),
                   model_uri=ALSPACDCS.git_tag, domain=None, range=Optional[str])

slots.qc_description = Slot(uri=ALSPACDCS.qc_description, name="qc_description", curie=ALSPACDCS.curie('qc_description'),
                   model_uri=ALSPACDCS.qc_description, domain=None, range=Optional[str])

slots.qc_parts = Slot(uri=ALSPACDCS.qc_parts, name="qc_parts", curie=ALSPACDCS.curie('qc_parts'),
                   model_uri=ALSPACDCS.qc_parts, domain=None, range=Optional[Union[Dict[Union[str, QCKeyValueId], Union[dict, QCKeyValue]], List[Union[dict, QCKeyValue]]]])

slots.qc_key = Slot(uri=ALSPACDCS.qc_key, name="qc_key", curie=ALSPACDCS.curie('qc_key'),
                   model_uri=ALSPACDCS.qc_key, domain=None, range=Optional[str])

slots.qc_value = Slot(uri=ALSPACDCS.qc_value, name="qc_value", curie=ALSPACDCS.curie('qc_value'),
                   model_uri=ALSPACDCS.qc_value, domain=None, range=Optional[str])

slots.ug_key = Slot(uri=ALSPACDCS.ug_key, name="ug_key", curie=ALSPACDCS.curie('ug_key'),
                   model_uri=ALSPACDCS.ug_key, domain=None, range=Optional[str])

slots.ug_value = Slot(uri=ALSPACDCS.ug_value, name="ug_value", curie=ALSPACDCS.curie('ug_value'),
                   model_uri=ALSPACDCS.ug_value, domain=None, range=Optional[str])

slots.ug_parts = Slot(uri=ALSPACDCS.ug_parts, name="ug_parts", curie=ALSPACDCS.curie('ug_parts'),
                   model_uri=ALSPACDCS.ug_parts, domain=None, range=Optional[Union[Dict[Union[str, UGKeyValueId], Union[dict, UGKeyValue]], List[Union[dict, UGKeyValue]]]])

slots.publications_dois = Slot(uri=ALSPACDCS.publications_dois, name="publications_dois", curie=ALSPACDCS.curie('publications_dois'),
                   model_uri=ALSPACDCS.publications_dois, domain=None, range=Optional[Union[Dict[Union[str, PaperId], Union[dict, Paper]], List[Union[dict, Paper]]]])

slots.data_distributions = Slot(uri=ALSPACDCS.data_distributions, name="data_distributions", curie=ALSPACDCS.curie('data_distributions'),
                   model_uri=ALSPACDCS.data_distributions, domain=None, range=Optional[Union[Dict[Union[str, DataDistributionId], Union[dict, DataDistribution]], List[Union[dict, DataDistribution]]]])

slots.authors = Slot(uri=ALSPACDCS.authors, name="authors", curie=ALSPACDCS.curie('authors'),
                   model_uri=ALSPACDCS.authors, domain=None, range=Optional[Union[str, List[str]]])

slots.known_issues = Slot(uri=ALSPACDCS.known_issues, name="known_issues", curie=ALSPACDCS.curie('known_issues'),
                   model_uri=ALSPACDCS.known_issues, domain=None, range=Optional[Union[Dict[Union[str, KnownIssueId], Union[dict, KnownIssue]], List[Union[dict, KnownIssue]]]])

slots.logged_by = Slot(uri=ALSPACDCS.logged_by, name="logged_by", curie=ALSPACDCS.curie('logged_by'),
                   model_uri=ALSPACDCS.logged_by, domain=None, range=Optional[str])

slots.logged_date = Slot(uri=ALSPACDCS.logged_date, name="logged_date", curie=ALSPACDCS.curie('logged_date'),
                   model_uri=ALSPACDCS.logged_date, domain=None, range=Optional[str])

slots.issue_description = Slot(uri=ALSPACDCS.issue_description, name="issue_description", curie=ALSPACDCS.curie('issue_description'),
                   model_uri=ALSPACDCS.issue_description, domain=None, range=Optional[str])

slots.freeze_size = Slot(uri=ALSPACDCS.freeze_size, name="freeze_size", curie=ALSPACDCS.curie('freeze_size'),
                   model_uri=ALSPACDCS.freeze_size, domain=None, range=Optional[str])