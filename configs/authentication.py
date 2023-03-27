from django.core.exceptions import ImproperlyConfigured


class LDAPBackend:

    def __new__(cls, *args, **kwargs):
        try:
            from django_auth_ldap.backend import LDAPSettings, LDAPBackend
            import ldap
        except ModuleNotFoundError as e:
            if getattr(e, 'name') == 'django_auth_ldap':
                raise ImproperlyConfigured(
                    "LDAP authentication has been configured, but django-auth-ldap is not installed."
                )
            raise e

        try:
            from . import ldap_config
        except ModuleNotFoundError as e:
            if getattr(e, 'name') == 'ldap_config':
                raise ImproperlyConfigured(
                    "LDAP configuration file not found: Check that ldap_config.py has been created alongside "
                    "configuration.py."
                )
            raise e

        try:
            getattr(ldap_config, 'AUTH_LDAP_SERVER_URI')
        except AttributeError:
            raise ImproperlyConfigured(
                "Required parameter AUTH_LDAP_SERVER_URI is missing from ldap_config.py."
            )

        obj = LDAPBackend()

        # Read LDAP configuration parameters from ldap_config.py instead of settings.py
        settings = LDAPSettings()
        for param in dir(ldap_config):
            if param.startswith(settings._prefix):
                setattr(settings, param[10:], getattr(ldap_config, param))
        obj.settings = settings

        # Optionally disable strict certificate checking
        if getattr(ldap_config, 'LDAP_IGNORE_CERT_ERRORS', False):
            ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)

        return obj


