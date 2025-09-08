from pathlib import Path
import environ
import os


BASE_DIR = Path(__file__).resolve().parent.parent


env = environ.Env(
DEBUG=(bool, False),
)


environ.Env.read_env(os.path.join(BASE_DIR, ".env"))


DEBUG = env("DEBUG")
SECRET_KEY = env("SECRET_KEY", default="dev-key")
ALLOWED_HOSTS = env("ALLOWED_HOSTS", default="").split() or ["*"]


INSTALLED_APPS = [
"django.contrib.admin",
"django.contrib.auth",
"django.contrib.contenttypes",
"django.contrib.sessions",
"django.contrib.messages",
"django.contrib.staticfiles",
# third party
"rest_framework",
"django_filters",
"drf_yasg",
# local
"employees",
"attendance",
]


MIDDLEWARE = [
"django.middleware.security.SecurityMiddleware",
"django.contrib.sessions.middleware.SessionMiddleware",
"django.middleware.common.CommonMiddleware",
"django.middleware.csrf.CsrfViewMiddleware",
"django.contrib.auth.middleware.AuthenticationMiddleware",
"django.contrib.messages.middleware.MessageMiddleware",
"django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "employee_project.urls"


TEMPLATES = [
{
"BACKEND": "django.template.backends.django.DjangoTemplates",
"DIRS": [BASE_DIR / "templates"],
"APP_DIRS": True,
"OPTIONS": {
"context_processors": [
"django.template.context_processors.debug",
"django.template.context_processors.request",
"django.contrib.auth.context_processors.auth",
"django.contrib.messages.context_processors.messages",
],
},
}
]


WSGI_APPLICATION = "employee_project.wsgi.application"


DATABASES = {
"default": {
"ENGINE": "django.db.backends.postgresql",
"NAME": env("DB_NAME"),
"USER": env("DB_USER"),
"PASSWORD": env("DB_PASSWORD"),
"HOST": env("DB_HOST"),
"PORT": env("DB_PORT"),
}
}


AUTH_PASSWORD_VALIDATORS = [
{"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
{"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
}