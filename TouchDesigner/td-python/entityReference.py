from dataclasses import dataclass


@dataclass
class entityReference:
    par_path: str
    par_label: str

    @property
    def to_dict(self) -> dict[str, str]:
        return {
            'parPath': self.par_path,
            'parLabel': self.par_label
        }

    @staticmethod
    def from_dict(dict):
        required_keys = ['parPath', 'parLabel']
        if required_keys not in dict.keys():
            raise TypeError("dict does not contain required keys")

        return entityReference(
            par_path=dict.get('parPath'),
            par_label=dict.get('parLabel'))

    @staticmethod
    def from_parGroup(parGroup):
        return entityReference(
            par_path=parGroup.owner.path,
            par_label=parGroup.label)
