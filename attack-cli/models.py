class APT(object):
    COUNTER = 0

    def __init__(self, name, description='', country=''):
        self.id = self.COUNTER
        self.__class__.COUNTER += 1
        self.name = name
        self.description = description
        self.country = country

    def get_details(self):
        return self.__dict__


class Tactic(object):
    COUNTER = 0

    def __init__(self, name, description='', phase='', url='', domain=''):

        self.id = self.COUNTER
        self.__class__.COUNTER += 1
        self.name = name
        self.description = description
        self.phase = phase
        self.url = url
        self.domain = domain

    def get_details(self):
        return self.__dict__


class Technique(object):
    COUNTER = 0

    def __init__(self, name, description='', references=None, mitre_technique_id=''):
        if references is None:
            references = []

        self.id = self.COUNTER
        self.__class__.COUNTER += 1
        self.name = name
        self.description = description
        self.references = references
        self.mitre_technique_id = mitre_technique_id

    def get_details(self):
        return self.__dict__


class TacticTechniqueMap(object):
    def __init__(self):
        self.tactics_to_techniques_map = {}
        self.techniques_to_tactics_map = {}

    def add_mapping(self, tactic, technique):
        self.tactics_to_techniques_map.setdefault(tactic.id, [])
        self.tactics_to_techniques_map[tactic.id].append(technique)

        self.techniques_to_tactics_map.setdefault(technique.id, [])
        self.tactics_to_techniques_map[technique.id].append(tactic)





