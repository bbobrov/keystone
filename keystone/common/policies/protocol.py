# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from oslo_policy import policy

from keystone.common.policies import base

protocol_policies = [
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'create_protocol',
        check_str=base.RULE_ADMIN_REQUIRED,
        # FIXME(lbragstad): Once it is possible to add complete federated
        # identity without having to modify system configuration files, like
        # Apache, this should include 'project' in scope_types.
        scope_types=['system'],
        description='Create federated protocol.',
        operations=[{'path': ('/v3/OS-FEDERATION/identity_providers/{idp_id}/'
                              'protocols/{protocol_id}'),
                     'method': 'PUT'}]),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'update_protocol',
        check_str=base.RULE_ADMIN_REQUIRED,
        scope_types=['system'],
        description='Update federated protocol.',
        operations=[{'path': ('/v3/OS-FEDERATION/identity_providers/{idp_id}/'
                              'protocols/{protocol_id}'),
                     'method': 'PATCH'}]),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'get_protocol',
        check_str=base.RULE_ADMIN_REQUIRED,
        scope_types=['system'],
        description='Get federated protocol.',
        operations=[{'path': ('/v3/OS-FEDERATION/identity_providers/{idp_id}/'
                              'protocols/{protocol_id}'),
                     'method': 'GET'}]),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'list_protocols',
        check_str=base.RULE_ADMIN_REQUIRED,
        scope_types=['system'],
        description='List federated protocols.',
        operations=[{'path': ('/v3/OS-FEDERATION/identity_providers/{idp_id}/'
                              'protocols'),
                     'method': 'GET'}]),
    policy.DocumentedRuleDefault(
        name=base.IDENTITY % 'delete_protocol',
        check_str=base.RULE_ADMIN_REQUIRED,
        scope_types=['system'],
        description='Delete federated protocol.',
        operations=[{'path': ('/v3/OS-FEDERATION/identity_providers/{idp_id}/'
                              'protocols/{protocol_id}'),
                     'method': 'DELETE'}])
]


def list_rules():
    return protocol_policies