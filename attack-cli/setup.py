import json

from models import Technique, Tactic, APT
from enterprise_attack import enterprise


class SetupTactic(object):
    def __init__(self):
        pass

    def _get_file_path(self):
        return 'tactic_data.json'

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
        techniques = enterprise['objects']
        technique_list = []
        for technique in techniques:
            title = technique.get('name')
            if not title or technique['type'] != 'attack-pattern':
                print(technique['id'], technique['type'])
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

            # tactics_list = [phase['phase_name']
            #                 for phase in technique.get('kill_chain_phases', [])]
            # tactics = AttackTactic.objects.filter(slug__in=tactics_list)
            # technique_obj.tactics.add(*tactics)
            #
            # log_source_list = technique.get('x_mitre_data_sources', [])
            # for log_source in log_source_list:
            #     source_obj, _ = LogSource.objects.get_or_create(title=log_source,
            #                                                  tenant=self.tenant)
            #     source_obj.attack_techniques.add(technique_obj)
            #
            # defense_bypassed_list = technique.get('x_mitre_defense_bypassed', [])
            # for defense_bypassed in defense_bypassed_list:
            #     defense_bypassed_obj, _ = DefenseBypassed.objects.get_or_create(
            #         title=defense_bypassed, tenant=self.tenant)
            #     defense_bypassed_obj.attack_techniques.add(technique_obj)
            #
            # print('Done')
            # # print('Created/Updated Technique {0}. Created? {1}'.format(
            # #     technique['id'],created))


class SetupAPTGroups(object):
    def __init__(self):
        pass

    def do_setup(self):
        apt_list = []
        enterprise_objects = enterprise['objects']
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


class SetupAPTGroupTechniqueMap(object):
    def __init__(self):
        tenant = global_context_manager.get_context('tenant')
        self.tenant = tenant

    def do_setup(self):
        enterprise_objects = enterprise['objects']
        for enterprise_object in enterprise_objects:
            if (enterprise_object['type'] == 'relationship'
                and enterprise_object['source_ref'].startswith('intrusion-set')
                and enterprise_object['target_ref'].startswith('attack-pattern')):

                technique = AttackTechnique.objects.get(
                    mitre_technique_id=enterprise_object['target_ref'])
                apt_group = APTGroup.objects.get(
                    mitre_id=enterprise_object['source_ref'])
                apt_group.attack_techniques.add(technique)
                print('Added {0} to APT {1}'.format(technique.title, apt_group.title))


# class SetupSoftware(object):
#     def __init__(self):
#         tenant = global_context_manager.get_context('tenant')
#         self.tenant = tenant
#
#     def do_setup(self):
#         enterprise_objects = enterprise['objects']
#         for enterprise_object in enterprise_objects:
#             if enterprise_object['type'] == 'malware':
#                 data = {
#                     'title': enterprise_object['name'],
#                     'description': enterprise_object['description'],
#                     'external_references': enterprise_object['external_references'],
#                     'mitre_id': enterprise_object['id'],
#                     'tenant': self.tenant,
#                 }
#                 instance, created = Software.objects.update_or_create(
#                     mitre_id=enterprise_object['id'], defaults=data)
#                 print('Created/Updated {0}. Created? {1}'.format(
#                     enterprise_object['name'], created))
#
#
# class SetupSoftwareTechniqueMap(object):
#     def __init__(self):
#         tenant = global_context_manager.get_context('tenant')
#         self.tenant = tenant
#
#     def do_setup(self):
#         enterprise_objects = enterprise['objects']
#         for enterprise_object in enterprise_objects:
#             if (enterprise_object['type'] == 'relationship'
#                     and enterprise_object['source_ref'].startswith('malware')
#                     and enterprise_object['target_ref'].startswith('attack-pattern')):
#
#                 software = Software.objects.get(mitre_id=enterprise_object['source_ref'])
#                 technique = AttackTechnique.objects.get(
#                     mitre_technique_id=enterprise_object['target_ref'])
#                 software.attack_techniques.add(technique)
#                 print('Added {0} to Software {1}'.format(technique.title, software.title))
