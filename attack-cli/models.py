class APT(object):
    COUNTER = 0

    def __init__(self, name, description='', country=''):
        self.id = self.COUNTER
        self.COUNTER += 1
        self.name = name
        self.description = description
        self.country = country


class Tactic(object):
    COUNTER = 0

    def __init__(self, name):
        self.id = self.COUNTER
        self.COUNTER += 1
        self.name = name

    def get_details(self):
        return {
            'name': self.name
        }


class Technique(object):
    COUNTER = 0

    def __init__(self, name):
        self.id = self.COUNTER
        self.COUNTER += 1
        self.name = name


class TacticTechniqueMap(object):
    def __init__(self):
        self.tactics_to_techniques_map = {}
        self.techniques_to_tactics_map = {}

    def add_mapping(self, tactic, technique):
        self.tactics_to_techniques_map.setdefault(tactic.id, [])
        self.tactics_to_techniques_map[tactic.id].append(technique)

        self.techniques_to_tactics_map.setdefault(technique.id, [])
        self.tactics_to_techniques_map[technique.id].append(tactic)


class AttackNavigator(object):
    def __init__(self):
        self.apts = {}
        self.tactics = {}
        self.techniques = []
        self.tactic_technique_map = None
        self.apt_technique_map = None

    def initialize(self):
        self._fetch_data()

    def get_tactics(self, search_param=None):
        if search_param is None:
            return [tactic.get_details() for tactic in self.tactics.values()]

    def get_tactic(self, id_param):
        pass

    def get_techniques(self, search_param=None):
        pass

    def get_technique(self, technique_id):
        pass

    def _fetch_data(self):
        a = Tactic('test tactics')
        self.tactics[a.id] = a



