class APT(object):
    COUNTER = 0

    def __init__(self, name, description='', country='',
                 mitre_id=''):
        self.id = self.COUNTER
        self.__class__.COUNTER += 1
        self.name = name
        self.description = description
        self.country = country
        self.mitre_id = mitre_id

    def get_details(self, relation=False):
        details = dict(self.__dict__)
        if not relation:
            return details

        techniques = TechniqueAPTMap.get_techniques_for_apt(self.id)
        technique_details = [technique.get_details(relation=False)
                             for technique in techniques]
        details['techniques'] = technique_details

        return details


class Tactic(object):
    COUNTER = 0

    def __init__(self, name, description='', phase='', url='', domain='',
                 slug=''):

        self.id = self.COUNTER
        self.__class__.COUNTER += 1
        self.name = name
        self.description = description
        self.phase = phase
        self.url = url
        self.domain = domain
        self.slug = slug

    def get_details(self, relation=False):
        details = dict(self.__dict__)
        if not relation:
            return details

        techniques = TacticTechniqueMap.get_techniques_for_tactic(self.id)
        technique_details = [technique.get_details(relation=False)
                             for technique in techniques]
        details['techniques'] = technique_details

        return details



class Technique(object):
    COUNTER = 0

    def __init__(self, name, description='', references=None, mitre_technique_id='',
                 tactic_slugs=None):
        if references is None:
            references = []
        if tactic_slugs is None:
            tactic_slugs = []
        self.id = self.COUNTER
        self.__class__.COUNTER += 1
        self.name = name
        self.description = description
        self.references = references
        self.mitre_technique_id = mitre_technique_id
        self.tactic_slugs = tactic_slugs

    def get_details(self, relation=False):
        details = dict(self.__dict__)
        if not relation:
            return details
        tactics = TacticTechniqueMap.get_tactics_for_technique(self.id)
        tactics_details = [tactic.get_details(relation=False)
                           for tactic in tactics]
        details['tactics'] = tactics_details

        return details


class TacticTechniqueMap(object):
    tactics_to_techniques_map = {}
    techniques_to_tactics_map = {}

    @classmethod
    def add_mapping(cls, tactic, technique):
        cls.tactics_to_techniques_map.setdefault(tactic.id, [])
        cls.tactics_to_techniques_map[tactic.id].append(technique)

        cls.techniques_to_tactics_map.setdefault(technique.id, [])
        cls.techniques_to_tactics_map[technique.id].append(tactic)

    @classmethod
    def get_tactics_for_technique(cls, technique_id):
        return cls.techniques_to_tactics_map.get(technique_id, [])

    @classmethod
    def get_techniques_for_tactic(cls, tactic_id):
        return cls.tactics_to_techniques_map.get(tactic_id, [])


class TechniqueAPTMap(object):
    apts_to_techniques_map = {}
    techniques_to_apts_map = {}

    @classmethod
    def add_mapping(cls, apt, technique):
        cls.apts_to_techniques_map.setdefault(apt.id, [])
        cls.apts_to_techniques_map[apt.id].append(technique)

        cls.techniques_to_apts_map.setdefault(technique.id, [])
        cls.techniques_to_apts_map[technique.id].append(apt)


    @classmethod
    def get_apts_for_technique(cls, technique_id):
        return cls.techniques_to_apts_map.get(technique_id, [])

    @classmethod
    def get_techniques_for_apt(cls, apt_id):
        return cls.apts_to_techniques_map.get(apt_id, [])



