default_app_config = "kave.contrib.django.apps.KaveDjangoConfig"

from kave.contrib.django.tenant import UserAgentContext, UserAgentManager, agent_name_for_user

__all__ = ["UserAgentContext", "UserAgentManager", "agent_name_for_user"]
