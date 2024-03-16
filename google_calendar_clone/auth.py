import os

from supertokens_python import InputAppInfo, SupertokensConfig, init
from supertokens_python.recipe import session, thirdparty
from supertokens_python.recipe.thirdparty.provider import (
    ProviderClientConfig,
    ProviderConfig,
    ProviderInput,
)


def init_auth() -> None:
    init(
        app_info=InputAppInfo(
            app_name="Google Calendar Clone",
            api_domain=os.environ.get("API_URL"),
            website_domain=os.environ.get("FRONTEND_URL"),
            api_base_path="/api/auth",
            website_base_path="/auth",
        ),
        supertokens_config=SupertokensConfig(
            connection_uri=os.environ.get("AUTH_URL"),
        ),
        framework="django",
        recipe_list=[
            session.init(),
            thirdparty.init(
                sign_in_and_up_feature=thirdparty.SignInAndUpFeature(
                    providers=[
                        ProviderInput(
                            config=ProviderConfig(
                                third_party_id="google",
                                clients=[
                                    ProviderClientConfig(
                                        client_id=os.environ.get("GOOGLE_CLIENT_ID"),
                                        client_secret=os.environ.get(
                                            "GOOGLE_CLIENT_SECRET"
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ]
                )
            ),
        ],
        mode="wsgi",
    )
