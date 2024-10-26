from urllib.parse import urlparse
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


def normalize_domain(url):
    # Parse the URL to handle protocol and extract netloc (domain part)
    parsed_url = urlparse(url)
    domain = parsed_url.netloc

    # Remove 'www.' if present
    if domain.startswith("www."):
        domain = domain[4:]

    return domain


def check_business_email_valid(email, company_domain):
    email_domain = email.split('@')[-1]
    allowed_domain = normalize_domain(company_domain)

    if email_domain != allowed_domain:
        raise ValidationError({'email': f"Email domain must be '{allowed_domain}'"})
    return email


def create_random_password():
    return User.objects.make_random_password(8)
