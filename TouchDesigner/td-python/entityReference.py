from dataclasses import dataclass


@dataclass
class entityReference:
    '''Entity reference helper object for ensuring parameter's updates are routed correctly
    '''
    par_path: str
    par_label: str
    par_name: str

    @property
    def to_dict(self) -> dict[str, str]:
        '''Converts entity reference into a dictionary
        '''
        return {
            'parPath': self.par_path,
            'parLabel': self.par_label,
            'parName': self.par_name
        }

    @staticmethod
    def from_dict(dict):
        '''Constructs entity reference from dictionary
        '''
        required_keys = ['parPath', 'parLabel', 'parName']
        if required_keys not in dict.keys():
            raise TypeError("dict does not contain required keys")

        return entityReference(
            par_path=dict.get('parPath'),
            par_label=dict.get('parLabel'),
            par_name=dict.get('parName'))

    @staticmethod
    def from_parGroup(parGroup):
        '''Constructs entity reference from parGroup
        '''
        return entityReference(
            par_path=parGroup.owner.path,
            par_label=parGroup.label,
            par_name=parGroup.name)
