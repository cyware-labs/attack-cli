import json

from .models import Technique, Tactic, APT
from attack_cli import enterprise_attack


class SetupTactic(object):
    def __init__(self):
        pass

    def _get_file_path(self):
        return 'attack_cli/tactic_data.json'

    def do_setup(self):
        content_dict = self._get_tactic_content()
        enterprise_tactics = content_dict['enterprise_tactics']['tactics']
        tactics = []
        for tactic in enterprise_tactics:
            slug = tactic['tactic']
            title = self._get_title(slug)
            data = {
                'slug': slug,
                'name': title,
                'description': tactic['description'],
                'phase': tactic['phase'],
                'url': tactic['url'],
                'domain': 'ENTERPRISE',
            }
            tactic = Tactic(**data)
            tactics.append(tactic)
        return tactics

    def _get_tactic_content(self):
        file_path = self._get_file_path()
        content = open(file_path, 'r')
        content_dict = json.loads(content.read())
        return content_dict

    @staticmethod
    def _get_title(slug):
        title = ' '.join([i.title() for i in slug.split('-')])
        return title


class SetupTechniques(object):
    def __init__(self):
        pass

    def do_setup(self):
        techniques = enterprise_attack.enterprise['objects']
        technique_list = []
        for technique in techniques:
            title = technique.get('name')
            if not title or technique['type'] != 'attack-pattern':
                continue
            tactic_slugs = [phase['phase_name']
                                for phase in technique.get('kill_chain_phases', [])]
            data = {
                'name': technique['name'],
                'description': technique.get('description', ''),
                'mitre_technique_id': technique['id'],
                'type': technique['type'],
                'external_references': technique['external_references'],
                'tactic_slugs': tactic_slugs,
            }
            technique = Technique(**data)
            technique_list.append(technique)
        return technique_list


class SetupAPTGroups(object):
    def __init__(self):
        pass

    def do_setup(self):
        apt_list = []
        enterprise_objects = enterprise_attack.enterprise['objects']
        for enterprise_object in enterprise_objects:
            if enterprise_object['type'] != 'intrusion-set' or enterprise_object.get(
                    'revoked'):
                continue

            data = {
                'name': enterprise_object['name'],
                'description': enterprise_object.get('description', ''),
                'mitre_id': enterprise_object['id'],
            }
            apt_group = APT(**data)
            apt_list.append(apt_group)
        return apt_list

