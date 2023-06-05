from authlib.integrations.django_client import OAuth

oauth = OAuth()

AUTHLIB_OAUTH_CLIENTS = {
    'lms': {
        # Set your own client_id and secret from earlier.
        'client_id': 'zAN5upjja9j1UAtFKfzSG0DOBvf59NO6VIOFDejn',
        'client_secret': 'IqLWOyMHBzcIdqqGa8PxoQhYTXWtj9sC6WnfNK98uNlxEyun81FL6epwoNhZrRyKXdXgHu9sctXepVRxqUPt1n1B4SiNtEQWNxk7YGqwXZCosETTojgDybWwZroVb6WU',
        # This is where your application will fetch access tokens from.
        'access_token_url': 'http://apps.local.overhang.io/oauth2/access_token',
        'access_token_params': None,
        # This is where your application will redirect the user to
        # authenticate and authorize your application.
        'authorize_url': 'http://apps.local.overhang.io/oauth2/authorize/',
        'authorize_params': None,
        # Authlib creates a client object that does a lot of the
        # heavy HTTP request work for you.
        # You specify the root of the API here. Since there are
        # a lot of different API paths in the LMS, we just pick
        # the root of the LMS as the URL.
        'api_base_url': 'http://apps.local.overhang.io/',
        # The client can be given some additional customization.
        # One thing we need to specify is the 'scopes' our client
        # will need access to. Here are a few of them. The full
        # list of available scopes can be found in the
        # edx-platform source-code, in lms/envs/common.py
        # within the OAUTH2_PROVIDER setting dictionary.
        'client_kwargs': {
            'scope': 'user_id',
            # These next two settings specify how the token should
            # be sent in the HTTP requests to authenticate with
            # the LMS.
            'token_endpoint_auth_method': 'client_secret_basic',
            'token_placement': 'header',
        },
    }
}

for key, value in AUTHLIB_OAUTH_CLIENTS.items():
    # This will register the LMS as a client for Authlib.
    # If you added any other providers to the AUTHLIB_OAUTH_CLIENTS
    # settings dictionary, they'll be added, too.
    oauth.register(key, **value)