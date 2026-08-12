"""Core functionality for Meta Ads API MCP package."""

from .server import mcp_server
from .accounts import get_ad_accounts, get_account_info
from .campaigns import get_campaigns, get_campaign_details, create_campaign
from .adsets import get_adsets, get_adset_details, update_adset
from .ads import get_ads, get_ad_details, get_creative_details, get_ad_creatives, get_ad_image, update_ad
from .insights import get_insights
from . import authentication  # Import module to register conditional auth tools
from .server import login_cli, main
from .auth import login
from . import ads_library  # Import module to register conditional tools
from .budget_schedules import create_budget_schedule
from .targeting import search_interests, get_interest_suggestions, estimate_audience_size, search_behaviors, search_demographics, search_geo_locations
from . import reports  # Import module to register conditional tools
from . import duplication  # Import module to register conditional duplication tools
from .openai_deep_research import search, fetch  # OpenAI MCP Deep Research tools
from . import audiences  # Import module to register custom audience tools
from . import lookalikes  # Import module to register lookalike audience tools
from . import conversions  # Import module to register CAPI / custom conversion tools
from . import insights_advanced  # Import module to register advanced insights tools
from . import rules  # Import module to register automated rule tools
from . import pixels  # Import module to register pixel tools
from . import ab_testing  # Import module to register A/B testing tools
from . import catalogs  # Import module to register product catalog tools
from . import lead_forms  # Import module to register lead form tools
from . import reach_frequency  # Import module to register reach & frequency tools
from . import business  # Import module to register Business Manager tools
from . import page_posts  # Import module to register page post tools
from . import offline_conversions  # Import module to register offline conversion tools
from . import creatives_advanced  # Import module to register advanced creative tools
from . import saved_audiences  # Import module to register saved audience tools
from . import attribution  # Import module to register attribution tools

__all__ = [
    'mcp_server',
    'get_ad_accounts',
    'get_account_info',
    'get_campaigns',
    'get_campaign_details',
    'create_campaign',
    'get_adsets',
    'get_adset_details',
    'update_adset',
    'get_ads',
    'get_ad_details',
    'get_creative_details',
    'get_ad_creatives',
    'get_ad_image',
    'update_ad',
    'get_insights',
    # Note: 'get_login_link' is registered conditionally by the authentication module
    'login_cli',
    'login',
    'main',
    'create_budget_schedule',
    'search_interests',
    'get_interest_suggestions',
    'estimate_audience_size',
    'search_behaviors',
    'search_demographics',
    'search_geo_locations',
    'search',  # OpenAI MCP Deep Research search tool
    'fetch',   # OpenAI MCP Deep Research fetch tool
] 