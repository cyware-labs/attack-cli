from models import Tactic, Technique, APT, TacticTechniqueMap, TechniqueAPTMap
from setup import SetupAPTGroups, SetupTactic, SetupTechniques


class AttackNavigator(object):
    def __init__(self):
        self.apts = {}
        self.tactics = {}
        self.techniques = {}


    def initialize(self):
        self._fetch_data()

    def get_tactics(self, query=None):
        if query is None:
            return [tactic.get_details(relation=True) for tactic in self.tactics.values()]

        result = self._search(self.tactics, ['name'], query)
        return result


    def _get_details(self, param_dict, key, raise_exception=False):
        instance = param_dict.get(key)
        if not instance:
            if raise_exception:
                raise Exception("Instance not found")
            else:
                return None

        return instance.get_details(relation=True)

    def _search(self, param_dict, search_keys, search_value):
        result = set()
        for id, value in param_dict.items():
            for search_key in search_keys:
                if search_value in getattr(value, search_key, None):
                    result.add(value)

        return [value.get_details(relation=True) for value in result]

    def get_tactic(self, id_param, raise_exception=False):
        return self._get_details(self.tactics, id_param, raise_exception)

    def get_techniques(self, query=None):
        if query is None:
            return [technique.get_details(relation=True)
                    for technique in self.techniques.values()]

        result = self._search(self.techniques, ['name'], query)
        return result

    def get_technique(self, id_param, raise_exception=False):
        return self._get_details(self.techniques, id_param, raise_exception)

    def get_apts(self, query=None):
        if query is None:
            return [apt.get_details(relation=True) for apt in self.apts.values()]

        result = self._search(self.apts, ['name'], query)
        return result

    def get_apt(self, id_param, raise_exception=False):
        return self._get_details(self.apts, id_param, raise_exception)

    def _fetch_data(self):
        # a1 = Tactic('Tactic 1')
        # self.tactics[a1.id] = a1
        #
        # a2 = Tactic('Tactic 2')
        # self.tactics[a2.id] = a2
        #
        # a3 = Tactic('Tactic 3')
        # self.tactics[a3.id] = a3
        #
        #
        # b1 = Technique('Technique 1')
        # self.techniques[b1.id] = b1
        #
        # b2 = Technique('Technique 2')
        # self.techniques[b2.id] = b2
        #
        # b3 = Technique('Technique 3')
        # self.techniques[b3.id] = b3
        #
        # e = TacticTechniqueMap
        # e.add_mapping(a1, b1)
        # e.add_mapping(a1, b2)
        # e.add_mapping(a2, b2)
        # e.add_mapping(a3, b3)
        #
        # c1 = APT('APT 1')
        # self.apts[c1.id] = c1
        #
        # c2 = APT('APT 2')
        # self.apts[c2.id] = c2
        #
        #
        # c3 = APT('APT 3')
        # self.apts[c3.id] = c3
        #
        # f = TechniqueAPTMap
        # f.add_mapping(c1, b1)
        # f.add_mapping(c1, b2)
        # f.add_mapping(c1, b3)
        # f.add_mapping(c3, b3)
        # f.add_mapping(c2, b2)
        tactic_technique_map_obj = TacticTechniqueMap
        tactics = SetupTactic().do_setup()
        for tactic in tactics:
            self.tactics[tactic.id] = tactic
        techniques = SetupTechniques().do_setup()
        for technique in techniques:
            self.techniques[technique.id] = technique

        technique_to_tactic_map = {}
        for technique in techniques:
            technique_tactics = []
            tactic_slugs = technique.tactic_slugs
            tactics = self.tactics.values()
            for tactic in tactics:
                if tactic.slug in tactic_slugs:
                    tactic_technique_map_obj.add_mapping(tactic, technique)

        apt_groups = SetupAPTGroups().do_setup()
        for apt in apt_groups:
            self.apts[apt.id] = apt
        # c = APT('test apt')
        # self.apts[c.id] = c
