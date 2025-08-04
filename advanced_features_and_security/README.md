# Advanced Features and Security in Django

This Django project enhances web application security and functionality through custom user models, permission management, secure coding, and HTTPS enforcement.

---

## Task 0: Custom User Model

- Extend `AbstractUser` to create `CustomUser` with `date_of_birth` and `profile_photo`.
- Update `settings.py` with `AUTH_USER_MODEL`.
- Implement `CustomUserManager` with `create_user` and `create_superuser`.
- Register model in `admin.py` and update foreign keys.

---

## Task 1: Permissions and Groups

- Add custom permissions (`can_view`, `can_create`, `can_edit`, `can_delete`) to a model.
- Create groups: Viewers, Editors, Admins.
- Use `@permission_required` in views to enforce access control.
- Test with users assigned to different groups.

---

## Task 2: Security Best Practices

- Set `DEBUG = False` and enable secure headers in `settings.py`.
- Use `{% csrf_token %}` in forms.
- Avoid SQL injection by using Django ORM and validating inputs.
- Implement Content Security Policy (CSP) with `django-csp`.

---

##  Task 3: HTTPS and Secure Redirects

- Enable `SECURE_SSL_REDIRECT`, HSTS settings, and secure cookies.
- Add headers like `X_FRAME_OPTIONS`, `SECURE_CONTENT_TYPE_NOSNIFF`.
- Configure web server (e.g., Nginx) for SSL/TLS.
- Document all security configurations.

