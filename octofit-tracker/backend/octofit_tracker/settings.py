# Django settings for octofit_tracker project

# ...existing settings...

# MongoDB Database Configuration
DATABASES = {
    'default': {
        'ENGINE': 'djongo',  # Use djongo as the database engine for MongoDB
        'NAME': 'octofit_db',
    }
}

# CORS Configuration
INSTALLED_APPS += [
    'corsheaders',
    'octofit_tracker',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True
ALLOWED_HOSTS = ['*']
