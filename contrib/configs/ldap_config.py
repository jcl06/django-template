import ldap
from django_auth_ldap.config import LDAPSearch, GroupOfNamesType, NestedGroupOfNamesType, LDAPGroupQuery
from django.conf import settings

# Server URI
if settings.LDAP_ADDRESS:
    AUTH_LDAP_SERVER_URI = settings.LDAP_ADDRESS

    # Set the DN and password for the NetBox service account.
    AUTH_LDAP_BIND_DN = settings.LDAP_USER
    AUTH_LDAP_BIND_PASSWORD = settings.LDAP_PASS

# The following may be needed if you are binding to Active Directory.
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_REFERRALS: 0
}

# Include this setting if you want to ignore certificate errors. This might be needed to accept a self-signed cert.
# ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
LDAP_IGNORE_CERT_ERRORS = True  # --> to be defined on setting later as a function

# This search matches users with the sAMAccountName equal to the provided username. This is required if the user's
# username is not in their DN (Active Directory).
AUTH_LDAP_USER_SEARCH = LDAPSearch("DC=abc,DC=domain,DC=com",
                                   ldap.SCOPE_SUBTREE,
                                   "(sAMAccountName=%(user)s)")

# You can map user attributes to Django attributes as so.
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
    "full_name": "displayName"
}

# This search ought to return all groups to which the user belongs. django_auth_ldap uses this to determine group
# hierarchy.
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("DC=abc,DC=domain,DC=com", ldap.SCOPE_SUBTREE,
                                    "(objectClass=group)")
AUTH_LDAP_GROUP_TYPE = NestedGroupOfNamesType()
# AUTH_LDAP_GROUP_TYPE = GroupOfNamesType()
# Define a group required to login.
AUTH_LDAP_REQUIRE_GROUP = settings.AUTH_LDAP_REQUIRE_GROUP

# Mirror LDAP group assignments.
# List the groups that will add and map to Django groups
if settings.AUTH_LDAP_MIRROR_GROUPS:
    AUTH_LDAP_MIRROR_GROUPS = settings.AUTH_LDAP_MIRROR_GROUPS

# Define special user types using groups. Exercise great caution when assigning superuser status.
if settings.AUTH_LDAP_USER_FLAGS_BY_GROUP:
    AUTH_LDAP_USER_FLAGS_BY_GROUP = settings.AUTH_LDAP_USER_FLAGS_BY_GROUP

'''
from django_auth_ldap.config import LDAPGroupQuery
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_active": "cn=active,ou=groups,dc=example,dc=com",
    "is_staff": (
        LDAPGroupQuery("cn=staff,ou=groups,dc=example,dc=com")
        | LDAPGroupQuery("cn=admin,ou=groups,dc=example,dc=com")
    ),
    "is_superuser": "cn=superuser,ou=groups,dc=example,dc=com",
}'''

# For more granular permissions, we can map LDAP groups to Django groups.
AUTH_LDAP_FIND_GROUP_PERMS = True
# Cache groups for one hour to reduce LDAP traffic
AUTH_LDAP_CACHE_TIMEOUT = 3600

