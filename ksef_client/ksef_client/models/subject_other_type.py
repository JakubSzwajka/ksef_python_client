from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.subject_identifier_to_type import SubjectIdentifierToType
from ..models.subject_name_type import SubjectNameType
from ..models.subject_other_type_subject_other_type import SubjectOtherTypeSubjectOtherType
from ..types import UNSET, Unset

T = TypeVar("T", bound="SubjectOtherType")


@attr.s(auto_attribs=True)
class SubjectOtherType:
    """
    Attributes:
        issued_to_identifier (SubjectIdentifierToType):
        subject_other_type (SubjectOtherTypeSubjectOtherType):
        issued_to_name (Union[Unset, SubjectNameType]):
    """

    issued_to_identifier: SubjectIdentifierToType
    subject_other_type: SubjectOtherTypeSubjectOtherType
    issued_to_name: Union[Unset, SubjectNameType] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        issued_to_identifier = self.issued_to_identifier.to_dict()

        subject_other_type = self.subject_other_type.value

        issued_to_name: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.issued_to_name, Unset):
            issued_to_name = self.issued_to_name.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "issuedToIdentifier": issued_to_identifier,
                "subjectOtherType": subject_other_type,
            }
        )
        if issued_to_name is not UNSET:
            field_dict["issuedToName"] = issued_to_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        issued_to_identifier = SubjectIdentifierToType.from_dict(d.pop("issuedToIdentifier"))

        subject_other_type = SubjectOtherTypeSubjectOtherType(d.pop("subjectOtherType"))

        _issued_to_name = d.pop("issuedToName", UNSET)
        issued_to_name: Union[Unset, SubjectNameType]
        if isinstance(_issued_to_name, Unset):
            issued_to_name = UNSET
        else:
            issued_to_name = SubjectNameType.from_dict(_issued_to_name)

        subject_other_type = cls(
            issued_to_identifier=issued_to_identifier,
            subject_other_type=subject_other_type,
            issued_to_name=issued_to_name,
        )

        subject_other_type.additional_properties = d
        return subject_other_type

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
